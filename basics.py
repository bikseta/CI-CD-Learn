class Person():
    def __init__(self, name, age, sex, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address

    def vote(self):
        print(f'Hi {self.name}, your sex is {self.sex} and you live in {self.address}')

        if int(self.age) < 18:
            print(f'You are not illegible to vote {self.name}')
        else:
            print(f'You are eligible to vote {self.name}, because your age is {self.age}')

person1 = Person('Bikila', '37', 'Male', 'Stockholm')
person2 = Person('Yero','17', 'Female', 'Addis Ababa')
person3 = Person('Shure', '28', 'Male', 'Uppsala')
person4 = Person('Hawwi', '28', 'Female', 'Spanga')

person1.vote()
print('-------------------------------------------------')
person2.vote()
print('-------------------------------------------------')
person3.vote()
print('-------------------------------------------------')
person4.vote()

