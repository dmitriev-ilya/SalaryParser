from main_functions import predict_salary, draw_table, get_vacancies_statistic
import requests
import time
import argparse


def predict_rub_salary_hh(vacancy):
    if vacancy["salary"]:
        salary = vacancy["salary"]
        if salary["currency"] != "RUR":
            return None
        return predict_salary(salary["from"], salary["to"])


def collect_hh_vacancies(keywords):
    vacancies = {}
    professional_role_id = 96
    city_id = 1
    days = 30
    for word in keywords:
        vacancies[word] = []
        pages_number = 1
        page = 0
        while page < pages_number:
            params = {
                "professional_role": professional_role_id,
                "area": city_id,
                "period": days,
                "text": word,
                "search_field": "name",
                "page": page,
            }
            try:
                page_response = requests.get(
                    "https://api.hh.ru/vacancies", params=params
                )
                page_response.raise_for_status()

                page_payload = page_response.json()
                pages_number = page_payload["pages"]
                page += 1

                for vacancy in page_response.json()["items"]:
                    vacancies[word].append(vacancy)
                print(
                    f"HeadHunter. languages: {word}, page {page} from {pages_number} is append"
                )
                time.sleep(0.5)
            except requests.exceptions.HTTPError:
                print("Oops..Try again")
                time.sleep(1)
    return vacancies


def draw_hh_statistic(languages):
    hh_vacancies = collect_hh_vacancies(languages)
    hh_statistic = get_vacancies_statistic(hh_vacancies, predict_rub_salary_hh)
    print()
    draw_table(hh_statistic, "HeadHunter Moscow")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Скрипт высчитывает среднюю зарлату по вакансиям разработчиков 
        в г.Москва на сервисе HeadHunter в разрезе языков программирования. 
        Выводит итоговую статистику в виде таблицы."""
    )
    parser.add_argument(
        "-l",
        "--languages",
        nargs="+",
        help="список языков программирования для поиска вакансий",
    )
    args = parser.parse_args()

    draw_hh_statistic(args.languages)
