# create a class

class Employee:
    def __init__(self, name , base_salary):
        self.name = name
        self.base_salary = base_salary

    def monthly_pay(self):
        return self.base_salary

class SalesEmployee(Employee):
    def __init__(self, name, base_salary,commission):
        super().__init__(name, base_salary)
        self.commission = commission

    def monthly_pay(self):
        return super().monthly_pay() + self.commission

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self , emp: Employee):
        self.employees.append(emp)

    def total_payroll(self):
        return sum(emp.monthly_pay() for emp in self.employees)

Engineering = Department("COMPUTER SCIENCE")

emp1 = Employee("prabhat" , 189022)
emp2 = Employee("om" , 20989)

Engineering.add_employee(emp1)
Engineering.add_employee(emp2)

print(f"Department : {Engineering.name}")
print(f"Total monthly_payroll : ${Engineering.total_payroll():.2f}")
