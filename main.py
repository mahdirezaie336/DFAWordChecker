class NDFA:

    def __init__(self, all_states: list['str'],
                 init_state: str,
                 final_states: list['str'],
                 alphabet: list['str'],
                 *transitions):

        self.all_states = all_states
        self.final_states = final_states
        self.alphabet = alphabet
        self.transitions = {}
        for item in transitions:
            if item[0] not in self.transitions:
                self.transitions[item[0]] = {}
            self.transitions[item[0]][item[1]] = item[2]

    def __contains__(self, item):
        if type(item) != 'str':
            raise TypeError('Type must be "str"')
