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
    
    def __convertPair(inputPair, letter = "X"):
        if inputPair in ["rr", "yy", "ww"]:
            return "0"
        elif inputPair in ["Rr", "Yy", "Ww", "rR", "yY", "wW"]:
            return "1"
        elif inputPair in ["RR", "YY", "WW"]:
            return "2"
        elif inputPair == "0":
            return letter.lower() + letter.lower()
        elif inputPair == "1":
            return letter.upper() + letter.lower()
        elif inputPair == "2":
            return letter.upper() + letter.upper()
        else:
            return -1

    @classmethod
    def convertToNumeric(self, genotype):
        return self.__convertPair(genotype[0:2]) + " - " + self.__convertPair(genotype[2:4]) + " - " + self.__convertPair(genotype[4:])
    
    @classmethod
    def convertToGenotype(self, numeric):
        return self.__convertPair(numeric[0:1], "R") + self.__convertPair(numeric[4:5], "Y") + self.__convertPair(numeric[8:], "W")
