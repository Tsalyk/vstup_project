"""Module for making research with different inputs"""
import sys, os
sys.path.insert(0, os.path.dirname('chance_flask/tools'))
from tools import AbitInfoADT


def get_chance(rate_grade: float, speciality: str) -> str:
    """
    Returns probability entering the speciality with rate grade
    Available specialities:
    Богослов'я
    Історія та археологія
    Комп'ютерні науки
    Культурологія
    Політологія
    Право
    Психологія
    Системний аналіз
    Соціальна робота
    Соціологія
    Філологія
    """
    abiturient = AbitInfoADT('chance_flask/data/abiturients_ucu_2019.json',
                             'chance_flask/data/abiturients_ucu_2020.json',
                             'chance_flask/data/coefficients')
    return (f"Chance of entrance into {speciality} with rate grade {rate_grade}: "
            f"{abiturient.calculate_chance(rate_grade, speciality)}")


if __name__ == "__main__":
    for i in range(190, 201):
        print(get_chance(i, 'Системний аналіз'))
