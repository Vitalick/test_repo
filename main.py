n = int(input()) # ввод первой строки
ns = list(map(int, input().split(" "))) # ввод второй строки, создание из неё списка str, применение к каждому элементу списка функции int, преобразование обратно к списку из типа map
tot = sum(ns) # сумма элементов списка
if tot % 5 == 0 and len(ns) > 4:
    sm = int(tot / 5)
    ns = sorted(ns, reverse=True)
    ps = "Yes"
    su = 0
    sk = 0
    b = False
    for n in ns:
        if n != 0 and b:
            su == 0
            sk += 1
            b = False
            break
        if sk == 5:
            ps = "No"
            break
        su += n
        if abs(su) > abs(sm):
            ps = "No"
            break
        if su == sm:
            b = True
    print(ps)
else:
    print("No")