f = open('temp2.csv')
w = open('output_data/explorations2agents.csv', 'a+')
for line in f.readlines():
    data = line.split(',')
    data = data[2:4] + data[0:2] + data[6:8] + data[4:6] + data[8:]
    data = ','.join(data)
    w.write(line)
    w.write(data)