f = open('temp.csv')
w = open('temp2.csv', 'a+')
lines = f.readlines()

times = set()
for line in lines:
    data = line.split(',')
    time = float(data[-1])
    data = ','.join(data)
    if time not in times:
        w.write(data)
    times.add(time)