# CREATE A CLASS

class Employee:
    def __init__(self, name , base_salary):
        self.name = name
        self.base_salary = base_salary

    def monthly_pay(self):
        return self.base_salary

# CREATE A SUBCLASS

class SalesEmployee(Employee):
    def __init__(self, name, base_salary, commission):
        super().__init__(name, base_salary)
        self.commission = commission

    def monthly_pay(self):
        return super().monthly_pay() + self.commission

emp = Employee("prabhat" , 19820)
sales_emp = SalesEmployee("OM" , 9000, 15000)

print(f"{emp.name}'s Monthly Pay: ${emp.monthly_pay():,.2f}")
print(f"{sales_emp.name}'s Monthly Pay: ${sales_emp.monthly_pay():,.2f}")