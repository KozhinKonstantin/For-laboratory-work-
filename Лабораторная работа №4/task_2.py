# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as csvfile:
        list_ = [row for row in csv.DictReader(csvfile)] #Открываем csv файл для чтения и записываем все строки, которые находятся в файле



    with open(OUTPUT_FILENAME,"w") as write_file:
        json.dump(list_, write_file, indent=4) #Преобразуем список словарей list_ в формат JSON


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
