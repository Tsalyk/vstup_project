"""Tools module"""
from arrays import Array
from arrays import DynamicArray
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
    def __init__(self, applicants_path: str, subjects_path: str):
        """
        Initialize ADT
        info_path: Файл з даними про кількість місць на спеціальності, кількість заявок, ціну навчання та середній бал у минулому році.
        applicants_path: Файл з даними про результати зно вступників на всі спеціальності
        subjects_path: Файл з даними про коефіцієнти та потрібні предмети на кожну спеціальність
        """
        self.grades = self.get_grades_from_json(applicants_path)
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
                        data.append(line[line.find(':')+1:].strip())
                    else:
                        data.append(line)
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
        with open(path, 'r') as json_file:
            data = json.load(json_file)

        for key, value in data.items():
            entered, rejected = Array(len(value[0])), Array(len(value[1]))
            for i, j in zip(range(len(value[0])), range(len(value[1]))):
                entered[i] = value[0][i]
                rejected[j] = value[1][j]
            data[key] = entered, rejected

        return data

    def get_specialties_by_university(self, university = None):
        """
        Returns list of specialties from subjects_path 
        with chosen university and specialty.

        e.g.
        ["Artes Liberales", "Business Analytics", "Computer Science", ...]
        """
        pass

    def get_info_by_specialty(self, university, specialty):
        """
        Returns list of items from info_path 
        with chosen university and specialty.

        Indexes:
        0: Число поданих заяв 2020 - int/str
        1: Ліцензований обсяг - int/str
        2: Середній рейтинговий бал вступників - int/str
        3: Вартість навчання (з пробілом) - str

        e.g.
        [403, 50, 197.66, "75 000"]
        """
        pass

    def get_exams_by_specialty(self, university, specialty):
        """
        Returns list of tuples from subjects_path 
        with chosen university and specialty.

        Indexes:
        0: Предмет і коеф - tuple
        1: Предмет і коеф - tuple
        2: Предмет і коеф - tuple
        3: Середній бал і коеф - tuple

        e.g.
        [("MATHEMATICS", 0.4), ("UKRAINIAN", 0.2), ("ENGLISH", 0.3), ("GRADE", 0.1)]
        """
        pass

    def calculate_rating_grade(self, grades_list, coefficients_list):
        """
        Return calculated rating grade from a given list of grades and
        coefficients.

        e.g.
        197.2 - float
        """
        pass

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

        e.g.
        98%
        """
        pass
