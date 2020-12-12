#!/usr/bin/env python3

from format import get_dna_seq
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


def plot_skew(y):
    import matplotlib.pyplot as plt
    plt.style.use('classic')
    fig = plt.figure()
    x = [i for i in range(len(y))]
    plt.plot(x, y)
    plt.title("Skew Plot of Genome")
    plt.xlabel("genome")
    plt.ylabel("#G - #C")
    #plt.show()
    fig.savefig("sequence.png")

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
    return  seq[pos - L//2 : pos + L//2].upper()

def save_result():
    fname = "./res/result1.txt"
    seq = get_dna_seq().getvalue().lower()
    positions = skew(seq)
    pos, min_value = min_pos(positions)
    plot_skew(positions)
    L = 500
    with open(fname, "w") as f:
        f.write("POSITION: {} \nOF MINIMUM SKEW VALUE: {}\n".format(pos, min_value))
        f.write("POSSIBLE ORIC REGION :\n{}\n".format(L_seq_near_min_skew(pos, min_value, L, seq)))

if __name__ == "__main__":
    #plot_skew(S)
    #seq = get_dna_seq().getvalue().lower()
    #print(seq.lower())
    #print(plot_skew((skew(seq))))
    #pos, min_value = min_pos(skew(seq))
    save_result()

    




    
