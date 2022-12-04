import requests
from main_functions import predict_salary, draw_table, get_vacancies_statistic
import time
from dotenv import load_dotenv
import os
import argparse


def predict_rub_salary_for_superJob(vacancy):
    if vacancy["currency"] != "rub":
        return None
    return predict_salary(vacancy["payment_from"], vacancy["payment_to"])


def collect_superjob_vacancies(keywords, superjob_key):
    headers = {"X-Api-App-Id": superjob_key}
    vacancies = {}
    town_id = 4
    profession_id = 48
    number_vacancies_on_page = 20
    vacancies_number_limit = 500
    for word in keywords:
        vacancies[word] = []
        pages_number = 1
        page = 0
        while page < pages_number:
            params = {
                "town": town_id,
                "catalogues": profession_id,
                "keyword": word,
                "page": page,
                "count": number_vacancies_on_page
            }
            try:
                page_response = requests.get(
                    "https://api.superjob.ru/2.0/vacancies/",
                    headers=headers,
                    params=params,
                )
                page_response.raise_for_status()

                page_payload = page_response.json()
                if page_payload["total"] > vacancies_number_limit:
                    pages_number = vacancies_number_limit // number_vacancies_on_page
                elif page_payload["total"] < number_vacancies_on_page:
                    pages_number = 1
                else:
                    pages_number = page_payload["total"] // number_vacancies_on_page
                page += 1

                for vacancy in page_response.json()["objects"]:
                    vacancies[word].append(vacancy)
                print(
                    f"SuperJob. languages: {word}, page {page} from {pages_number} is append"
                )
                time.sleep(0.5)
            except requests.exceptions.HTTPError:
                print("Oops..Try again")
                time.sleep(1)
    return vacancies


def draw_superjob_statistic(languages, superjob_key):
    sj_vacancies = collect_superjob_vacancies(languages, superjob_key)
    sj_statistic = get_vacancies_statistic(
        sj_vacancies, predict_rub_salary_for_superJob
    )
    print()
    draw_table(sj_statistic, "SuperJob Moscow")


if __name__ == "__main__":
    load_dotenv()
    SUPERJOB_API_KEY = os.environ["SUPERJOB_API_KEY"]

    parser = argparse.ArgumentParser(
        description="""Скрипт высчитывает среднюю зарлату по вакансиям разработчиков 
        в г.Москва на сервисе SuperJob в разрезе языков программирования. 
        Выводит итоговую статистику в виде таблицы.
        Требует получения SUPERJOB_API_KEY, который должен быть указан в переменной .env"""
    )
    parser.add_argument(
        "-l",
        "--languages",
        nargs="+",
        help="список языков программирования для поиска вакансий",
    )
    args = parser.parse_args()

    draw_superjob_statistic(args.languages, SUPERJOB_API_KEY)
