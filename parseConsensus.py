import sys

snp_file = sys.argv[1]
consensus_file = sys.argv[2]

with open(snp_file, 'r') as snp, open(consensus_file, 'w') as dest:
    for line in snp:
        input_list = line.strip().split(" ")
        scaffold = input_list[0]
        position = input_list[1]
        ref = input_list[2]
        
        dest.write(f"{scaffold} {position} {ref}")
        
        total = 0
        total_a = 0
        total_c = 0
        total_g = 0
        total_t = 0
        lines = 0
        # countNucs
        for x in range(3, len(input_list), 8):
            lines += 1
            A = int(input_list[x])
            a = int(input_list[x + 1])
            C = int(input_list[x + 2])
            c = int(input_list[x + 3])
            G = int(input_list[x + 4])
            g = int(input_list[x + 5])
            T = int(input_list[x + 6])
            t = int(input_list[x + 7])
            
            line_total = A + a + C + c + G + g + T + t
            total_a += A + a
            total_c += C + c
            total_g += G + g
            total_t += T + t
            total += line_total
            
            if line_total == 0:
                dest.write(" - 0 0 0 0")
                continue
            if (A + a) / line_total > 0.80:
                if A > 2 and a > 2:
                    temp = (A + a) / line_total
                    dest.write(f" A {A} {a} {temp} {line_total}")
                    continue
            if (C + c) / line_total > 0.80:
                if C > 2 and c > 2:
                    temp = (C + c) / line_total
                    dest.write(f" C {C} {c} {temp} {line_total}")
                    continue
            if (G + g) / line_total > 0.80:
                if G > 2 and g > 2:
                    temp = (G + g) / line_total
                    dest.write(f" G {G} {g} {temp} {line_total}")
                    continue
            if (T + t) / line_total > 0.80:
                if T > 2 and t > 2:
                    temp = (T + t) / line_total
                    dest.write(f" T {T} {t} {temp} {line_total}")
                    continue
            dest.write(" - - - -")
        if total == 0:
            dest.write(" - 0\n")
            continue
        if total_a / total > 0.50:
            dest.write(" A")
        if total_c / total > 0.50:
            dest.write(" C")
        if total_g / total > 0.50:
            dest.write("G")
        if total_t / total > 0.50:
            dest.write("T")

    print(dest + " ", total/lines)
    print (dest + "\n")

       

