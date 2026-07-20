# create_bench_data.py

# Sample data with 8 bench employees
records = [
    'EmpID,Name,Skills,BenchDays,LastProject\n',
    'E101,Rahul Sharma,"Python, SQL, Django",45,Project Orion\n',
    'E102,Priya Nair,"Java, Spring Boot",20,Project Falcon\n',
    'E103,Amit Verma,"React, Node.js, JavaScript",35,Project Titan\n',
    'E104,Sneha Patel,"Python, AWS, Docker",15,Project Apex\n',
    'E105,Vikram Singh,"C++, Linux, Shell",60,Project Legacy\n',
    'E106,Ananya Roy,"Data Science, R, Machine Learning",50,Project Insight\n',
    'E107,Karan Gupta,"Flutter, Android, Kotlin",10,Project Mobile\n',
    'E108,Meera Joshi,"SQL, PowerBI, Tableau",40,Project Analytics\n'
]

# Write records to bench_employees.csv using 'w' mode
with open("bench_employees.csv", "w", encoding="utf-8") as file:
    file.writelines(records)

print("'bench_employees.csv' created successfully with 8 sample records.")

# view_bench_data.py
import csv

try:
    with open("bench_employees.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        
        # Skip header line
        header = next(reader, None)
        
        print("\n=== BENCH EMPLOYEE RECORDS ===")
        for row in reader:
            if row:  # Ensure the row is not empty
                emp_id, name, skills, bench_days, last_project = row
                print(f"EmpID: {emp_id} | Name: {name} | Skills: {skills} | Bench Days: {bench_days}")
                
except FileNotFoundError:
    print(" Error: 'bench_employees.csv' file was not found. Please run create_bench_data.py first.")
except Exception as e:
    print(f" An error occurred: {e}")

    # add_bench_employee.py

def add_employee():
    print("=== Add New Bench Employee ===")
    emp_id = input("Enter EmpID (e.g., E109): ").strip()
    name = input("Enter Name: ").strip()
    skills = input("Enter Skills (comma-separated, e.g., Python, SQL): ").strip()
    bench_days = input("Enter Bench Days: ").strip()
    last_project = input("Enter Last Project Name: ").strip()

    # Format line for CSV (skills quoted to safely store inner commas)
    new_record = f'{emp_id},{name},"{skills}",{bench_days},{last_project}\n'

    with open("bench_employees.csv", "a", encoding="utf-8") as file:
        file.write(new_record)

    print(f"\n✅ Employee '{name}' added successfully to bench_employees.csv!")

if __name__ == "__main__":
    add_employee()

    # long_bench_report.py
import csv

try:
    long_bench_employees = []

    with open("bench_employees.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header

        for row in reader:
            if row:
                emp_id, name, skills, bench_days, last_project = row
                # Check business condition: BenchDays > 30
                if int(bench_days) > 30:
                    long_bench_employees.append(f"{name} - {bench_days} days on bench\n")

    # Write results to long_bench_alert.txt
    with open("long_bench_alert.txt", "w", encoding="utf-8") as file:
        file.writelines(long_bench_employees)

    print("✅ Report generated! Check 'long_bench_alert.txt' for results.")
    
    # Optional: Display output in console
    print("\n--- Long Bench Alert Content ---")
    for line in long_bench_employees:
        print(line.strip())

except FileNotFoundError:
    print(" Error: 'bench_employees.csv' file missing.")
except Exception as e:
    print(f" An error occurred: {e}")