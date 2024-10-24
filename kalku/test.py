def kalkulator():
    operator = input("Masukkan operator (+, -, *, / ,%): ")
    num1 = int(input("Masukkan nomor pertama: "))
    num2 = int(input("Masukkan nomor kedua: "))

    hasil = 0  
    if operator == "+":
        hasil = num1 + num2
    elif operator == "-":
        hasil = num1 - num2
    elif operator == "*":
        hasil = num1 * num2
    elif operator == "/":
        hasil = num1 / num2

    print(hasil)

kalkulator()