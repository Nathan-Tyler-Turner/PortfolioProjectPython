import sys

align_pos_file = sys.argv[1]
cvg_file = sys.argv[2]

with open(align_pos_file, "r") as align:
    with open(cvg_file, "w") as cvg:
        for line in align:
            line = line.strip()
            input_list = line.split(" ")
            scaffold = input_list[0]
            position = input_list[1]
            ref = input_list[2]

            cvg.write(" ".join([scaffold, position, ref]))

            total = 0
            totalA = 0
            totalC = 0
            totalG = 0
            totalT = 0
            lines = 0

            for i in range(3, len(input_list), 8):
                lines += 1
                A = int(input_list[i])
                a = int(input_list[i + 1])
                C = int(input_list[i + 2])
                c = int(input_list[i + 3])
                G = int(input_list[i + 4])
                g = int(input_list[i + 5])
                T = int(input_list[i + 6])
                t = int(input_list[i + 7])

                line_total = A + a + C + c + G + g + T + t
                total += line_total

                cvg.write(" " + str(line_total))

            cvg.write(" " + str(total / lines) + "\n")
