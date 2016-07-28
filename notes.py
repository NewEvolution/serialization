import pickle

class Notes:

    def __init__(self):
        self.notes = []
        try:
            self.notes =self.deserialize()
        except FileNotFoundError:
            pass

    def prompt(self):
        note = input('Enter a note or command\n> ')
        if note == 'ls':
            [print(str(key) + ' • ' + note) for key, note in enumerate(self.notes)]

        elif note == 'quit':
            exit()

        elif note == 'rm':
            [print(str(key) + ' • ' + note) for key, note in enumerate(self.notes)]
            print('')
            del self.notes[int(input('Remove which note?\n> '))]

        else:
            self.notes.append(note)
            self.serialize()

        print('')
        self.prompt()

    def serialize(self):
        with open('notes.txt', 'wb+') as f:
            pickle.dump(self.notes, f)


    def deserialize(self):
        try:
            with open('notes.txt', 'rb+') as f:
                self.notes = pickle.load(f)

            return self.notes

        except FileNotFoundError:
            self.notes = []
