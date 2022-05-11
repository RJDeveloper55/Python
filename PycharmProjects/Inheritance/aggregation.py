class Salary:
    __pay = None
    __bonus = None

    def __init__(self, pay, bonus):
        self.__pay = pay
        self.__bonus = bonus

    def annualSalary(self):
        return (self.__pay*12) + self.__bonus


class Employee:
    __age = None
    __name = None

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
       # self.obj_salary = Salary(pay, bonus)
        self.obj_salary = salary

    def emp_total_salary(self):
        return self.obj_salary.annualSalary()


salary = Salary(84000, 7500)
emp = Employee('max', 33, salary)
print(emp.emp_total_salary())




