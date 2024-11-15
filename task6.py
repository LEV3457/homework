n = int(input("Введите количество секунд: "))
hours = n // 3600
min = (n - hours * 3600)// 60
sec = (n - ((hours * 3600) + (min * 60)))
print(hours,min,sec)
