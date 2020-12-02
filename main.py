with open("advent","r") as f:
    data = f.read().splitlines()

print(data)

for i in range(0, len(data)):
    i = int(i)
    o = data[i]
    for b in range(0, len(data)):
        b = int(b)
        if o + data[b] == 2020:
            total = o * data[b]
            print(o,data[b], total)