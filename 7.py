a = int(input("Введите кол-во копеек: "))
x = int(a/100)
y = int((a-x*100)/10)
z = int((a-x*100-y*10)/3)
v = int((a-x*100-y*10-z*3)*4)
print(x,"рублей + ",y,"гривен + ",z,"алтынов + ",v,"полушек")