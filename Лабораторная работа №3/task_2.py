# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, raz='|'):
   res1 = str1.split(raz)
   res2 = str2.split(raz)
   result = list(set(res1).intersection(res2))
   result.sort()
   return result





participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
