import csv

result = []
tag = 0
csv_reader = csv.reader(open("2.csv"))
for line in csv_reader:
    if int(line[2]) != tag:
        for i in range(int(line[2]) - tag):
            result.append([])
    mid = []
    mid.append(line[0])
    mid.append(line[1])
    mid.append(line[2])
    result.append(mid)
    tag = int(line[2]) + 1
# print(result)

count = 0
for line in result:
    if len(line) != 0:
        message = line[0] + ',' + line[1] + ',' + line[2]
        print(message)
    else:
        count += 1
        print("")
    # csv_writer.writerows(line)
print("empty: " + str(count))