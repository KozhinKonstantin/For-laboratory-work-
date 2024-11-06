# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, raz='|'):

    result = list(set(str1.split(raz)).intersection(str2.split(raz)))
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)