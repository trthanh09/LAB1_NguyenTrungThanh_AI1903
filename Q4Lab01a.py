# Ý 1 Q4:
try:
    number1 = float(input("Nhập vào một số thực a: "))
    number2 = float(input("Nhập vào một số thực b: "))
    number3 = float(input("Nhập vào một số thực c: "))
    print(f"Số thập phân {number1} trong bát phân là: {oct(int(number1))}")
    print(f"Số thập phân {number2} trong bát phân là: {oct(int(number2))}")
    print(f"Số thập phân {number3} trong bát phân là: {oct(int(number3))}")
except:
    print("Hãy nhập số thực !!!")
# Ý 2 Q4:
print(f"Số thực {number1} lấy sau dấu phẩy 2 chữ số là: {number1:.2f}")
print(f"Số thực {number2} lấy sau dấu phẩy 2 chữ số là: {number2:.2f}")
print(f"Số thực {number3} lấy sau dấu phẩy 2 chữ số là: {number3:.2f}")