import math

# Ý 1
a = float(input("Nhập số thực a là: "))
b = float(input("Nhập số thực b là: "))
c = float(input("Nhập số thực c là: "))
x = float(input("Nhập số thực x là: "))

# Ý 2
S1 = a * x**2 + b * x + c
print("Đáp án của S1 là", S1)
# Ý 3
hamso = b**2 - 4 * a * c
if hamso > 0:
    S2 = math.sqrt(hamso) / (2 * a)
    print("Đáp án của S2 là", S2)
else:
    S2 = 0
    print("Đáp án của S2 = 0")

# Ý 4
print("Nhập lại giá trị a, b, c để tính tam giác:")
a = float(input("Nhập giá trị của a là: "))
b = float(input("Nhập giá trị của b là: "))
c = float(input("Nhập giá trị của c là: "))

# Ý 5
if a + b <= c or a + c <= b or b + c <= a:
    print("a, b, and c không phải là cạnh của tam giác")
else:
    # Chu vi
    perimeter = a + b + c

    # Nửa chu vi
    s = perimeter / 2

    # Diện tích
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("Chu vi của tam giác là:", perimeter)
    print("Diện tích của tam giác là:", area)