"""Example of dealing with Beautiful Soup"""
from bs4 import BeautifulSoup


def read_content(path: str) -> BeautifulSoup:
    """Returns Beautiful Soup object with the content of html page"""
    with open (path, "r", encoding="utf-8") as file:
        content = file.read()
    return BeautifulSoup(content, 'lxml')


def get_title(content: BeautifulSoup) -> str:
    """Returns title of the content"""
    return content.title.text


def get_list(content: BeautifulSoup) -> list:
    """Returns names from the list"""
    return list(map(lambda content: content.text, content.find_all('li')))


def get_paragraphs(content: BeautifulSoup) -> list:
    """Returns texts of all paragraphs"""
    return list(map(lambda content: content.text, content.find_all('p')))


if __name__ == "__main__":
    content = read_content("examples/templates/html_example.html")
    print(content)
    print('-' * 100 + '\n')
    print(get_title(content))
    print('-' * 100 + '\n')
    print(get_list(content))
    print('-' * 100 + '\n')
    print(get_paragraphs(content))
