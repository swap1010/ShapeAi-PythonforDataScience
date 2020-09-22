f = open('data/spiderman.txt', 'r')
file_data = f.read()
f.close()
print(file_data)
with open('data/my_file.txt', 'r') as f:
    file_data = f.read()

print(file_data)
