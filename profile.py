name, email, address, other_information, years = '', '', '', '', ''
phone_number, post_index, age = 0, 0, 0

import re  
def own_information(name, age, phone_number, email, post_index, address, other_information):
  if 11 <= age % 100 <= 19: years = 'лет'
  elif age % 10 == 1: years = 'год'
  elif 2 <= age % 10 <= 4: years = 'года'
  else: years = 'лет'
  print('Имя: ', name)
  print('Фамилия: ', surname)
  print('Возраст : ', age, years)
  print('Номер телефона: ', phone_number)
  print('Email: ', email)
  print('Индекс: ', replaced)
  print('Адрес: ', address)
  print('Дополнительная информация: ', other_information)
  
def business_information(ogrnip, inn, bank_account, bank, bik, correspondent_account):
  print('\nИнформация о предпринимателе')
  print('ОГРНИП: ', ogrnip)
  print('ИНН: ', inn)
  print('Банковские реквизиты для перевода: ')
  print('Р/c: ', bank_account)
  print('Банк: ', bank)
  print('Бик: ', bik)
  print('К/c: ',  correspondent_account)

def count_digits(numeral): #подсчёт цифр
  count = 0
  while numeral % 10 != 0:
    count += 1
    numeral //= 10
  return count  

print('Приложение MyProfile Business version')
print('Сохраняй информацию о себе и выводи ее в разных форматах') 

while True:
  print('=' * 60)
  print('ГЛАВНОЕ МЕНЮ')
  print('1 - Ввести или обновить информацию')
  print('2 - Вывести информацию')
  print('0 - Завершить работу')
  main_option = int(input('\nВведите номер пункта меню: '))#опции осн.меню
  if main_option == 0:
    print('\nРабота приложения завершена.')
    break
  elif main_option == 1:
    print('=' * 40)
    print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
    print('1 - Личная информация')
    print('2 - Информация о предпринимателе')
    print('0 - Назад')
    option = int(input('\nВведите номер пункта меню: '))
    if option == 1:
      name = input('Введите имя: ')
      surname = input('Введите фамилию: ')
      while age <= 0:
        age = int(input('Введите возраст: '))
        if age < 0:
          print('Возраст должен быть положительный!')
      phone_number = int(input('Введите номер телефона (+7ХХХХХХХXXX): '))
      email = input('Введите адрес электронной почты: ')
      post_index = input('Введите почтовый индекс: ')
      replaced = re.sub('[\D]', '', post_index)
      address = input('Введите почтовый адрес (без индекса): ')
      other_information = input('Введите дополнительную информацию: ')
    elif option == 2:
      count = 0
      while count != 15:
        ogrnip = int(input('ОГРНИП: '))
        count = count_digits(ogrnip)
        if count != 15:
          print('ОГРНИП должен содержать 15 цифр!')
      inn = int(input('ИНН: '))
      while count != 20:
        bank_account = int(input('Расчётный счёт: '))
        count = count_digits(bank_account)
        if count != 20:
          print('Расчётный счёт должен содержать 20 цифр!')
      bank = input('Название банка: ')
      bik = int(input('БИК: '))
      correspondent_account = int(input('Корреспондентский счёт: '))
    else: print('Введите корректный пункт меню')
  elif main_option == 2:
    print('=' * 40)
    print('ВЫВЕСТИ ИНФОРМАЦИЮ')
    print('1 - Личная информация')
    print('2 - Вся информация')
    print('0 - Назад')
    option = int(input('\nВведите номер пункта меню: '))
    if option == 0:
      print('Возврат в предыдущее меню')
    elif option == 1:
      own_information(name, age, phone_number, email, post_index, address, other_information)
    elif option == 2:
      own_information(name, age, phone_number, email, post_index, address, other_information)
      business_information(ogrnip, inn, bank_account, bank, bik, correspondent_account)
    else: print('\nВведите корректный пункт меню')
  else:      
    print('\nВведите корректный пункт меню.')
