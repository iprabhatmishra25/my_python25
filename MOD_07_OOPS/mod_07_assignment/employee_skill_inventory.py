# CREATE CLASS WITH A INSTANCES

class Employee:
    def __init__(self,name,skills,experience,location):
        self.name = name
        self.skills = skills
        self.experience = experience
        self.location = location

    def __str__(self):
        skills_formatted =", ".join(sorted(self.skills))
        return (
            f"EMPLOYEE" : {self.name:<15} | Location : {self.location:<10} |"
            f"EXP": {self.experience} yrs | skills : [{skills_formatted}]"

        )

    def has_skill(self,skill):
        return skill.strip().lower in (s.lower() for s in self.skills)