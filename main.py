class NDFA:

    def __init__(self, all_states: list['str'],
                 init_state: str,
                 final_states: set['str'],
                 alphabet: list['str'],
                 *transitions):

        self.all_states = all_states
        self.init_state = init_state
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
        current_state = self.init_state
        for letter in item:
            try:
                current_state = self.transitions[current_state][letter]
            except KeyError:
                return False
        return current_state in self.final_states
