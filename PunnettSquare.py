import sys
from Genotype import Genotype

parent1 = Genotype("RrYyWw")
parent2 = Genotype("RRYYWW")

children = []

def breed(coupling1, coupling2):
    child = ""
    for i in range(3):
        child += coupling1[i]
        child += coupling2[i]
    return child

for coupling1 in parent1.couplings:
    for coupling2 in parent2.couplings:
        children.append(breed(coupling1, coupling2))

numericChildren = []

for child in children:
    numericChildren.append(Genotype.convertToNumeric(child))
    