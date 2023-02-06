import sys

snp_file = sys.argv[1]

with open(snp_file, "r") as f:
    for line in f:
        line = line.strip()
        input_data = line.split()
        scaffold = input_data[0]
        position = input_data[1]
        ref = input_data[2]
        cons = input_data[-2]
        lines = 0
        diff = 0
        for x in range(3, len(input_data)-2):
            if input_data[x] == "-":
                continue
            #if only using 1 line/strain
            #if input_data[x] != ref:
            #    diff += 1
            #if using more than 1 line/strain
            if input_data[x] != cons:
                diff += 1
            lines += 1
        if lines > 0 and diff < lines and diff > 0:
            print(line)
