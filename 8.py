w = float(input("Введите кол-во оборотов в секунду: "))
t = int(input("Введите кол-во секунд: "))
krug = int(w * t)
ugol = float((w * t - krug)* 360)
print(ugol)