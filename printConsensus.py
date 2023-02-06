import sys

snpFile = sys.argv[1]
consensusFile = sys.argv[2]

try:
    with open(snpFile) as SNP:
        with open(consensusFile, 'w') as DEST:
            for line in SNP:
                line = line.rstrip()
                input_list = line.split(" ")
                scaffold = input_list[0]
                position = input_list[1]
                ref = input_list[2]
                DEST.write(scaffold + " " + position + " " + ref)

                total = 0
                totalA = 0
                totalC = 0
                totalG = 0
                totalT = 0
                lines = 0
                for i in range(3, len(input_list), 8):
                    lines += 1
                    A = int(input_list[i])
                    a = int(input_list[i+1])
                    C = int(input_list[i+2])
                    c = int(input_list[i+3])
                    G = int(input_list[i+4])
                    g = int(input_list[i+5])
                    T = int(input_list[i+6])
                    t = int(input_list[i+7])

                    line_total = A + a + C + c + G + g + T + t
                    totalA += A + a
                    totalC += C + c
                    totalG += G + g
                    totalT += T + t
                    total += line_total

                    if line_total == 0:
                        DEST.write(" -")
                        continue
                    if (A + a) / line_total > 0.80:
                        if A > 2 and a > 2:
                            DEST.write(" A")
                            continue
                    if (C + c) / line_total > 0.80:
                        if C > 2 and c > 2:
                            DEST.write(" C")
                            continue
                    if (G + g) / line_total > 0.80:
                        if G > 2 and g > 2:
                            DEST.write(" G")
                            continue
                    if (T + t) / line_total > 0.80:
                        if T > 2 and t > 2:
                            DEST.write(" T")
                            continue
                    DEST.write(" -")
                if total == 0:
                    DEST.write(" -\n")
                    continue
                if totalA / total > 0.50:
                    DEST.write(" A")
                if totalC / total > 0.50:
                    DEST.write(" C")
                if totalG / total > 0.50:
                    DEST.write(" G")
                if totalT / total > 0.50:
                    DEST.write(" T")
                DEST.write(" " + str(total / lines) + "\n")
except FileNotFoundError:
    print("cant load file")