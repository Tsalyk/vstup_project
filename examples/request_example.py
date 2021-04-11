"""Example of dealing with requests"""
import requests as req


def get_response(url: str) -> req.models.Response:
    """Returns response by url"""
    return req.get(url)


def get_text(response: req.models.Response) -> str:
    """Returns html from response"""
    return response.text


def get_links(response: req.models.Response) -> dict:
    """Returns links from header, if there were such"""
    return response.links


def is_ok(response: req.models.Response) -> bool:
    """Returns True if response was received, False otherwise"""
    return response.ok


if __name__ == "__main__":
    url = 'http://osvita.ua/vnz/rating/vstup-osvita/'
    response = get_response(url)
    print(get_text(response))
    print('-' * 100 + '\n')
    print(get_links(response))
    print('-' * 100 + '\n')
    print(is_ok(response))
