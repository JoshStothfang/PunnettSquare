import sys
from Genotype import Genotype
from collections import Counter

def main():
    parent1 = Genotype(sys.argv[1])
    parent2 = ""
    
    # If only one genotype is provided, it is assigned to both parent1 and parent2.
    if len(sys.argv) == 2:
        parent2 = parent1
    else:
        parent2 = Genotype(sys.argv[2])

    if len(parent1.genotype) % 2 != 0 or len(parent2.genotype) % 2 != 0:
        print("ERROR: Genotypes must have an even number of characters.")
        return

    if len(parent1.genotype) != len(parent2.genotype):
        print("ERROR: Genotypes must be the same length.")
        return

    children = []

    for combo1 in parent1.alleleCombos:
        for combo2 in parent2.alleleCombos:
            children.append(breed(combo1, combo2))
    
    output = []

    for child in Counter(children):
        output.append((Counter(children).get(child) / len(children), child))

    output.sort(reverse=True)

    for percent, genotype in output:
        print(str(percent * 100) + "%", genotype, sep="\t")

def breed(combo1, combo2):
    child = ""
    for i in range(len(combo1)):
        if ord(combo1[i]) > ord(combo2[i]):
            child += combo2[i]
            child += combo1[i]
        else:
            child += combo1[i]
            child += combo2[i]
    return child

if __name__ == "__main__":
    main()