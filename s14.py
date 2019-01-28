import collections
from collections import Counter

d = ['Vasilsa': ['ручка', 'ручка', 'карандаш', 'ластик'],
     'Vasya': ['ластик', 'картинка', 'шпора']]
#значением может быть все что угодно, а ключем не может быть изменяемый объект

student, item = input('Имя ученика и предмет: ').split()
list_of_items = d[student]
count = list_of_items.count(item)
#.count - это метод, который есть у каждого списка
print(count)

print(*d['Вася'], sep=', ')


#нам нужен словарь, в котором значениями будут словари
#с предметом и его количеством, а ключами - ученики
counter = Counter()
#можем так писать, потому что импортировали Counter отдельно в начале
for name, list_of_items in d.items():
    d[student] = Counter(list_of_items)

print(d)
student, item = input('Имя ученика и предмет: ').split()
print(d[student][item])

item = input('предмет:')
count = 0
for counter in d.values():
    count += counters[item]
print(count)

while True:
    input_ = input('Ученик предмет:')
    if not input_:
        break
    student, item = input_.split()
    #if student not in d: #тут мы создаем пустой пенал для нового ученика
        #d[student] = Counter()
    #d[student][item] += 1

    counter = d.setdefault(student, Counter())
    counter[item] += 1
    

    
    #for key, value in d.items():
        #if student == None:
           #d[student] = 
        
        









    
    
    
    
