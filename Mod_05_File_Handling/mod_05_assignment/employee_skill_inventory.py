# -------------------------------------------------------------------
# Step 1 & 2: Create Employee Skill Inventory Dictionary
# -------------------------------------------------------------------
employees = {
    "Alice": {
        "skills": ["Python", "AWS", "Docker", "SQL"],
        "experience": 5,
        "location": "New York"
    },
    "Bob": {
        "skills": ["Python", "Django", "SQL"],
        "experience": 3,
        "location": "Chicago"
    },
    "Charlie": {
        "skills": ["AWS", "Kubernetes", "Linux"],
        "experience": 4,
        "location": "San Francisco"
    },
    "Diana": {
        "skills": ["Python", "AWS", "React", "GraphQL"],
        "experience": 6,
        "location": "Austin"
    },
    "Evan": {
        "skills": ["Java", "Spring Boot", "SQL"],
        "experience": 2,
        "location": "Remote"
    },
    "Fiona": {
        "skills": ["JavaScript", "React", "Node.js"],
        "experience": 3,
        "location": "Seattle"
    }
}


# -------------------------------------------------------------------
# Step 3: Find Employees by a Single Skill
# -------------------------------------------------------------------
def find_by_skill(employees_dict, skill):
    """Returns a list of employee names who possess the given skill."""
    return [
        name for name, details in employees_dict.items()
        if skill.lower() in [s.lower() for s in details['skills']]
    ]


# -------------------------------------------------------------------
# Step 4: Find Employees Matching Multiple Skills
# -------------------------------------------------------------------
def find_multi_skill(employees_dict, skills):
    """Returns a list of employee names who possess ALL specified skills."""
    target_skills = [s.lower() for s in skills]
    return [
        name for name, details in employees_dict.items()
        if all(ts in [s.lower() for s in details['skills']] for ts in target_skills)
    ]


# -------------------------------------------------------------------
# Step 5: Compute Skill Gap using Set Operations
# -------------------------------------------------------------------
def skill_gap(required_skills, employee_skills):
    """Returns skills present in required_skills but missing in employee_skills."""
    return list(set(required_skills) - set(employee_skills))


# -------------------------------------------------------------------
# Step 6: Print Employee Inventory
# -------------------------------------------------------------------
def print_inventory(employees_dict):
    """Prints each employee's details in a clean, readable format."""
    print("\n" + "=" * 50)
    print("           EMPLOYEE SKILL INVENTORY           ")
    print("=" * 50)
    for name, details in employees_dict.items():
        skills_str = ", ".join(details['skills'])
        print(f"• Name:       {name}")
        print(f"  Location:   {details['location']}")
        print(f"  Experience: {details['experience']} years")
        print(f"  Skills:     {skills_str}")
        print("-" * 50)


# -------------------------------------------------------------------
# Step 7: Testing Functions & Displaying Results
# -------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Print full inventory
    print_inventory(employees)

    # 2. Test find_by_skill
    search_skill = "Python"
    python_devs = find_by_skill(employees, search_skill)
    print(f"\n Employees with skill '{search_skill}':")
    print(f"   {python_devs}")

    # 3. Test find_multi_skill
    required_multi = ["Python", "AWS"]
    multi_match = find_multi_skill(employees, required_multi)
    print(f"\n Employees with ALL skills {required_multi}:")
    print(f"   {multi_match}")

    # 4. Test skill_gap
    project_requirements = ["Python", "AWS", "Docker", "Kubernetes", "Terraform"]
    bob_skills = employees["Bob"]["skills"]
    gap = skill_gap(project_requirements, bob_skills)
    
    print(f"\n Skill Gap Analysis for Bob:")
    print(f"   Required Skills: {project_requirements}")
    print(f"   Bob's Skills:    {bob_skills}")
    print(f"   Missing Skills:  {gap}")