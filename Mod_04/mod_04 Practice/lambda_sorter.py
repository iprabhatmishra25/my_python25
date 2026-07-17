# 1. Initialize the 6 employee dictionaries
employees = [
    {"name": "Prabhat", "dept": "Engineering", "salary": 95000},
    {"name": "Akash", "dept": "Sales", "salary": 70000},
    {"name": "Roshan", "dept": "Engineering", "salary": 110000},
    {"name": "Aditya", "dept": "HR", "salary": 65000},
    {"name": "Lamin", "dept": "Sales", "salary": 85000},
    {"name": "Messi", "dept": "HR", "salary": 80000}
]

def print_employees(employee_list):
    """Helper function to print list of employees cleanly."""
    for emp in employee_list:
        print(f"  Name: {emp['name']:<8} | Dept: {emp['dept']:<12} | Salary: ${emp['salary']:,}")
    print()

# (a) Sorted Alphabetically by Name
print("--- (a) Sorted Alphabetically by Name ---")
by_name = sorted(employees, key=lambda x: x["name"])
print_employees(by_name)

# (b) Sorted by Salary Descending
print("--- (b) Sorted by Salary Descending ---")
by_salary_desc = sorted(employees, key=lambda x: x["salary"], reverse=True)
print_employees(by_salary_desc)

# (c) Sorted by Department First, then Salary Descending
print("--- (c) Sorted by Department (A-Z), then Salary Descending ---")
# To sort salary in descending order while department is in ascending order 
# within a single tuple key, we can negate the numerical salary value (-x["salary"]).
by_dept_salary_desc = sorted(
    employees, 
    key=lambda x: (x["dept"], -x["salary"])
)
print_employees(by_dept_salary_desc)