#!/usr/bin/env python3

from format import get_dna_seq
import sys
from util import get_kv
def skew(seq):
    diff = 0                            # track G - C for very new nucleotide encountered
    min_pos = []                        # track position where G - C changed from decreasing to increasing
    for v in seq.lower():
        if v == "g":
            diff += 1
        elif v == "c":
            diff -= 1
        min_pos.append(diff)
    return min_pos


def plot_skew(y, org):
    import matplotlib.pyplot as plt
    plt.style.use('classic')
    fig = plt.figure()
    x = [i for i in range(len(y))]
    plt.plot(x, y)
    plt.title("Skew Plot of Genome")
    plt.xlabel("genome")
    plt.ylabel("#G - #C")
    #plt.show()
    fig.savefig("./res/{}_skew_plot.png".format(org))

def min_pos(seq):
    MIN_SEQ = min(seq)
    for i, v in enumerate(seq):
        if v == MIN_SEQ:
            return i , MIN_SEQ
    return None
            
def L_seq_near_min_skew(pos, min_value, L, seq):
    ''' Return an L length sequence (symmetric)
        from the genome around min_skew
        value postion
    '''
    return  seq[pos: pos + L]

def save_result(org):
    fname = "./res/{}_oric_prediction.txt".format(org)
    seq = get_dna_seq(' '.join(org.split("_"))).getvalue().lower()
    positions = skew(seq)
    pos, min_value = min_pos(positions)
    plot_skew(positions, org)
    L = 700
    with open(fname, "w") as f:
        f.write("POSITION: {} \nOF MINIMUM SKEW VALUE: {}\n".format(pos, min_value))
        f.write("POSSIBLE ORIC REGION :\n{}\n".format(L_seq_near_min_skew(pos, min_value, L, seq)))

if __name__ == "__main__":
    #plot_skew(S)
    #seq = get_dna_seq().getvalue().lower()
    #print(seq.lower())
    #print(plot_skew((skew(seq))))
    #pos, min_value = min_pos(skew(seq))
    if len(sys.argv) != 3:
        print("Usage: {} <genus> <species>".format(sys.argv[0]))
        sys.exit(1)
    else:
        org, _ = get_kv(" ".join([sys.argv[1], sys.argv[2]]))
        save_result(org)

    




    
