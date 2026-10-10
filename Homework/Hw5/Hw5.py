import csv
import json
from pathlib import Path


# Task1
# 1.Напишите три функции
# - 1.1 save_test_ids(test_ids) — принимает список ID тестов и сохраняет их в tests.txt.
# Каждый ID должен находиться на отдельной строке.
# - 1.2  add_test_id(test_id) — добавляет один новый ID в конец существующего файла,
# не удаляя предыдущие записи.
# - 1.3  load_test_ids(filename) — читает файл и возвращает список ID.
# Пустые строки нужно пропускать, пробелы по краям удалять.
# Пример исходного списка->["QA-1001", "QA-1002", "QA-1003"]
# После вызова add_test_id("QA-1004") функция load_test_ids("tests.txt") должна вернуть:
# ["QA-1001", "QA-1002", "QA-1003", "QA-1004"]
# Используйте: def, return, for, list, append(), with open(), режимы w, a, r, strip().
# Проверьте пустой список, повторное добавление записи и чтение файла с пустыми строками.


def save_test_ids(*test_ids):
    with open("tests.txt","w",encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(test_id+"\n")
            # file.write("QA-1001\n")    # - проверка на  пустые строки и пробелы
            # file.write("   \n")
            # file.write("  QA-1002  \n")
            # file.write("\n")

save_test_ids("QA-1001", "QA-1002", "QA-1003")

def add_test_id(test_id):
    with open("tests.txt", "a", encoding="utf-8") as file:
        file.write(test_id+"\n")

add_test_id("QA-1004")

def load_test_ids(filename):
    result = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()
            if test_id != "":  # Если строка после strip() пустая, мы её не добавляем в список
                result.append(test_id)

    return result

print(load_test_ids("tests.txt"))
# save_test_ids()
# print(load_test_ids("tests.txt")) #- проверка на пустой список
# add_test_id("QA-1004")
# print(load_test_ids("tests.txt")) #- добавляем тот же ID - работает


print("____________")

# Task 3
# Напишите две функции:
# •save_test_config(environment, base_url, timeout) — создаёт config.json и сохраняет параметры тестового окружения.
# •load_test_config(filename) — читает JSON и возвращает словарь с настройками.
# Пример вызова
# save_test_config(
#     "staging",
#     "https://example.com",
#     30
# )
# Ожидаемый JSON {
#     "environment": "staging",
#     "base_url": "https://example.com",
#     "timeout": 30
# }
# —-----------
# 1.Для сохранения используйте json.dump().
# 2.Для чтения используйте json.load().
# 3.Сохраняйте данные с отступами для удобного чтения.
# 4.Проверьте, что после загрузки тип timeout остаётся int.
# 5.Проверьте, что повторное сохранение заменяет старую конфигурацию.
#
# Используйте: dict, json.dump(), json.load(), with open(), type(), assert.

def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

save_test_config("staging", "https://example.com", 30)

def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        config = json.load(file) # превращаем json файл в Python-словарь

    return config

config = load_test_config("config.json")

print(config)
print(type(config["timeout"]))

# Проверяем результат
assert config["environment"] == "staging"
assert config["base_url"] == "https://example.com"
assert config["timeout"] == 30
assert type(config["timeout"]) is int
# Это проверка: тип значения timeout должен быть именно int
# Если условие верно, программа продолжает работу. Если неверно, Python выдаёт ошибку AssertionError

print("____________")

# Task 2
# Создайте файл results.csv
# test_id,status,duration_ms
# QA-1001,PASSED,120
# QA-1002,FAILED,230
# QA-1003,PASSED,150
# Напишите функцию get_test_statistics(filename)
#
# Функция должна:
# 1.Прочитать данные из CSV.
# 2.Посчитать общее количество тестов.
# 3.Посчитать количество PASSED и FAILED.
# 4.Найти суммарное время выполнения тестов в миллисекундах.
# 5.Собрать в список ID всех проваленных тестов.
# 6.Вернуть словарь с результатом
# Ожидаемый резальт->
# {
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500,
#     "failed_ids": ["QA-1002"]
# }
# Используйте: csv.DictReader(), for, if, dict, list, int(), append(), return.
# Считайте, что в корректном входном файле статусы могут быть только PASSED и FAILED, а время — целое неотрицательное число.
# Дополнительно проверьте файл, содержащий только заголовки. Все счётчики должны быть равны нулю, список ошибок — пустой.

def get_test_statistics(filename):
    statistics = {              # создаем словарь с начальными значениями
        "total": 0,
        "passed": 0,
        "failed": 0,
        "total_duration_ms": 0,
        "failed_ids": []
    }

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # представляем каждую строку как словарь
                                    # причем значения CSV изначально читаются как строки

        for row in reader:
            statistics["total"] += 1  # Для каждой строки увеличиваем общее количество тестов на единицу
                                           # Считаем успешные и проваленные тесты
            if row["status"] == "PASSED":   # Если статус PASSED, увеличиваем счётчик успешных тестов
                statistics["passed"] += 1
                                            # Если статус FAILED, увеличиваем счётчик ошибок
                                            # и добавляем ID проваленного теста в список через append()
            if row["status"] == "FAILED":
                statistics["failed"] += 1
                statistics["failed_ids"].append(row["test_id"])
                                            # Считаем суммарное время
            statistics["total_duration_ms"] += int(row["duration_ms"])
# Почему нужен int()? Потому что CSV возвращает "120" как строку, а нам нужно число 120, чтобы складывать время.

    return statistics


print(get_test_statistics("results.csv"))

# Дополнительная проверка: файл содержит только заголовки
# создали results_empty.csv  с только заголовками test_id,status,duration_ms
print(get_test_statistics("results_empty.csv"))
# печатает {'total': 0, 'passed': 0, 'failed': 0, 'total_duration_ms': 0, 'failed_ids': []}
# for row in reader не выполнит ни одной итерации, если после заголовков нет данных

# дополнительная проверка на пустой файл не требуется, т.к. мы заранее создаём словарь с нулевыми счётчиками

print("____________")

# Task 4  Advanced
# Вы работаете QA Engineer. После запуска автоматизированных тестов необходимо создать отчёт для команды.
# Напишите функцию build_run_report(project_name, csv_filename)
# Функция получает название проекта и путь к CSV-файлу в формате из Task 2.
# Она должна
# 1.Прочитать все результаты тестирования.
# 2.Посчитать total, passed, failed, total_duration_ms.
# 3.Создать папку reports.
# 4.Внутри неё создать папку с названием проекта.
# 5.Создать файл summary.json с общей статистикой.
# 6.Создать файл failed_tests.txt, в который записать ID всех тестов со статусом FAILED.
# 7.Вернуть словарь с итоговой статистикой.
#
# Пример
# build_run_report("Shop", "results.csv")
# reports/
#     Shop/
#         summary.json
#         failed_tests.txt


def build_run_report(project_name, csv_filename):
    # 1. Создаём словарь для статистики
    statistics = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "total_duration_ms": 0,
        "failed_ids": []
    }

    # 2. Читаем CSV и считаем статистику
    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            statistics["total"] += 1

            if row["status"] == "PASSED":
                statistics["passed"] += 1

            if row["status"] == "FAILED":
                statistics["failed"] += 1
                statistics["failed_ids"].append(row["test_id"])

            statistics["total_duration_ms"] += int(row["duration_ms"])

    # 3. Создаём папку проекта
    project_folder = Path("reports") / project_name
    project_folder.mkdir(parents=True, exist_ok=True)
                # Если project_name равен "Shop", путь будет reports/Shop
                # - parents=True — создаёт также папку reports, если её ещё нет.
                # - exist_ok=True — не выдаёт ошибку, если папка уже существует

    # 4. Сохраняем общую статистику в JSON
    summary = {
        "total": statistics["total"],
        "passed": statistics["passed"],
        "failed": statistics["failed"],
        "total_duration_ms": statistics["total_duration_ms"]
    }

    with open(project_folder / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)
            # Записывает словарь summary в файл .json .
            # Здесь мы сохраняем только общие показатели, без списка failed_ids

    # 5. Сохраняем ID проваленных тестов
    with open(project_folder / "failed_tests.txt", "w", encoding="utf-8") as file:
        for test_id in statistics["failed_ids"]:
            file.write(test_id + "\n")
            # Цикл проходит по списку проваленных тестов и записывает каждый ID с новой строки.
            # Если проваленных тестов нет, файл будет создан, но останется пустым

    # 6. Возвращаем итоговую статистику
    return statistics
    # Возвращает все показатели, включая список failed_ids. Поэтому их можно использовать дальше в программе,
    # например для проверки результатов автоматизированного запуска


result = build_run_report("Shop", "results.csv")
print(result)
