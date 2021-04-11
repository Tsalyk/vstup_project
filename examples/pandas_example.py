"""Example of dealing with Pandas"""
import pandas as pd


def read_csv_file(path: str) -> pd.DataFrame:
    """Returns data from csv"""
    with open(path, "r", encoding="utf-8") as file:
        data = pd.read_csv(file)
    return data


def max_rate_grade(data: pd.DataFrame) -> pd.Float64Index:
    """Returns the highest rate grade"""
    return data.max().get(key=" rateGrade")


def min_rate_grade(data: pd.DataFrame) -> pd.Float64Index:
    """Returns the lowest rate grade"""
    return data.min().get(key=" rateGrade")


if __name__ == "__main__":
    data = read_csv_file("examples/test_pandas.csv")
    print(max_rate_grade(data))
    print(min_rate_grade(data))
