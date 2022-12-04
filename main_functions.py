import requests
from statistics import mean
from terminaltables import DoubleTable


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_from and not salary_to:
        return salary_from * 1.2
    elif not salary_from and salary_to:
        return salary_to * 0.8
    else:
        return None


def get_vacancies_statistic(vacancies, predict_rub_salary_func):
    vacancies_statistic = {}
    for language in vacancies:
        salaries = []
        for vacancy in vacancies[language]:
            salary = predict_rub_salary_func(vacancy)
            if salary:
                salaries.append(salary)
        if not salaries:
            average_salary = 0
        else:
            average_salary = int(mean(salaries))

        vacancies_statistic[language] = {
            "vacancies_found": len(vacancies[language]),
            "vacancies_processed": len(salaries),
            "average_salary": average_salary,
        }
    return vacancies_statistic


def draw_table(vacancies_statistic, title):
    raw_table = [
        [
            "Язык программирования",
            "Вакансий найдено",
            "Вакансий обработано",
            "Средняя зарплата",
        ]
    ]
    for language in vacancies_statistic:
        raw_table.append(
            [
                language,
                vacancies_statistic[language]["vacancies_found"],
                vacancies_statistic[language]["vacancies_processed"],
                vacancies_statistic[language]["average_salary"],
            ]
        )
    table_instance = DoubleTable(raw_table, title)
    return table_instance.table
