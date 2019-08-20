#task_1
books_list = []


def order_by_alphabet(li, *books):
    book_list = li[:]
    book_list.extend(books)
    book_list.sort()
    print(book_list)
    # нет return


books_list = order_by_alphabet(books_list, 'Anna', 'Coco', 'Bob', 'Zorg')
books_list = order_by_alphabet(books_list, 'Home', 'Go', 'Na', 'La')
order_by_alphabet('Ad', 'Jo', 'Pa', 'Ma')  # А это работать не будет
# но можно сделать li keyword-аргументом
# def order_by_alphabet(*books, li)
# не стоит делать значением по умолчанию list(), он будет изменяемым.

#task_2
numbers_list = [1.5,2,3,4,5,(),3,4,2,4.5,5,6,22,55,33,'b']


def number_in_the_list(number):
    # А ты умеешь смотреть в документацию ;)
    print(f"{number} is found in the list " + str(numbers_list.count(number)) + ' times')


number_in_the_list(4)

#task_3
def sum_of_even_numbers(num_list):
    sum_of_num = 0
    print(list(enumerate(num_list, 1)))
    for i in enumerate(num_list, 1):  # enumerate - кортеж из кортежей
    # Можно написать проще
    # for idx, element in in enumerate(num_list, 1):
        if (i % 2) and isinstance(num_list[i], (int,float)):  # Тут ошибка i - кортеж
            sum_of_num += num_list[i]
            print(sum_of_num)
        else:
            pass
    # for i in range(len(num_list)):
    #     if i % 2 and isinstance(num_list[i], (int,float)):
    #         sum_of_num += num_list[i]
    #         print(sum_of_num)
    #     else:
    #         pass
    print(f'Total sum is {sum_of_num}')


sum_of_even_numbers(numbers_list)


#task_4

a = input("Please enter some words: ").split()


def find_max_from_list(max_item):
    print("Max item is : ", max(max_item))  # это не работает для строк
    # можно написать max(map(len, max_item)),
    # или реализовать через цикл


find_max_from_list(a)

#task_5

a = input("Please enter some words: ").split()  # split - возвращает список
b = [list(i) for i in a]
print(b)


def is_not_empty(list_of_lists):
    # Самый простой способ
    # return any(list_of_lists)
    for i in list_of_lists:
        if len(i) > 0:
            print(f"{list_of_lists.index(i)} of lists is not empty")
        else:
            print(f"{list_of_lists.index(i)} list is empty")
    # Или так
    # for i in list_of_lists:
    #     if not i:
    #         return False
    # return True


is_not_empty(b)

#task_6

l = input("Please enter some words: ").split()
new_string = ''.join(l)
print(new_string)
