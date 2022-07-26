class State(object):
    def __init__(self, rotulo, regras, dot_idx, comeco_indice, final_indice, idx, receptor, produtor):
        self.rotulo = rotulo
        self.regras = regras
        self.dot_idx = dot_idx
        self.comeco_indice = comeco_indice
        self.final_indice = final_indice
        self.index = idx
        self.receptor = receptor
        self.produtor = produtor

    def next(self):
        """Returns the tag after the dot"""
        return self.regras[self.dot_idx]

    def complete(self):
        """Verifica se o ponto esta na regra atual, se sim, esta completo"""
        return len(self.regras) == self.dot_idx

    def __eq__(self, other):
        return (self.rotulo == other.rotulo and
                self.regras == other.regras and
                self.dot_idx == other.dot_idx and
                self.comeco_indice == other.comeco_indice and
                self.final_indice == other.final_indice)

    def __str__(self):
        regra_s = ''
        for i, rule in enumerate(self.regras):
            if i == self.dot_idx:
                regra_s += '.'
            regra_s += rule + ' '
        if self.dot_idx == len(self.regras):
            regra_s += '.'

        index = self.index
        rotulo = self.rotulo
        regra_s = regra_s
        comeco_indice = self.comeco_indice
        final_indice = self.final_indice
        receptor = self.receptor
        produtor = self.produtor

        return '%s -> %s' % (rotulo, regra_s)
