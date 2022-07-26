from state import State


class Earley:
    def __init__(self, words, grammar, terminals):
        self.chart = [[] for _ in range(len(words) + 1)]
        self.current_id = 0
        self.words = words
        self.grammar = grammar
        self.terminals = terminals

    def get_new_id(self):
        self.current_id += 1
        return self.current_id - 1

    def eh_terminal(self, tag):
        return tag in self.terminals

    def is_complete(self, state):
        return len(state.regras) == state.dot_idx

    def enqueue(self, state, chart_entry):
        if state not in self.chart[chart_entry]:
            self.chart[chart_entry].append(state)
        else:
            self.current_id -= 1

    def predictor(self, state):
        for production in self.grammar[state.next()]:
            self.enqueue(
                State(state.next(), production, 0, state.final_indice, state.final_indice, self.get_new_id(), [], 'predictor'), state.final_indice)

    def scanner(self, state):
        if self.words[state.final_indice] in self.grammar[state.next()]:
            self.enqueue(
                State(state.next(), [self.words[state.final_indice]], 1, state.final_indice, state.final_indice + 1, self.get_new_id(),
                      [], 'scanner'), state.final_indice + 1)

    def completer(self, state):
        for s in self.chart[state.comeco_indice]:
            if not s.complete() and s.next() == state.rotulo and s.final_indice == state.comeco_indice and s.rotulo != 'gamma':
                self.enqueue(State(s.rotulo, s.regras, s.dot_idx + 1, s.comeco_indice, state.final_indice, self.get_new_id(),
                                   s.receptor + [state.index], 'completer'), state.final_indice)

    def parse(self):
        self.enqueue(State('gamma', ['S'], 0, 0, 0, self.get_new_id(), [], 'dummy start state'), 0)

        for i in range(len(self.words) + 1):
            for state in self.chart[i]:
                if not state.complete() and not self.eh_terminal(state.next()):
                    self.predictor(state)
                elif i != len(self.words) and not state.complete() and self.eh_terminal(state.next()):
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
