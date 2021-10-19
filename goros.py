# -*- Coding: utf-8 -*-

import random
import datetime
import os

# Заготовки для трёх предложений
def loadList():
	with open('first.txt', 'r', encoding='utf-8') as file:
		first = file.readlines()
	with open('second.txt', 'r', encoding='utf-8') as file:
		second = file.readlines()
	with open('second_add.txt', 'r', encoding='utf-8') as file:
		second_add = file.readlines()
	with open('third.txt', 'r', encoding='utf-8') as file:
		third = file.readlines()
	return first, second, second_add, third

def gorlist(took):
	znak = ['Овен','Телец','Близнецы','Рак','Лев','Дева','Весы','Скорпион','Стрелец','Козерог','Водолей','Рыбы']
	first, second, second_add, third = loadList()

	# текущая дата
	today = datetime.datetime.today()
	# формируем текст гороскопа
	msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)

	print('-----------------------------------------')
	print(' ', znak[int(took) - 1], ', Ваш гороскоп на', today.strftime("%d-%m-%Y"))
	print('-----------------------------------------')
	print('      \   ^__^ ')
	print('       \  (OO)\_______ ')
	print('          (__)\       )\/\ ')
	print('              ||----W | ')
	print('              ||     || ')
	print('*****************************************\n', msg, '\n*****************************************\n')

def printMenu():
	print(
		'\n'
		'Введите номер знака Зодиака и нажмите Enter:\n'
		'1 - Овен\n'
		'2 - Телец\n'
		'3 - Близнецы\n'
		'4 - Рак\n'
		'5 - Лев\n'
		'6 - Дева\n'
		'7 - Весы\n'
		'8 - Скорпион\n'
		'9 - Стрелец\n'
		'10- Козерог\n'
		'11- Водолей\n'
		'12- Рыбы\n'
		'\n'
		'Нажмите <H> чтобы получить помощь по программе.\n'
		'Нажмите <Q> для завершения программы.\n'
		)

def main():
	print('Hello! Программа "Гороскоп"')
	while True:
		printMenu()
		flag = input()
		os.system('cls')
		if flag in ['q','Q']:
			break
		elif flag in ['h','H']:
			print('Справочная система в разработке.\n')
		elif flag in ['1','2','3','4','5','6','7','8','9','10','11','12']:
			gorlist(flag)
		elif flag in ['t','T']:
			None
		else:
			print('Не понимаю запрос.\n')

if __name__ == '__main__':
	main()
