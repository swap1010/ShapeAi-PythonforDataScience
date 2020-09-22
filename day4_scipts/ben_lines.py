ben_parker_lines = []
with open("data/spiderman.txt") as f:
    for line in f:
        ben_parker_lines.append(line.strip())

print(ben_parker_lines)
