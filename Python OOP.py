#class
class Person:
    def __init__(self, person_name: str, date_of_birth: int, ht_inches: int = None):
        self.__name = person_name #encapsulation - private member(__)
        self.__date_of_birth = date_of_birth
        self.__height = ht_inches
        self.abc = None

    def get_year_of_birth(self):
     return self.__date_of_birth

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if (self.__has_any_num(new_name)):
            print("Sorry person name can't have number")
            return
            self.__name = new_name

    def __has_any_num(self, string):
        return "0" in string

    def get_summary(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height}"


# a_Person = Person("Ashfat","1998","6 feet")
# print(a_Person.get_summary())
# a_Person.set_name("Abegh")
# print(a_Person.get_summary())
# a_Person.set_name("0Abegh")

Person_list = [Person("Ashfat", 1998, 72), Person("Rashid", 1998, 65), Person("Rafat", 1998, 80),
               Person("Sakib", 1998, 73)]

for Person in Person_list:
    if Person.get_year_of_birth() >= 1990:
        print(Person.get_summary())


