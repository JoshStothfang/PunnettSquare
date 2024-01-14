class Genotype:
    def __init__(self, input):
        self.input = input
        self.alleles = list(input)
        self.couplings = self.generateCouplings(self.alleles)
    
    def generateCouplings(self, alleles):
        couplings = []
        couplingIndices = ["024", "025", "034", "035", "124", "125", "134", "135"]

        for indices in couplingIndices:
            coupling = ""
            for index in indices:
                coupling += alleles[int(index)]
            couplings.append(coupling)
        
        return couplings
    
    def __convertPair(inputPair):
        if inputPair in ["rr", "yy", "ww"]:
            return "0"
        elif inputPair in ["Rr", "Yy", "Ww", "rR", "yY", "wW"]:
            return "1"
        elif inputPair in ["RR", "YY", "WW"]:
            return "2"

    @classmethod
    def convertToNumeric(self, genotype):
        return self.__convertPair(genotype[0:2]) + " - " + self.__convertPair(genotype[2:4]) + " - " + self.__convertPair(genotype[4:])
