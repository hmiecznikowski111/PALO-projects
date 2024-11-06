y = 'AAAABCBCAZZZZ'
x = 'AAAABCBCAZZZYZZ'
def lider(x):
    flag = True
    lider = ['', 0]
    for i in x:
        c = x.count(i)
        if c > lider[1]:
            flag = True
            lider = [i, c]
        elif c == lider[1]:
            if lider[0] != i:
                flag = False
    if flag:
        return lider
    return [None,'']

def lider2(x):
    lider = ['', 0]
    for i in x:
        c = x.count(i)
        if c > lider[1]:
            lider = [i, c]
    return lider

def lider3(x):
    lider = ['', 0]
    for i in x:
        c = x.count(i)
        if c >= lider[1]:
            lider = [i, c]
    return lider

def lider4(x):
    lider = [[], 0]
    for i in x:
        c = x.count(i)
        if c > lider[1]:
            lider = [[i], c]
        elif c == lider[1] and i not in lider[0]:
            lider[0].append(i)
    return lider

print('Example')
print(*lider4(x))
