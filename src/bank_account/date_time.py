class DateError(Exception):
    def __init__(self, msg, val, fn):
        self.__message = msg
        self.__value = val 
        self.__function_name = fn
        
    def get_info(self):
        return "{} value out of range {} - {}".format(self.__message, self.__value, self.__function_name)
        
    def get_value(self):
        return self.__value

class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30,31,30,31,31,30,31,30,31]
    def __init__(self, y, m, d):
        try:
            if y < 0:
                raise DateError("Year", y, 'constructor')
            if m < 1 or m > 12:
                raise DateError("Month", m, 'constructor')
            if d < 1 or d > Date.MONTH_DAYS[m]:
                raise DateError("Day", d, 'constructor')
        except DateError as err:
            print(err.get_info())
        else:
            self.__year = y 
            self.__month = m 
            self.__day = d 
    
    def __str__(self):
        return "{}/{}/{}".format(self.__year, self.__month, self.__day)
        
    #TODO get functions for all data-members
    
    def add_year(self, y):
        self.__year += y
        
    def add_month(self, m):
        x = self.__month + m
        self.__month = ((x-1) % 12) + 1
        self.add_year((x - 1) // 12)

    def add_day(self, d):
        x = self.__day + d

        while x > self.MONTH_DAYS[self.__month]:
            x = x - self.MONTH_DAYS[self.__month]
            self.__month += 1
        self.__day = x
        

    def get_month(self):
        return self.__month
 
    def set_month(self, m):
        try:
            if not self.__check_month_value(m):
                raise DateError("Month", m, 'set month')
        except DateError as err:
            print(err.get_info())
        else:
            self.__month = m

    def __check_month_value(self, m):
        if m < 0 or m > 12:
            return False
        return True
