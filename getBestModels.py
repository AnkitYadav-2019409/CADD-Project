file1 = open('ModelsWithDope.csv', 'r')
firstLineIgnored = False

dic = {}

for x in file1:
    if(firstLineIgnored == False):
        firstLineIgnored = True
        continue
    lis = x.split(',')
    dic[float(lis[2])] = lis[0]

# Sorting the dictionary
sortedDict = sorted(dic.keys())

for i in sortedDict:
    print("Model Name:", dic[i], "with DOPE score:", i)
