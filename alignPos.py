import sys

posFile = sys.argv[1]
joinList = sys.argv[2]
outFile = sys.argv[3]

with open(posFile, 'r') as f1, open(joinList, 'r') as f2, open(outFile, 'w') as f3:
    posHash = {}
    for line in f1:
        line = line.strip()
        input = line.split()
        poskey = ' '.join(input[:3])
        posHash[poskey] = poskey

    for line in f2:
        fileName = line.strip()
        hash = {}
        try:
            with open(fileName, 'r') as f:
                for line in f:
                    line = line.strip()
                    input = line.split()
                    newkey = ' '.join(input[:3])
                    hash[newkey] = ' '.join(input[3:])
        except FileNotFoundError:
            continue

        for key in posHash:
            if newkey not in hash:
                posHash[key] = ' '.join([posHash[key]] + [0,0,0,0,0,0,0,0])
            else:
                posHash[key] = ' '.join([posHash[key]] + [hash[newkey]])
        print(fileName)

    sorted_posHash = sorted(posHash.keys(), key=lambda x: (x.split()[0], int(x.split()[1])))

    for element in sorted_posHash:
        f3.write(posHash[element] + '\n')
