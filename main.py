
ans = [[]]
sp = ["r","x","p","a","m","s","c","t","k","f"]
dicts = {
        "r": [3, 25],
        "x": [3, 20],
        "p": [2, 15],
        "a": [2, 15],
        "m": [2, 20],
        "s": [2, 20],
        "c": [2, 20],
        "t": [1, 25],
        "k": [1, 15],
        "f": [1, 15],
        }


def recurs(i, dl, sp_ans, count):
    global ans, sp, dicts
    summa = 190
    if dicts[sp[i]][0] + dl <= 8:
        dl += dicts[sp[i]][0]
        count += dicts[sp[i]][1]
        sp_ans.append(sp[i])
        for j in range(i+1, 10):
            recurs(j, dl, sp_ans.copy(), count)
        if summa - count < count:
            ans.append(sp_ans.copy())
            ans[0].append(count)

recurs(0, 0, [], 0)





#print(*ans)
for ind, sp in enumerate(ans[1::]):
    table = [[0 for _ in range(3)] for _ in range(3)]
    table[2][2] = "i"
    for el in sp:
        if dicts[el][0] == 3:
            table[0] = [el for _ in range(3)]
        if dicts[el][0] == 2:
            if table[1][0] == 0:
                table[1][0] = el
                table[2][0] = el
            else:
                table[1][1] = el
                table[2][1] = el
        else:
            if table[1][1] == 0:
                table[1][1] = el
            elif table[1][2] == 0:
                table[1][2] = el
            else:
                table[2][1] = el
    for line in table:
        print(*line)
    print(f"Итоговые очки выживания: {ans[0][ind] - 190 + ans[0][ind]}")
    print("-------")

