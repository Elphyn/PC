# Даны целые числа k, l. Если числа не равны, то заменить каждое из них одним и тем же числом,
# равным большему из исходных, а если равны, то заменить числа нулями.
__author__ = "Vlad Karelov"

def maxx(a,b):
    if a > b:
        return a
    else:
        return b

def main(k: int,l: int):
    if k != l:
        k,l = maxx(k,l), maxx(k,l)
    else:
        k,l = 0,0
    print(f"k: {k} \nl: {l}")

main(
    int(input("Enter k: ")),
    int(input("Enter l: "))
)




# написать max руками ✔️






