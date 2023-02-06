import sys

pileupFile = sys.argv[1]

with open(pileupFile) as PILEUP:
    for line in PILEUP:
        line = line.strip()
        input = line.split("\t")
        ref = input[2].upper()
        lcref = ref.lower()
        mut = input[3]
        if "*" in mut or "*" in ref:
            continue
        input[4] = input[4].replace(".", ref).replace(",", lcref).replace("$", "")
        bases = list(input[4])
        aCount = 0
        ACount = 0
        gCount = 0
        GCount = 0
        cCount = 0
        CCount = 0
        tCount = 0
        TCount = 0
        starCount = 0
        indelCount = 0
        x = 0
        while x < len(bases):
            if bases[x] == "^":
                x += 1
                continue
            if bases[x] in "+-" :
                x += 1
                indelCount += 1
                indelSize = ""
                while x < len(bases) and bases[x].isdigit():
                    indelSize += bases[x]
                    x += 1
                x += int(indelSize)
            if bases[x] == "A":
                ACount += 1
            if bases[x] == "a":
                aCount += 1
            if bases[x] == "C":
                CCount += 1
            if bases[x] == "c":
                cCount += 1
            if bases[x] == "G":
                GCount += 1
            if bases[x] == "g":
                gCount += 1
            if bases[x] == "T":
                TCount += 1
            if bases[x] == "t":
                tCount += 1
            if bases[x] == "*":
                starCount += 1
            x += 1
        print("\t".join(map(str, [input[0], input[1], input[2], input[3], ACount, aCount, CCount, cCount, GCount, gCount, TCount, tCount, starCount, indelCount])))
