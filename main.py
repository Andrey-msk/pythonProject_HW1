# 1
name = input("Введите свое имя: ")
surname = input("Введите свою фамилию: ")
print(name)
print(surname)
a = int(input("Введите ваш возраст: "))
b = input("Введите ваш пол: ")
print(a,b)

# 2
t = int(input("Введите время в секундах: "))
hours = t //3600
minutes = (t // 60) - (hours * 60)
seconds = t % 60
print(F't: {hours:02}:{minutes:02}:{seconds:02}')

# 3
n = input("Введите число: ")
print(F'сумма чисел: ={int(n) + int(n + n) + int(n + n + n)}')

# 4
numbers = int(input("Ведите числа: "))
max_number = 0
while numbers != 0:
    number = numbers % 10
    numbers = numbers // 10
    if max_number < numbers:
        max_number = number
print(F"Максимальное цифра: {max_number}")

# 5
revenue = float(input("доходы: "))
costs = float(input("расходы: "))
profit = revenue - costs
if profit > 0:
    print(F'прибыль {profit/costs}')
    num_workers = int(input("штат: "))
    print(F'прибыль на человека {profit/num_workers}')
elif profit < 0:
    print(F'в минус')
else:
    print(F'нет прибыли')

# 6
days = 1
first_jogging = float(input("Starts with: "))
last_jogging = float(input("Ends with: "))
while last_jogging > first_jogging:
    first_jogging += first_jogging*0.1
    days += 1
print(f'Will reach the goal on {days} day')
# подсмотрел у вас это задание,сам не смог решить





