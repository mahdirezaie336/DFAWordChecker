class Machine:
    """ This class is a DFA machine in which we can define a regular language.
        By this machine we can check if a letter is acceptable and exists in
        a language or no.

        Author: Mahdi Rezaie
        Email: mahdi.rezaie.336@gmail.com
        Student ID: 9728040
        """

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
        """ Checks the acceptability of a word in this machine. """
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

    def __str__(self):
        return str(self.transitions)


if __name__ == '__main__':

    # Getting first machine from input
    print('*******************')
    print('First Machine:')
    alphabet1 = input('    Enter alphabet letters for the first machine: ').split()
    states1 = input('    Not enter name of all states for the first machine: ').split()
    init_state1 = input('    Not enter name of initial state for the first machine: ')
    final_states1 = input('    Not enter name of all final states for the first machine: ').split()
    print('    Now enter rows of the machine table:')
    print('_______________________________________________')
    print('   ', ' '.join(alphabet1))
    transitions1 = []
    for state in states1:
        next_states = input(state + ' ').split()
        for i, letter in enumerate(alphabet1):
            transitions1.append((state, letter, next_states[i]))
    machine1 = Machine(set(states1), init_state1, set(final_states1), set(alphabet1), *transitions1)

    # Getting second machine from input
    print('*******************')
    print('Second Machine:')
    alphabet2 = input('    Enter alphabet letters for the second machine: ').split()
    states2 = input('    Not enter name of all states for the second machine: ').split()
    init_state2 = input('    Not enter name of initial state for the second machine: ')
    final_states2 = input('    Not enter name of all final states for the second machine: ').split()
    print('    Now enter rows of the machine table:')
    print('_______________________________________________')
    print('   ', ' '.join(alphabet2))
    transitions2 = []
    for state in states2:
        next_states = input(state + ' ').split()
        for i, letter in enumerate(alphabet2):
            transitions2.append((state, letter, next_states[i]))
    machine2 = Machine(set(states2), init_state2, set(final_states2), set(alphabet2), *transitions2)

    # The loop of getting inputs
    while True:
        word = input('Enter a word to check: ')
        print()
        print(word, 'in machine1:', word in machine1)
        print(word, 'in machine2:', word in machine2)
        print(word, 'in both machines:', word in machine1 and word in machine2)
        print()
