class NDFA:

    def __init__(self, all_states: set['str'],
                 init_state: str,
                 final_states: set['str'],
                 alphabet: set['str'],
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
        if type(item) != str:
            raise TypeError('Type must be "str"')
        current_state = self.init_state
        for letter in item:
            try:
                current_state = self.transitions[current_state][letter]
            except KeyError:
                return False
        return current_state in self.final_states


def main():
    all_states = {'S00', 'S01', 'S02'}
    alphabet = {'a', 'b', 'c'}
    init_state = 'S00'
    final_states = {'S02'}
    transitions = [('S00', 'a', 'S00'), ('S00', 'b', 'S01'), ('S01', 'a', 'S01'), ('S01', 'b', 'S02'),
                   ('S02', 'a', 'S02'), ('S02', 'b', 'S02')]
    #   _______        _______        _______
    #   | S00 | --b--> | S01 | --b--> | S02 |
    #   -------        -------        -------
    machine = NDFA(all_states, init_state, final_states, alphabet, *transitions)

    print('aaaabbaaaa' in machine)
    print('abaaaaaa' in machine)


if __name__ == '__main__':
    main()
