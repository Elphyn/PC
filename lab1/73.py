# Даны целые числа k, l. Если числа не равны, то заменить каждое из них одним и тем же числом, равным большему из исходных, а если равны, то заменить числа нулями.
__author__ = "Vlad Karelov"

def main(k: int,l: int):
    if k != l:
        k,l = max(k,l), max(k,l)
    else:
        k,l = 0,0
    print(f"k: {k} \nl: {l}")

main(
    k = int(input("Enter k: ")),
    l = int(input("Enter l: "))
)






