file = open("Advent.txt")
data = []

for line in file:
    line = line.strip()
    data.append(line)

data = list(map(int, data))

print(data)

for i in data:
    for b in data:
        for s in data:
            if i + b + s == 2020:
                total = i * b * s
                print(i,"*",b,"*",s,"=", total)