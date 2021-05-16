"""
Testing AbitInfoADT
"""
import unittest
import sys, os

sys.path.insert(0, os.path.dirname('chance_flask/tools'))

from tools import AbitInfoADT


class TestAbitInfoADT(unittest.TestCase):
    """
    Represents tests for AbitInfoAdt
    """
    def setUp(self):
        self.abiturient = AbitInfoADT('chance_flask/data/abiturients_ucu_2019.json',
                                      'chance_flask/data/abiturients_ucu_2020.json',
                                      'chance_flask/data/coefficients')

    def test_grades_loading(self):
        self.assertTrue((dict, type(self.abiturient.grades_2019)))

    def test_specialities_loading(self):
        self.assertEqual(dict, type(self.abiturient.specialties))

    def test_specialities_getter(self):
        sample = ["Богослов'я", 'Історія та археологія', "Комп'ютерні науки",
                  'Культурологія', 'Політологія', 'Право', 'Психологія',
                  'Системний аналіз', 'Соціальна робота', 'Соціологія', 'Філологія']
        self.assertEqual(self.abiturient.get_university_specialties(), sample)

    def test_info_about_speciality_getter(self):
        self.assertEqual(self.abiturient.get_info_by_specialty('Системний аналіз'),
                        [274, 50, 196.76, '75 000'])

    def test_subject_by_speciality(self):
        sample = {'Українська мова та література': 0.25,
                  'Математика': 0.4,
                  'Іноземна мова / Фізика': 0.25,
                  'Середній бал документа про освіту': 0.1}
        self.assertEqual(self.abiturient.get_exams_by_specialty('Системний аналіз'), sample)

    def test_rating_grade_calculator(self):
        input_data = ([180, 180, 180, 10],
                           {'Українська мова та література': 0.35,
                            'Історія України': 0.3,
                            'Географія': 0.25,
                            'Середній бал документа про освіту': 0.1
                            })
        self.assertEqual(self.abiturient.calculate_rating_grade(*input_data), 183.6)

    def test_minimal_element(self):
        self.assertEqual(self.abiturient.grades['Системний аналіз'][0].min(), 193.29)

    def test_maximal_element(self):
        self.assertEqual(self.abiturient.grades['Системний аналіз'][0].max(), 200.0)

    def test_calculate_good_probability(self):
        self.assertEqual(self.abiturient.calculate_chance(200.0, 'Системний аналіз'), '100 %')

    def test_calculate_unsure_probability(self):
        self.assertNotEqual(self.abiturient.calculate_chance(192.5, 'Системний аналіз'), '0 %', '100 %')

    def test_calculate_bad_probability(self):
        self.assertEqual(self.abiturient.calculate_chance(180, 'Системний аналіз'), '0 %')


if __name__ == "__main__":
    unittest.main()
