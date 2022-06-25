from datetime import datetime, timedelta


class Person:
    def __init__(self, fn,ln):
        self.first_name = fn
        self.last_name = ln

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Patient(Person):
    def __init__(self, fn, ln):
        super().__init__(fn, ln)
    
    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

class Doctor(Person):
    def __init__(self, fn, ln):
        super().__init__(fn, ln)
        self.schedule = {}

    def is_registered(self, p):
        return p in self.schedule.values()

    def is_free(self, dt):
        dt1 = dt - timedelta(minutes=30)
        dt2 = dt + timedelta(minutes=30)

        for k in self.schedule.keys():
            if dt1 < k < dt2:
                return False
        return True

    def register_patient(self, dt, p):
        if self.is_free(dt) and not self.is_registered(p):
            self.schedule[dt] = p
            # self.schedule.update({dt:p})
            print("Successfully registered!")
            return True
        else:
            print("Patient is already registered or time is not abailable")
            return False


    def __repr__(self):
        return "{}\n{}".format(super().__repr__(), self.schedule)


p = Patient('Gegham', 'Jivanyan')
d = Doctor('John', 'Smith')
print(p)
print(d)
dt = datetime(2022, 6, 5, 12, 0, 0)
d.register_patient(dt, p)
print(d)
dt = datetime(2022, 6, 5, 12, 30, 0)
print(d.is_free(dt))

