import csv
import os
from scrap_category_url import get_category_urls, next_page_url, scrap_category_books, export_list_to_csv, export_single_book_to_csv
from typing import Dict, List, Tuple, Any
from Book_Scraper import scrap_book_url


base_url = 'https://books.toscrape.com/index.html'


def export_categories_dictionaries_and_images() -> List[Tuple[str, List[Dict]]]:
    """
    :param: Give 'https://books.toscrape.com/catalogue/page-1.html' url
    :return: Create a list of tuples with category name and dictionary. Exports the dictionary to csv using
    the category name as file name
    """
    category_urls_and_names = get_category_urls(base_url)
    all_category_and_dictionary_tuples = [
        (category_url_and_name[1] + '.csv', scrap_category_books(category_url_and_name[0])) for
        category_url_and_name in category_urls_and_names]
    saving_path = os.path.join('/Users/Henry/Desktop/gitprojects/Open_Classroom_projects/Project2')
    if not os.path.isdir(saving_path):
        os.makedirs(saving_path)
    os.chdir(saving_path)
    for category_and_dictionary_tuple in all_category_and_dictionary_tuples:
        export_list_to_csv(category_and_dictionary_tuple[1], (category_and_dictionary_tuple[0]))


def export_dictionary_and_image(url: str, file_name: str) -> Dict:
    export_single_book_to_csv(scrap_book_url(url), file_name)


def export_category_dictionaries_and_images(url: str, category_name: str) -> List[Dict]:
    export_list_to_csv(scrap_category_books(url), category_name)


# export_dictionary_and_image('https://books.toscrape.com/catalogue/frankenstein_20/index.html', "Frankenstein")
# export_category_dictionaries_and_images('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html', 'mystery.csv')
# export_categories_dictionaries_and_images()
