class Entrada:
    def __init__(self, palavras, gramatica, terminais):
        self.palavras = palavras
        self.gramatica = self.Gramatica()
        self.terminais = terminais

    class Gramatica:
        def __init__(self, regra_de_producao):
            self.regra_de_producao = self.Regra_de_producao()

        class Regra_de_producao:
            def __init__(self, variavel_inical, variaveis, variavel_nao_terminal):
                self.variavel_inical = variavel_inical
                self.variavel_terminal = variaveis
                self.variavel_nao_terminal = variavel_nao_terminal
