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

    def __init__(self, name, age, pay, bonus):
        self.__name = name
        self.__age = age
        self.obj_salary = Salary(pay, bonus)

    def emp_total_salary(self):
        return self.obj_salary.annualSalary()


emp = Employee('max', 33, 84000, 7500)
print(emp.emp_total_salary())




