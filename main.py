from dotenv import load_dotenv
import os
from main_functions import draw_table, get_vacancies_statistic
from hh_vacancies_collector import draw_hh_statistic
from sj_vacancies_collector import draw_superjob_statistic


if __name__ == "__main__":
    load_dotenv()
    languages = [
        "Python",
        "Java",
        "JavaScript",
        "Ruby",
        "PHP",
        "C++",
        "C#",
        "Go",
        "Swift",
        "C",
    ]
    superjob_key = os.environ["SUPERJOB_API_KEY"]
    
    print(draw_hh_statistic(languages))
    print()
    print(draw_superjob_statistic(languages, superjob_key))
