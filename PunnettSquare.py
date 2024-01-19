import sys
from Genotype import Genotype
from collections import Counter

def main():
    parent1 = Genotype(sys.argv[1])
    parent2 = ""
    
    if len(sys.argv) == 2:
        parent2 = parent1
    else:
        parent2 = Genotype(sys.argv[2])

    children = []

    for combo1 in parent1.alleleCombos:
        for combo2 in parent2.alleleCombos:
            children.append(breed(combo1, combo2))

    numericChildren = []

    for child in children:
        numericChildren.append(Genotype.convertToNumeric(child))

    outputTuples = []

    for numericChild in list(Counter(numericChildren)):
        genotypeChild = Genotype.convertToGenotype(numericChild)
        percentage = (Counter(numericChildren).get(numericChild))/64
        outputTuples.append((percentage, genotypeChild, numericChild))

    outputTuples.sort(reverse=True)

    for percent, geno, _ in outputTuples:
        print(str(percent * 100) + "%", geno, sep="\t")

def breed(combo1, combo2):
    child = ""
    for i in range(3):
        child += combo1[i]
        child += combo2[i]
    return child

if __name__ == "__main__":
    main()