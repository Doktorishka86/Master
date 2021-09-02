#time = int(input('Введите количество секунд: '))
#days, hours, minutes, seconds = time // 86400, time // 3600 % 24, time // 60 % 60, time % 60
#print(f'{days} дн {hours} час {minutes} мин {seconds} cек')

prime_list_01 = []

for x in range(101):
    prime_list_01.append(x)

for element in prime_list_01:
    if element % 10 == 5 or element % 10 == 0 or 6 <= element % 10 <= 9 or 11 <= element % 100 <= 14:
        print(element, 'процентов')
    elif element % 10 == 1:
        print(element, 'процент')
    elif element % 10 <= 4:
        print(element, 'процента')