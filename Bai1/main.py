import time

def tinh1(a, x):
    kq = 0

    for i in range(len(a)):
        kq = kq + a[i] * (x**i)

    return kq

def tinh2(a, x):
    kq = a[-1]

    for i in range (len(a) - 2 , -1 , -1):
        kq = a[i] + x * kq
    return kq

def tinh_time(f, a, x):
    start = time.time()
    f(a, x)
    end = time.time()
    return end - start

x = 1.000001
ds = [1000, 10000, 100000]

print("\nKet qua:")
print("-" * 75)
print("{:<10} {:<20} {:<20}".format("n", "Thoi gian (Cach 1)", "Thoi gian (Cach 2)", "Nhan xet"))
print("-" * 75)

for n in ds:
    a = [1] * (n + 1)

    t1 = tinh_time(tinh1, a, x)
    t2 = tinh_time(tinh2, a, x)

    if t1 > t2:
        nhanxet = "Cach 2 nhanh hon"
    elif t1 < t2:
        nhanxet = "Cache 1 nhanh hon"
    else:
        nhanxet = "Hai cach bang nhau"
    print("{:<10} {:<20.8f} {:<20.8f} {:<20}".format(n, t1, t2, nhanxet ))
print("-" * 75)
