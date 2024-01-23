from copy import deepcopy

class Genotype:
    def __init__(self, genotype):
        self.genotype = genotype
        self.alleles = list(genotype)
        self.alleleCombos = self.generateAlleleCombos(self.alleles)
    
    def generateAlleleCombos(self, alleles):
        countdown = len(alleles) - 1
        alleleCombos = [[alleles[countdown]]]
        countdown -= 1
        alleleCombos.insert(0, [alleles[countdown]])
        countdown -= 1

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
