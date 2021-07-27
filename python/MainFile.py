class Decide:
    
    def __init__(self, choice, path):
        self.choice = choice
        self.path = path

    def choose(self):
        if self.choice == 1:
            return self.runbysize(self.path)
        elif choice == 2:
            return self.runbyextension(self.path)
        elif choice == 3:
            return self.runbydate(self.path)

    def runbysize(self, path):
        a = sizecheck(self.path)
        return a

    def runbyextension(self, path):
        a = sort_exten(self.path)
        return a

    def runbydate(self, path):
        a = bydate(self.path)

        return a
