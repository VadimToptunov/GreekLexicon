import requests
from bs4 import BeautifulSoup


def get_all_links() -> list:
    all_links = []
    url = "https://www.lingohut.com/ru/l68/%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B3%D1%80%D0%B5%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9"
    sp = _request_page(url)
    links = sp.find_all("a", class_="background-hover-link")
    for i in links:
        all_links.append(i['href'])
    return all_links


def get_page_lexicon(list_of_links):
    for url in list_of_links:
        soup = _request_page(url)
        greek = soup.find_all("div", class_="col-xs-12 col-sm-12 col-md-6 col-lg-6")
        for gr in greek:
            rus = gr.find("span", class_="vocab-box-english").text
            grw = gr.find("span", class_="vocab-box-spalan").text
            line = str(f'{rus} - {grw}')
            save_page_lexicon_into_file(line + '\n')
    print("Lexicon is saved!")


def save_page_lexicon_into_file(lexicon):
    with open('greek_lexicon.txt', 'a+',  encoding="utf-8") as lex:
        lex.writelines(lexicon)


def get_full_lexicon():
    links = get_all_links()
    get_page_lexicon(links)


def _request_page(url):
    resp = requests.get(url)
    bs = BeautifulSoup(resp.text, 'html.parser')
    return bs


if __name__ == '__main__':
    get_full_lexicon()
