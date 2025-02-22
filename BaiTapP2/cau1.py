a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

S1 = a ** 2 - 2 * b + a*b/(c**2 + 3)
S2 = (b ** 2 - 4 * a * c ) / (2 * a)
S3 = 3 * a - b ** 3 + 2 * ((c**2 + 1) ** 0.5)
S4 = ((a**2)/b -4*a/(b*c) +1) ** 0.5

print(f"S1 = {S1:.3f} ")
print(f"S2 = {S2:.3f} ")
print(f"S3 = {S3:.3f} ")
print(f"S4 = {S4:.3f} ")