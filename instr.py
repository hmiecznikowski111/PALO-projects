file = open('instrukcje.txt')

data = []
for f in file:
    data.append(f.strip().split())

gata = []
for d in data:
    #['DOPISZ', 'A']
    if d[0] == 'DOPISZ':
        gata.append(d[1])
fata = list(set(gata))
winner = ['?', 0]
for f in fata:
    x = gata.count(f)
    if x > winner[1]:
        winner = [f, x]
print(winner)
