angka1 = (input("masukan angka pertama :"))
angka2 = (input("masukan angka kedua :"))

print("tambah(+), kurang(-), kali(*), bagi(/)")

operator = input("pilih salah satu operator : ")

if operator == '+':
    operator = angka1 + angka2
elif operator == '-':
    operator = angka1 - angka2
elif operator == '*':
    operator = angka1 * angka2
elif operator == '/':
    operator = angka1 / angka2
else:
    print("operator yang anda gunakan tidak sesuai")
        

print(operator)
