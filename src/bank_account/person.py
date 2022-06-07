class Person:

    def __init__(self, fn, ln, a, g):
        self.first_name = fn
        self.last_name = ln
        self.age = a
        self.gender = g


    def __str__(self):
        # print("Person")
        return "{} {} - {}, {}".format(self.first_name, self.last_name, self.age, self.gender)
