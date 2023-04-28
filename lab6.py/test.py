from multiprocessing import Process

def f(x):
    print("Hello", x)


if __name__ == '__main__':
    p = Process(target=f, args=('bob', ))
    p.start()
    p.join()
    