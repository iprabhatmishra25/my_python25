
# Step 1 & 2: Create a list of 8 consultants
consultants = [
    {"name": "Prabhat Kumar", "skill": "Python", "days_on_bench": 52},
    {"name": "Siddhi Singh", "skill": "React", "days_on_bench": 38},
    {"name": "Rajesh Rao", "skill": "AWS", "days_on_bench": 22},
    {"name": "Ananya Sen", "skill": "Java", "days_on_bench": 18},
    {"name": "Rahul Mehta", "skill": "Java", "days_on_bench": 8},
    {"name": "Axar Patel", "skill": "Python", "days_on_bench": 5},
    {"name": "Neha Sharma", "skill": "React", "days_on_bench": 12},
    {"name": "Sid Malhotra", "skill": "AWS", "days_on_bench": 3}
]

# Create counter variables to track summary statistics
urgent_count = 0
warning_count = 0
normal_count = 0

print("=== Bench Status Report ===")

# Step 3 & 4: Loop and check statuses
for c in consultants:
    days = c["days_on_bench"]
    
    if days > 30:
        status = "*** URGENT — Place Immediately ***"
        urgent_count = urgent_count + 1  # Step 5: Count urgent consultants
    elif days > 14:
        status = " !! WARNING — Over 2 Weeks !!"
        warning_count = warning_count + 1
    else:
        status = " OK — Bench Duration Normal"
        normal_count = normal_count + 1

    # Print the line using basic formatting spaces to line things up nicely
    print(f"{c['name']:<15} | {c['skill']:<6} | {days:>2} days | {status}")

# Step 6: Print the summary
print("\n=== Summary ===")
print(f"Total Consultants : {len(consultants)}")
print(f"Urgent (>30 days) : {urgent_count}")
print(f"Warning (>14 days): {warning_count}")
print(f"Normal            : {normal_count}\n")

# Step 7 & 8: Sort by days and print again
print("=== Sorted Bench Status Report (Highest Days First) ===")

# This sorts the list using the 'days_on_bench' key from highest to lowest
sorted_consultants = sorted(consultants, key=lambda x: x['days_on_bench'], reverse=True)

for c in sorted_consultants:
    days = c["days_on_bench"]
    
    # Check status again for the sorted display
    if days > 30:
        status = "*** URGENT — Place Immediately ***"
    elif days > 14:
        status = " !! WARNING — Over 2 Weeks !!"
    else:
        status = " OK — Bench Duration Normal"
        
    print(f"{c['name']:<15} | {c['skill']:<6} | {days:>2} days | {status}")