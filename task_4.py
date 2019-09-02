import itertools

# 1. Соединить словари

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic_sum = {**dic1,**dic2,**dic3}

print(dic_sum)


def add_dicts(*dicts):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    print(result)
    return result


add_dicts(dic1, dic2, dic3)

# 2. Написать функцию, которая определяет есть ли ключ в словаре


def check_key(d, k):
    return k in d.keys()


d = {1: True, 2: 'abc', 'msg': 'hello', 'lol': 'laughter'}
check_key(d, 'lol')

# 3. Составить таблицу умножения до 10 с помощью словаря
# 1. option
d = {a: {b: a*b for b in range(10)} for a in range(10)}
print(d)

# 2. option
for a, b in itertools.combinations(range(10), 2):
    print(a, " * ", b, "=", a*b)

# 4. Написать функцию, которая выводит словарь в виде таблицы
d = {1: True, 2: 'abc', 'msg': 'hello', 'lol': 'laughter'}


def print_table(dic_to_table):
    print("| key \t | value \t |")
    for k,v in dic_to_table.items():
        print(f"| {k} \t | {v} \t |")


print_table(d)

# 5. Написать фукцию, которая при объединении двух и более словарей возращает,
#    только те ключи, которые уникальны для каждого.
d1 = {1: True, 2: 'abc', 'd': 'hello'}
d2 = {5: True, 2: 'abc', 'msg': 'hello'}
d3 = {1: True, 4: 'abc', 'msg': 'hello'}


def intersection(*args):
    d = {}
    f, *rest = map(frozenset, map(dict.keys, args))

    for key in rest:
        f = f.symmetric_difference(key)
    for source in args:
        for key in f:
            if key in source:
                d[key] = source[key]
                print(d)
    return d

intersection(d1,d2,d3)

# 6. Найти количество символов букв в тексте. Разничу в регистре (верхний/нижний) - игнорировать
s = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce fermentum volutpat velit, sit amet consequat 
       massa convallis in. Mauris sollicitudin fringilla augue et pellentesque. Curabitur at sapien in dolor 
       malesuada luctus. Nullam. '''


def counter(s):
    count = {}
    s = s.lower()
    for char in s:
        count.setdefault(char, 0)
        count[char] = count[char]+1
    print(count)
    return count


counter(s)

# 7. Написать функцию, которая будет заполнять журнал посещаимости в следующем формате.
j = {
    'Petrov': [{'date': '31.03.2019', 'is_attended': True}]
    }


def change_status(name, date, is_present=True):
    # j = journal.copy() почему когда я копировала journal сверху(сейчас j называется) у меня не подтягивался 2й
    # добавленный ключ 'Ivanov'?

    if name in j.keys():
        for i in range(len(j[name])):
            if date != j[name][i]['date']:
                j[name].append({'date': date, 'is_attended': is_present})
            else:
                j[name][i]['is_attended'] = False
    else:
        j.setdefault(name, [{'date': date, 'is_attended': is_present}])

    print(j)
    return j


change_status('Petrov', '31.03.2019')
change_status('Ivanov', '31.03.2019')
change_status('Petrov', '01.04.2019')
change_status('Ivanov', '01.04.2019')