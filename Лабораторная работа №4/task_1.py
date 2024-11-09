# TODO решите задачу
import json
def task() -> float:
    with open("input.json", "r") as rfile:
        data = json.load(rfile) #Считываем данные из файла и представляем их в виде Python-объекта

    result = sum([item["score"] * item["weight"] for item in data]) #Находим сумму всех произведений score и weight в словаер data
    return round(result, 3) #Возвращаем результат округленный до 3 знаков


print(task())
