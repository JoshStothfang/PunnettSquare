class Genotype:
    def __init__(self, genotype):
        self.genotype = genotype
        self.alleles = list(genotype)
        self.alleleCombos = self.generateAlleleCombos(self.alleles)
    
    def generateAlleleCombos(self, alleles):
        alleleCombos = []
        alleleComboIndices = ["024", "025", "034", "035", "124", "125", "134", "135"]

        for indices in alleleComboIndices:
            alleleCombo = ""
            for index in indices:
                alleleCombo += alleles[int(index)]
            alleleCombos.append(alleleCombo)
        
        return alleleCombos