# Дано натуральное число n. Вычислить: 
__author__ = "Vlad Karelov"

def calc(n):
    k = 1
    result = 0
    for k in range(k,n):
        result += 1/(2*k+1)**2
    return result 
    # print(f"Result: {result}")


# print(calc(
#     int(input("Enter n"))
# ))
result = calc(int(input("Enter n")))
print(f"Result: {result:.4f}")