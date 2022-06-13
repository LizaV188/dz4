"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""

# def add_acc2():
#     # тут я попыталась использовать в функции с глобальную переменную, но все же лучше передавать
#     # глобальную переменную как аргумент функции
#     global acc
#     print('acc', acc)
#     while True:
#         sum1 = input('Введите сумму пополнения счета: ')
#         if sum1.replace('.', '', 1).isdigit():
#             acc += float(sum1)
#             break

import os
ACC_FILE_NAME='acc.txt'
GOODS_FILE_NAME='goods.txt'

history_goods = []

def add_acc(acc_sum):
    # обновляет acc_sum до введенного значения, если это число
    while True:
        sum1 = input('Введите сумму пополнения счета: ')
        if sum1.replace('.', '', 1).isdigit():
            acc_sum += float(sum1)
            return acc_sum

def purchase(acc_sum):
    while True:
        sum1 = input('Введите сумму покупки: ')
        if sum1.replace('.', '', 1).isdigit():
            sum1 = float(sum1)
            if sum1 <= acc_sum:
                balance = acc_sum - sum1
                item_goods = input('Введите название покупки: ')
                history_goods.append([item_goods, sum1])
            else:
                balance = acc_sum
                print('Для покупки недостаточно средств!')
            return (balance)


def print_history():
    if not history_goods:
        print('Покупок еше не было')
    else:
        print('Покупки:')
        for n, x in enumerate(history_goods):
            print(f'{n+1}) {x[0]}: {x[1]}')

def personal_acc():
    acc = 0
    if os.path.isfile(ACC_FILE_NAME):
        with open(ACC_FILE_NAME, 'r') as f:
            acc = float(f.read())
    if os.path.isfile(GOODS_FILE_NAME):
        with open(ACC_FILE_NAME, 'r') as f1:
            for line in f1:
                history_goods.append(line)


    while True:
        print('Текущий счет: ', acc)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню ')
        if choice == '1':
            acc = add_acc(acc)
    #        add_acc2()
        elif choice == '2':
            acc = purchase(acc)
        elif choice == '3':
            print_history()
        elif choice == '4':
            with open(ACC_FILE_NAME, 'w') as f:
                f.write(str(acc))
            with open(GOODS_FILE_NAME, 'w') as f1:
                for i in history_goods:
                    f1.write(", ".join(i))


            break
        else:
            print('Неверный пункт меню ')


if __name__ == '__main__':
    personal_acc()