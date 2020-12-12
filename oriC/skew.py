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
    plt.show()
    fig.savefig("sequence.png")

if __name__ == "__main__":
    S = "CATGGGCATCGGCCATACGCC"

    #plot_skew(S)
    seq = get_dna_seq().getvalue().lower()
    #print(seq.lower())
    print(plot_skew((skew(seq))))

    




    
