from copy import deepcopy

class Genotype:
    def __init__(self, genotype):
        self.genotype = genotype
        self.alleleCombos = self.alleleCombosFactory(list(genotype))
    
    # Generates allele combos for axis of punnett square.
    def alleleCombosFactory(self, alleles):
        # Creates alleleCombos array containing 2 arrays. One containing the last allele in genotype. The other containing the second-to-last allele in genotype.
        countdown = len(alleles) - 1
        alleleCombos = [[alleles[countdown]]]
        countdown -= 1
        alleleCombos.insert(0, [alleles[countdown]])
        countdown -= 1

        # Duplicates alleleCombos array on itself and alternates between the previous two alleles adding them to the beginning of the child arrays.
        while countdown > 0:

            newAlleleCombos = deepcopy(alleleCombos) + deepcopy(alleleCombos)
            alleleCombos = deepcopy(newAlleleCombos)
            
            for i in range(len(alleleCombos)):
                if i < (len(alleleCombos) / 2):
                    alleleCombos[i].insert(0, alleles[countdown - 1])
                else:
                    alleleCombos[i].insert(0, alleles[countdown])
            
            countdown -= 2
        
        return alleleCombos
