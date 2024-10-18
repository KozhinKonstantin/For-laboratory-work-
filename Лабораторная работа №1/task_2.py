data = 1.44    #Мбайт
n_page = 100
n_str = 50
n_sim = 25
sim_data = 4   #байт


data_book = n_page*n_str*n_sim * sim_data   # Сколько весит одна книга(в байтах)
data_book_Mbates = data_book / (1024*1024)  #Переводим в Мбайты
numbers_of_book = int(data // data_book_Mbates)  #Ищем количество книг

# TODO Найдите количество книг, которое можно разместить на дискете
print("Количество книг, помещающихся на дискету:", numbers_of_book)
