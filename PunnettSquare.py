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

    newChildren = []

    for child in children:
        childList = list(child)
        counter = 0
        while counter < len(child):
            if ord(child[counter]) > ord(child[counter + 1]):
                char1 = child[counter]
                char2 = child[counter + 1]
                childList[counter + 1] = char1
                childList[counter] = char2
            counter += 2
        newChildren.append("".join(childList))
    
    outputTuples = []

    for child in Counter(newChildren):
        outputTuples.append((Counter(newChildren).get(child) / len(children), child))

    outputTuples.sort(reverse=True)

    for percent, genotype in outputTuples:
        print(str(percent * 100) + "%", genotype, sep="\t")

def breed(combo1, combo2):
    child = ""
    for i in range(len(combo1)):
        child += combo1[i]
        child += combo2[i]
    return child

if __name__ == "__main__":
    main()