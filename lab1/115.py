# Дано натуральное число n. Вычислить: 
__author__ = "Vlad Karelov"

def calc(n):
    k = 1
    result = 0
    for k in range(k,n):
        result += 1/(2*k+1)**2 
    print(f"Result: {result}")


calc(
    n = int(input("Enter n"))
)