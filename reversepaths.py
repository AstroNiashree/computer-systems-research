f = open('output_data/explorations2agents.csv')
w = open('output_data/explorations2agents.csv', 'a+')
for line in f.readlines()[27953:]:
    data = line.split(',')
    data = data[4:8] + data[0:4] + data[8:]
    # print(data)
    data = ','.join(data)
    w.write(data)