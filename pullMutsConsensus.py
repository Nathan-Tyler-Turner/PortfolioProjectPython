import sys

mut_file = sys.argv[0]
cons_file = sys.argv[1]
out_file = sys.argv[2]

try:
    with open(mut_file, 'r') as mut, open(cons_file, 'r') as cons, open(out_file, 'w') as dest:
        pos_hash = {}
        for line in mut:
            line = line.strip()
            input = line.split()
            pos_key = ' '.join(input[0], input[1], input[2])
            pos_hash[pos_key] = pos_key

        dest.write("test\n")

        for line in cons:
            line = line.strip()
            input = line.split()
            new_key = ' '.join(input[0], input[1], input[2])

            if new_key in pos_hash:
                dest.write(line + "\n")
except IOError:
    print("Cannot load file")
