# Парсер статистики по вакансиям разработчиков на HeadHunter и SuperJob.

Проект представляет собой набор скриптов для автоматизации сбора информации о вакансиях разработчиков в г.Москва на таких ресурсах как HeadHunter и SuperJob.

Основной скрипт выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе самых популярных языков программирования.
Полный список поиска:
* "Python"
* "Java"
* "JavaScript"
* "Ruby"
* "PHP"
* "C++"
* "C#"
* "Go"
* "Swift"
* "C"

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Помимо этого, для работы понадобится создать файл `.env` в корневом каталоге проекта. Данный файл необходим для работы с переменными окружения и должен содержать в себе переменные: 
```
SUPERJOB_API_KEY=<SUPERJOB_API_KEY>
``` 
Для получения `SUPERJOB_API_KEY` необходимо сгенерировать ключ согласно [инструкции](https://api.superjob.ru/). 

## Использование скриптов

Проект включает в себя несколько скриптов для автоматизации сбора информации с разных площадок.

### Основной исполняемый скрипт `main.py`
Выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе самых популярных языков программирования, сразу для двух площадок HeadHunter и SuperJob.

Пример запуска:
```bash
$python3 main.py
```
Пример работы скрипта:

![image](https://user-images.githubusercontent.com/67222917/205433896-45742a6e-dfda-4682-a290-3bd3eb81032b.png)

### Вспомогательный скрипт `hh_vacancies_collector.py`
Выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе указанных языков программирования на HeadHunter (г.Москва).

Принимает обязательный аргумент: 
* "-l", "--languages", - список языков программирования для поиска вакансий.


Пример запуска:
```bash
$python3 hh_vacancies_collector.py -l 'Python', 'Ruby', 'Swift'
```
Пример работы аналогичен основному скрипту.

### Вспомогательный скрипт `sj_vacancies_collector.py`
Выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе указанных языков программирования на SuperJob (г.Москва).
Требует получения SUPERJOB_API_KEY, который должен быть указан в переменной .env

Принимает обязательный аргумент: 
* "-l", "--languages", - список языков программирования для поиска вакансий.


Пример запуска:
```bash
$python3 sj_vacancies_collector.py -l 'Python', 'Ruby', 'Swift'
```
Пример работы аналогичен основному скрипту.
