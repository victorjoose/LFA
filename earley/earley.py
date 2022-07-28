from state import State


class Earley:
    def __init__(self, palavras, gramatica, terminais, variavel_inicial):
        self.chart = [[] for _ in range(len(palavras) + 1)]
        self.current_id = 0
        self.palavras = palavras
        self.gramatica = gramatica
        self.terminais = terminais
        self.variavel_inicial = variavel_inicial

    def novo_id(self):
        self.current_id += 1
        return self.current_id - 1

    def eh_terminal(self, tag):
        return tag in self.terminais

    def enqueue(self, state, chart_entry):
        if state not in self.chart[chart_entry]:
            self.chart[chart_entry].append(state)
        else:
            self.current_id -= 1

    def predictor(self, state):
        for production in self.gramatica[state.next()]:
            self.enqueue(
                State(state.next(), production, 0, state.final_indice, state.final_indice, self.novo_id()), state.final_indice)

    def scanner(self, state):
        if self.palavras[state.final_indice] in self.gramatica[state.next()]:
            self.enqueue(
                State(state.next(), [self.palavras[state.final_indice]], 1, state.final_indice, state.final_indice + 1, self.novo_id()), state.final_indice + 1)

    def completer(self, state):
        for s in self.chart[state.comeco_indice]:
            if not s.complete() and s.next() == state.rotulo and s.final_indice == state.comeco_indice and s.rotulo != 'Início':
                self.enqueue(State(s.rotulo, s.regras, s.dot_idx + 1, s.comeco_indice, state.final_indice, self.novo_id()), state.final_indice)

    def parse(self):
        self.enqueue(State('Início', [self.variavel_inicial], 0, 0, 0, self.novo_id()), 0)

        for i in range(len(self.palavras) + 1):
            for state in self.chart[i]:
                if not state.complete() and not self.eh_terminal(state.next()):
                    self.predictor(state)
                elif i != len(self.palavras) and not state.complete() and self.eh_terminal(state.next()):
                    self.scanner(state)
                else:
                    self.completer(state)

    def __str__(self):
        res = ''
        for i, chart in enumerate(self.chart):
            res += '\nD%d\n' % i
            for state in chart:
                res += str(state) + '\n'
        return res
