import sys

mut_file = sys.argv[1]
cvg_file = sys.argv[2]
out_file = sys.argv[3]

pos_hash = {}
with open(mut_file) as f_mut:
    for line in f_mut:
        line = line.strip()
        input_ = line.split()
        poskey = " ".join([input_[0], input_[1], input_[2]])
        pos_hash[poskey] = poskey

with open(cvg_file) as f_cvg, open(out_file, 'w') as f_out:
    for line in f_cvg:
        line = line.strip()
        input_ = line.split()
        newkey = " ".join([input_[0], input_[1], input_[2]])

        if newkey not in pos_hash:
            continue
        else:
            f_out.write(line + "\n")
