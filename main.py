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
            if current_state not in self.all_states:
                raise ValueError('State ' + current_state + ' is not valid')
        return current_state in self.final_states


def main():
    machine1_all_states = {'S00', 'S01', 'S02'}
    machine1_alphabet = {'a', 'b'}
    machine1_init_state = 'S00'
    machine1_final_states = {'S02'}
    machine1_transitions = [('S00', 'a', 'S00'), ('S00', 'b', 'S01'),
                            ('S01', 'a', 'S01'), ('S01', 'b', 'S02'),
                            ('S02', 'a', 'S02'), ('S02', 'b', 'S00')]
    #    v----------------b---------------
    #   _______        _______        _______
    #   | S00 | --b--> | S01 | --b--> |[S02]|
    #   -------        -------        -------
    #    ^-a--          ^-a--          ^-a--
    # Accepts a word with at least two n(b) % 3 == 2
    machine1 = NDFA(machine1_all_states, machine1_init_state, machine1_final_states,
                    machine1_alphabet, *machine1_transitions)

    print('aaaabaabaa in machine 1:', 'aaaabaabaa' in machine1)
    print('abaaaaa in machine 1:', 'abaaaaa' in machine1)

    machine2_all_states = {'S00', 'S01'}
    machine2_alphabet = {'a', 'b'}
    machine2_init_state = 'S00'
    machine2_final_states = {'S01'}
    machine2_transitions = [('S00', 'a', 'S01'), ('S00', 'b', 'S00'),
                            ('S01', 'a', 'S00'), ('S01', 'b', 'S01')]
    #    v-b--          v-b--
    #   _______        _______
    #   | S00 | --a--> |[S01]|
    #   -------        -------
    #    ^--------a---------
    # Accepts a word with at least one 'a'
    machine2 = NDFA(machine2_all_states, machine2_init_state, machine2_final_states,
                    machine2_alphabet, *machine2_transitions)

    print('aaaababaa in machine 2:', 'aaaababaa' in machine2)
    print('abbbaba in machine 2:', 'abbbaba' in machine2)

    # Testing two machines
    s = 'aaaababaa'
    print('aaaababaa in machine 1 and 2:', s in machine2 and s in machine1)


if __name__ == '__main__':
    main()
