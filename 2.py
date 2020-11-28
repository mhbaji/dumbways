dataArray = ['a', 'b', 'c', 'd', 'e']

def putarArray(data):
    for i in range(0,4):
        dataTemp = data[0]
        # print(len(data))
        for j in range(0,len(data)-1):
            data[j] = data[j+1]
        data[len(data)-1] = dataTemp
        print(data)

putarArray(dataArray)