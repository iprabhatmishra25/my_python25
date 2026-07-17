# Step 1: Get the initial list of consultants

def get_consultants():
    """Returns the list of 8 consultant dictionaries."""
    list_of_consultants = [
        {"name": "Prabhat Kumar", "skill": "Python", "days_on_bench": 52},
        {"name": "Siddhi Singh", "skill": "React", "days_on_bench": 38},
        {"name": "Rajesh Rao", "skill": "AWS", "days_on_bench": 22},
        {"name": "Ananya Sen", "skill": "Java", "days_on_bench": 18},
        {"name": "Rahul Mehta", "skill": "Java", "days_on_bench": 8},
        {"name": "Amit Patel", "skill": "Python", "days_on_bench": 5},
        {"name": "Neha Sharma", "skill": "React", "days_on_bench": 12},
        {"name": "Vikram Malhotra", "skill": "AWS", "days_on_bench": 3}
    ]
    return list_of_consultants

# Step 2: Determine status and category
# ==========================================
def get_status(days):
    """Takes bench days and returns a tuple: (status_text, category)"""
    if days > 30:
        return "URGENT", "urgent"
    elif days > 14:
        return "WARNING", "warning"
    else:
        return "NORMAL", "normal"

# Step 3: Sort and print the formatted report
def print_report(consultants_list):
    """Sorts the consultants by days and prints them in a nice table."""
    print("=== Bench Status Report ===")
    
    # Sort the list from highest days to lowest days
    sorted_list = sorted(consultants_list, key=lambda x: x['days_on_bench'], reverse=True)
    
    # Loop through the sorted list and print each row
    for c in sorted_list:
        # Call get_status internally to get the text label
        status_text, category = get_status(c['days_on_bench'])
        
        print(f"{c['name']:<15} | {c['skill']:<6} | {c['days_on_bench']:>2} days | {status_text}")
    print()  # Empty line for spacing

# Step 4: Filter the list by a specific skill
def filter_by_skill(consultants_list, skill_to_find):
    """Returns a new list containing only consultants with the matching skill."""
    matching_consultants = []
    
    for c in consultants_list:
        # lower() makes sure it matches even if capitalization is different
        if c['skill'].lower() == skill_to_find.lower():
            matching_consultants.append(c)
            
    return matching_consultants

# Step 5: Calculate the average bench days
def average_bench_days(consultants_list):
    """Returns the average bench days rounded to 1 decimal place."""
    if len(consultants_list) == 0:
        return 0.0
        
    total_days = 0
    for c in consultants_list:
        total_days = total_days + c['days_on_bench']
        
    avg = total_days / len(consultants_list)
    return round(avg, 1)

# Step 6 & 7: Main execution block
if __name__ == '__main__':
    # 1. Load the data
    all_consultants = get_consultants()
    
    # 2. Print the main sorted report
    print_report(all_consultants)
    
    # 3. Filter by Python and print the results
    print("=== Filter by Skill: Python ===")
    python_team = filter_by_skill(all_consultants, "Python")
    for c in python_team:
        print(f"{c['name']:<12} — {c['days_on_bench']} days on bench")
    print()
    
    # 4. Calculate and print the overall average
    avg_days = average_bench_days(all_consultants)
    print(f"Average bench days across all consultants: {avg_days} days\n")
    
    # 5. Filter by a missing skill (Kotlin) and handle the edge case
    print("=== Filter by Skill: Kotlin ===")
    kotlin_team = filter_by_skill(all_consultants, "Kotlin")
    
    # Step 7 logic: check if the filtered list came back empty
    if len(kotlin_team) == 0:
        print("No consultants found with skill: Kotlin")
    else:
        for c in kotlin_team:
            print(f"{c['name']:<12} — {c['days_on_bench']} days on bench")