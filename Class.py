# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: May 5, 2024
# ************************************************************************


# create a class named person
class Person:
    # define here your init() constructor (optional)

    school_graduated_from = "Jose Rizal University"  # class variable

    def __init__(self, name, sex, profession):
        # instance variable, define the attributes/ properties/ states
        # data members
        self.name = name
        self.sex = sex
        self.profession = profession

    #  define here the instance method/ behavior
    def show(self):
        x = " | "
        print("Name: ", self.name, x, "Sex: ", self.sex, x, "Profession: ", self.profession)


# Instantiate / Create an object from class Person
p1 = Person("Jose Rizal","Male", "Doctor")
print(p1)
p1.show()  # This is a method call/ invocation

p2 = Person("Sophia", "Female", "Student")
p2.show()
