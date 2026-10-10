from pathlib import Path   # инструмент Python для работы с путями к файлам и папкам


data_folder = Path("data_test")
# Создаём объект пути к папке data_test. Сама папка при этом не создаётся
file_path = data_folder/"test.csv"
# Оператор / соединяет путь к папке и имя файла
print(file_path)
# Выводит путь к файлу:  data_test\test.csv
print(file_path.exists())
# Метод .exists() проверяет, существует ли объект по этому пути — файл или папка
# True — существует
# Если файла test.csv пока нет в папке data_test, результат будет False
# Важно: этот код не создаёт ни папку data_test, ни файл test.csv

screen_folder = Path("screen")
# строка задаёт путь к папке screen
screen_folder.mkdir(exist_ok=True)
# строка создаёт эту папку с помощью .mkdir()
# Параметр exist_ok=True означает: если папка уже существует, не выдавать ошибку
# Без этого параметра повторный запуск кода может привести к ошибке FileExistsError, если папка уже создана.
reports_folder = Path("reports")/"october"
# строка задаёт путь к вложенной папке reports/october
reports_folder.mkdir(parents=True,exist_ok=True)
# строка создаёт папки по этому пути
# parents=True — создать и родительскую папку reports, если её ещё нет, и вложенную папку october
# exist_ok=True — не выдавать ошибку, если конечная папка october уже существует