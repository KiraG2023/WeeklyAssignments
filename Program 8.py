def print_seq(seq):
    if len(seq) > 19:
        print(seq[30])
        print_seq(seq[10:])
        seq = ([5, 10, 17, 18, 19])
print_seq(seq)
