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
