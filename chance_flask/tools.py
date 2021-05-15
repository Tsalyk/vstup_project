"""Tools module"""
from arrays import Array, DynamicArray
import json


class AbitInfoADT:
    """
    Class for storing and processing university data.

    User logic:
    Input university -> Recieve list of specialties.
    Input specialty -> Recieve grade coefficients and specialty info.
    Input grades -> Recieve rating grade and a chance of enrollment.

    Від Тіми:
    Для реалізації класу беріть якийсь АДТ, а не просто лісти.
    Всі потрібні виводи я прописав. 
    Я всюди прописував параметр university, але можете його забрати, бо у нас поки лише УКУ.
    Ініціалізація буде відбуватись завдяки записуванню даних з файлів у якийсь АДТ. 
    Функції для цього я не прописував, але робіть їх staticmethod'aми десь під самим __init__().
    Можете міняти вигляд того, що приймає функція, але потрібні саме такі ретурни.
    Для функції calculate_chance краще робити допоміжні функції.
    """
    def __init__(self, applicants_2019_path: str, applicants_2020_path: str, subjects_path: str):
        """
        Initialize ADT
        info_path: Файл з даними про кількість місць на спеціальності, кількість заявок, ціну навчання та середній бал у минулому році.
        applicants_path: Файл з даними про результати зно вступників на всі спеціальності
        subjects_path: Файл з даними про коефіцієнти та потрібні предмети на кожну спеціальність
        """
        self.grades = self.get_grades_from_json(applicants_2020_path)
        self.grades_2019 = self.get_grades_from_json(applicants_2020_path)
        self.specialties = self.get_specialties_info(subjects_path)



    @staticmethod
    def get_specialties_info(path:str) -> dict:
        '''
        Returns a dict with data about specialties.
        Keys are specialties names and values it are
        DynamicArray ADT.
        DynamicArray ADT format:(price,amount,subj,min grade, coef, subj....)
        '''
        specialties = {}
        data = DynamicArray()
        with open(path, 'r',encoding='UTF-8') as university_data:
            speciality = university_data.readline()[3:].strip()
            for line in university_data:
                line = line.strip()
                if line and line[0].isdigit():
                    specialties[speciality] = data
                    speciality = line[line.find(' '):].strip()
                    data = DynamicArray()
                elif line:
                    if line.find(':') != -1:
                        data.append(float(line[line.find(':')+1:].strip()))
                    else:
                        data.append(line)
        specialties[speciality] = data
        return specialties


    @staticmethod
    def get_grades_from_json(path: str) -> dict:
        """
        Returns a dict with grades, where
        a key is the name of the speciality;
        a value consists of 2 Arrays ADT which contain grades (float);
        first Array - grades those, who entered the university;
        second Array - grades those, who were rejected
        """
        with open(path, 'r', encoding="UTF-8") as json_file:
            data = json.load(json_file)

        for key, value in data.items():
            entered, rejected = Array(len(value[0])), Array(len(value[1]))
            for i in range(len(value[0])):
                entered[i] = value[0][i]
            for j in range(len(value[1])):
                rejected[j] = value[1][j]
            data[key] = entered, rejected
        return data

    def get_university_specialties(self):
        """
        Returns list of specialties from subjects_path 
        with chosen university and specialty.

        e.g.
        ["Artes Liberales", "Business Analytics", "Computer Science", ...]
        """
        return list(self.specialties.keys())

    def get_info_by_specialty(self, speciality=None):
        """
        Returns list of items from info_path 
        with chosen university and specialty.

        Indexes:
        0: Число поданих заяв 2020 - int
        1: Ліцензований обсяг - int
        2: Середній рейтинговий бал вступників - round(float, 2)
        3: Вартість навчання (з пробілом) - str

        e.g.
        [403, 50, 197.66, "75 000"]
        """
        if not speciality:
            return ["?", "?", "?", "?"]
        specialty_info = self.specialties[speciality]
        specialty_grades = self.grades[speciality]
        quantity = 0
        for i in range(2):
            quantity += len(specialty_grades[i])
        speciality_price = str(int(specialty_info[0]))[:-3] + " " + str(int(specialty_info[0]))[-3:]
        license_quantity = specialty_info[1]
        average_note = round(sum(specialty_grades[0])/len(specialty_grades[0]),2)

        return [quantity, int(license_quantity), average_note, speciality_price]

    def get_exams_by_specialty(self, specialty):
        """
        Returns list of tuples from subjects_path
        with chosen university and specialty.

        Indexes:
        0: Предмет і коеф - tuple
        1: Предмет і коеф - tuple
        2: Предмет і коеф - tuple
        3: Середній бал і коеф - tuple

        e.g.
        {'Українська мова та література' : 0.35,
         'Історія України' : 0.3,
         'Іноземна мова (На вибір)' : 0.25,
         'Географія (На вибір)' : 0.25,
         'Середній бал документа про освіту' : 0.1}
        """
        if not specialty:
            return {'EXAM 1' : 0.5,
         'EXAM 2' : 0.25,
         'EXAM 3' : 0.25,
         'GRADE' : 0.1}
        specialty_info = self.specialties[specialty]
        result = {}
        idx = 2
        third_zno = ""
        third_zno_coef = 0
        while specialty_info[idx] != specialty_info[len(specialty_info)-2]:
            if "На вибір" in specialty_info[idx]:
                if third_zno == "":
                    third_zno = specialty_info[idx].replace(" (На вибір)","")
                else:
                    third_zno += " / " + specialty_info[idx].replace(" (На вибір)","")
                third_zno_coef = specialty_info[idx + 2]
            else:
                result[specialty_info[idx]] = specialty_info[idx+2]
            idx += 3
        if third_zno_coef != 0:
            result[third_zno] = third_zno_coef
        result[specialty_info[len(specialty_info)-2]] = specialty_info[len(specialty_info)-1]
        return result

    def calculate_rating_grade(self, grades_list, coefficients_dict):
        """
        Return calculated rating grade from a given list of grades and
        coefficients.
        calculate_rating_grade({"Українська мова та література" : 192.2,
                                "Історія України" : 199.9,
                                "Іноземна мова (На вибір)" : 195.7,
                                "Середній бал документа про освіту" : 11.5
                                },
                                {'Українська мова та література' : 0.35,
                                 'Історія України' : 0.3,
                                 'Іноземна мова (На вибір)' : 0.25,
                                 'Географія (На вибір)' : 0.25,
                                 'Середній бал документа про освіту' : 0.1
                                 }
                                )

        e.g.
        197.2 - float
        """
        grades_dict = {}
        i = 0
        for exam in coefficients_dict.keys():
            grades_dict[exam] = grades_list[i]
            i += 1

        print(grades_dict)
        result = 0
        for subject,grade in grades_dict.items():
            try:
                grade = float(grade)
            except TypeError:
                grade = 0
                print(grade)
            if subject == 'Середній бал документа про освіту':
                if grade > 2:
                    grade = min( (grade-2)/0.1 , 100) + 100
                else:
                    grade = 100
            normal = grade * coefficients_dict[subject]
            result += normal
        return min(result * 1.02, 200)


    def calculate_chance(self, rating_grade, university, specialty):
        """
        Return chance of entering specialty at university
        with a given rating grade from applicants_path.

        Method:
        1. Зчитати дані по спеціальності по різних роках.
        2. Порахувати в яких межах варіюється кількість тих, хто міг пройти, але відмовився.
        3. Порахувати динаміку середнього балу вступників
        4. Знайти "проміжок неточності" на основі динаміки та меж відмов.
        5. Якщо rating_grade не входить в проміжок, вивести 100% або 0%.
        6. Якщо rating_grade входить в проміжок, то:
            *. симулювати рандомні значення з визначених проміжків 10 000 раз та вивести відсоток тих,
                в яких rating_grade було достатньо.

        calculate_chance( 199.2, "ucu", "Системний аналіз")
        e.g.
        98%
        """
        abiturients_2020 = self.grades[specialty]
        abiturients_2019 = self.grades_2019[specialty]

        max_grade_2020,min_grade_2020 = max(abiturients_2020[0]), min(abiturients_2020[0])
        max_grade_2019,min_grade_2019 = max(abiturients_2019[0]), min(abiturients_2019[0])

        def find_refused_quantity(abiturients_year, min_grade_year):
            refused_quantity_year = 0
            refused_persons = []
            for person in abiturients_year[1]:
                if person > min_grade_year:
                    refused_quantity_year += 1
                    refused_persons.append(person)
            return refused_quantity_year, max(refused_persons), min(refused_persons)

        refused_quantity_2020, max_refused_grade_2020, min_refused_grade_2020 = find_refused_quantity(abiturients_2020, min_grade_2020)
        refused_quantity_2019, max_refused_grade_2019, min_refused_grade_2019 = find_refused_quantity(abiturients_2019, min_grade_2019)

        average_grade_2019 = abiturients_2019[0].average()
        average_grade_2020 = abiturients_2020[0].average()




ABIT = AbitInfoADT("chance_flask/data/abiturients.json", "chance_flask/data/coefficients")

if __name__ == "__main__":
    test = AbitInfoADT("chance_flask/data/abiturients.json", "chance_flask/data/coefficients")
    print(test.get_exams_by_specialty('Богослов’я'))
    test.calculate_rating_grade({"Українська мова та література": 200,
                            "Історія України": 200,
                            "Іноземна мова (На вибір)": 200,
                            "Середній бал документа про освіту": 8.9
                            },
                           {'Українська мова та література': 0.35,
                            'Історія України': 0.3,
                            'Іноземна мова (На вибір)': 0.25,
                            'Географія (На вибір)': 0.25,
                            'Середній бал документа про освіту': 0.1
                            }
                           )
