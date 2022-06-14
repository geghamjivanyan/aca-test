class UnknownAtomError(Exception):
    def __init__(self, value):
        self.__value = value

    def get_info(self):
        return "Invalid atom name - {}\n".format(self.__value)


class Atom:
    
    ATOMS = {'O': 'Oxygen', 'H': 'Hydrogen', 'N': 'Nytrogen', 'P': 'Phosphorius', 'C': 'Carbon'}

    def __init__(self, name):
        try:
            if name not in self.ATOMS:
                raise UnknownAtomError(name)
        except UnknownAtomError as err:
            print(err.get_info())
        else:
            self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        if x in self.ATOMS:
            self.__name = x
        else:
            print("Object not changed")

    def __repr__(self):
        try:
            return self.ATOMS[self.__name]
        except AttributeError:
            return "Object does not created"

    def __add__(self, other):
        return Molecul([self, other])


class Molecul:

    def __init__(self, a):
        self.__atoms = a
        
    @property
    def atoms(self):
        return self.__atoms
    
    @atoms.setter
    def atoms(self, a):
        self.__atoms = a
        
    def __add__(self, other):
        if isinstance(other, Atom):
            self.__atoms.append(other)
        else:
            self.__atoms.extend(other.atoms)
        return Molecul(self.__atoms)

    def __repr__(self):
        s = ''
        for i in self.__atoms:
            s += i.name + '-'
        return s[:-1]

a1 = Atom('H')
a2 = Atom('O')
a3 = Atom('C')
a4 = Atom('N')
a5 = Atom('P')

m = Molecul([a1, a3, a1, a2, a4, a1, a2, a5])
m1 = a1 + a4 
print(a1 + a2 + a3)

