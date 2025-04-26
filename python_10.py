# swap variable without using third variable/temp

a = 5
b = 10

# swaping witout a temporary variable
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)