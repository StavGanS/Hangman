import json 
import time
import random

attempt = 5
op = random.randint(1, 3)
res = 0

class word:

    def __init__(self,name):
        with open('./ls.json', 'r', encoding = 'utf-8') as f:
                import_data = json.load(f)
        for slovo in import_data:
            if slovo['name'] == name:
                podskazka = slovo['podskazka'] 
                podskazka2 = slovo['podskazka2']
        self.name = name  
        self.podskazka = podskazka
        self.podskazka2 = podskazka2

    def call(self):
        print(f'Слово - {self.name}')
    
    def call2(self):
        print(f'Подсказка - {self.podskazka}')
    
    def call3(self):
        print(f'Ещё одна подсказка - {self.podskazka2}')

def vou():
    if answer == lll.name[0]:
        res += 1
        print(f'Буква "{answer}" есть в данном слове! Идём дальше!')
        answer = input('-'*25 + '\nВведите следующую букву:\n-->')

def word1():
    global res, attempt
    lll = word('Лыжи')
    print('-'*25 + f'\nПриветсвую тебя, мой друг!\nСейчас ты должен будешь угадать слово!\nТвоё кол-во попыток: {attempt}\n' + '-'*25)
    lll.call2()
    answer = input('-'*25 + '\nВведите 1-ую букву:\n-->')
    while res != 4 or attempt != 0:
        if answer == lll.name[0]:
            res += 1
            print(f'Буква "{answer}" есть в данном слове! Идём дальше!\nСлово - К...')
        if answer != lll.name[0]:
            attempt -= 1
            print(f'Такой буквы в слове нет!\nВаше кол-во попыток - {attempt}')
            lll.call3()
        if res == 4:
            print('Ты угадал слово! Молодец!')

def word2():
    global res, attempt
    lll = word('Компьютер')
    print('-'*25 + f'\nПриветсвую тебя, мой друг!\nСейчас ты должен будешь угадать слово!\nПодсказка: все слова начинаются с заглавной буквы\nТвоё кол-во попыток: {attempt}\n' + '-'*25)
    lll.call2()
    answer = input('-'*25 + '\nВведите 1-ую букву:\n-->')
    while res != 9 or attempt != 0:
        if answer == lll.name[0]:
            res += 1
            print(f'Буква "{answer}" есть в данном слове! Идём дальше!')
            answer = input('-'*25 + '\nВведите следующую букву:\n-->')
        if answer != lll.name[0]:
            attempt -= 1
            print(f'Такой буквы в слове нет!\nВаше кол-во попыток - {attempt}')
            lll.call3()
        if res == 9:
            print('Ты угадал слово! Молодец!')

def word3():
    global res, attempt
    lll = word('Смартфон')
    print('-'*25 + f'\nПриветсвую тебя, мой друг!\nСейчас ты должен будешь угадать слово!\nПодсказка: все слова начинаются с заглавной буквы\nТвоё кол-во попыток: {attempt}\n' + '-'*25)
    lll.call2()
    answer = input('-'*25 + '\nВведите 1-ую букву:\n-->')
    while res != 8 or attempt != 0:
        if answer == lll.name[0]:
            res += 1
            print(f'Буква "{answer}" есть в данном слове! Идём дальше!')
            answer = input('-'*25 + '\nВведите следующую букву:\n-->')
        if answer != lll.name[0]:
            attempt -= 1
            print(f'Такой буквы в слове нет!\nВаше кол-во попыток - {attempt}')
            lll.call3()
        if res == 8:
            print('Ты угадал слово! Молодец!')

if op == 1:
    word1()
elif op == 2:
    word2()
else:
    word3()