# Nhập số thực
a = float(input("Nhập số thực đầu tiền là: "))
b = float(input("Nhập số thực thứ hai là: "))
c = float(input("Nhập số thực thứ ba là: "))

# Tìm max và min
maximum = max(a, b, c)
minimum = min(a, b, c)
print("Giá trị lớn nhất là:" (maximum))
print("Giá trị nhỏ nhất là:" (minimum))

# Sắp xếp thứ tự
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print("Cách sắp xếp theo thứ tự tằng dần là:" (a), (b), (c))