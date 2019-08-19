# task_1

s = input('Please enter some characters: ')
if (len(s) % 2) == 0:
    print('Number is Even')
else:
    print('Number is Odd')


# task_2
s1 = '0a2b4c6d8e'

def is_number_correct(s):
    if len(s) != 10:
        return False
    for i in range(len(s)):
        if not (i % 2) and not s[i].isdigit():
            print('The number is not correct')
    print('The number is correct')


is_number_correct(s1)


#task_3

s2 = input('Please enter a sentence: ')
last_letter = s2[-1:]
for i in enumerate(s2):
    if i[1] == last_letter:
        print(i[0] + 1)
indices = [i+1 for i, x in enumerate(s2) if x == last_letter]
print(indices)


#task_4

s3 = input('Please enter a sentence: ')

if s3.find('x') == -1 or s3.find('w') == -1:
    print('X or W is not found')
else:
    if s3.find('x') - s3.find('w') > 0:
        print('W was found first')
    else:
        print('X was found first')


# task_5

s5 = input('Please enter some characters: ')
if len(s5) > 10:
    print(s5[:6])
else:
    for i in s5:
        if len(s5) < 12:
            s5 = s5 + 'o'
    print(s5)


# task_6

s6 = input('Please enter a sentence: ')
words_list = s6.split(' ')
print(len(words_list))


#task_7

s7 = input('Please enter 10 characters: ')

for i in range(len(s7)):
    if (i % 2 == 0) and (s7[i] != 'a' or 'b'):
        s7 = s7[:i] + 'a' + s7[i+1:]
    else:
        s7 = s7[:i] + 'c' + s7[i + 1:]
print(s7)


# task_8

s8 = input('Please enter long string: ')
if s8.lower().startswith('abc'):
    print('www' + s8[3:])
else:
    print(s8 + 'zzz')


# task_9

s9 = input('Please enter first string: ')
s9_1 = input('Please enter second string: ')

s9_first_symbols = s9[0:4]
s9_last_symbols = s9[-4:]
s9_1_first_symbols = s9_1[0:4]
s9_1_last_symbols = s9_1[-4:]

if s9_first_symbols == s9_1_first_symbols and s9_last_symbols ==  s9_1_last_symbols:
    print('First and Last symbols match')
else:
    print('Symbols do not match')


#task_10

s10 = input('Please enter 0-10 characters: ')
if len(s10) % 2 == 0:
    middle_position = len(s10)//2
    print(s10[:middle_position-1] + s10[middle_position-1].lower()
          + s10[middle_position].lower() + s10[middle_position+1:])
else:
    middle_position = len(s10) // 2
    print(s10[:middle_position] + s10[middle_position].lower() + s10[middle_position+1:])