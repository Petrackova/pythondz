"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

strr = input()
punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_—~'''
COUNT_FREQUENCY = 10

for ele in strr:
    if ele in punctuation_marks:
        strr = strr.replace(ele, "")
strr = strr.lower()
strr = strr.split()
my_dict_1 = {}

for i in range(len(strr)):
    my_dict_1[strr[i]] = my_dict_1.get(strr[i], 0)+1

sorted_dict = sorted(my_dict_1.items(), key=lambda x: x[1], reverse=True)
sorted_dict = sorted_dict[:COUNT_FREQUENCY]
print()
ten_dict = dict(sorted_dict)
for key, value in ten_dict.items():
    print(key, '-', value)


