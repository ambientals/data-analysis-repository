"""Code created to test a class and test it with assigned examples. This code has educational purposes; no copyright infringement is intended."""

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
#        self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_1.fullname()  # doesnt need to pass "self", it does automatically
print(emp_1.fullname())
print(emp_1.fullname)
Employee.fullname(emp_1)  #doesnt know which instance to run the method with, so it needs an instance explicitly passed in
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)

# emp_2.fullname()
# print(emp_2.fullname())
# print(emp_2.fullname)
# Employee.fullname(emp_2)
# print(Employee.fullname(emp_2))

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)