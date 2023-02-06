import sys


infile = sys.argv[1]
try:
    with open(infile, 'r') as source:
        source_data = source.read().split(">")
        source_data = [x for x in source_data if x]  # remove empty strings
        for data in source_data:
            header, sequence = data.split("\n", 1)
            seqid = header.split()[0]
            sequence = sequence.replace("\n", "")
            input_list = list(sequence)
            n = 1
            for element in input_list:
                print(f"{seqid} {n} {element.upper()}")
                n += 1
except FileNotFoundError:
    print("Cannot load file")
