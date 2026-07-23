# CREATE A CLASS WITH ITS INSTANCE ATTRIBUTES

class consultant:
    def __init__(self,name,skill,days_on_bench):
        self.name = name
        self.skill = skill
        self.days_on_bench = days_on_bench

# ADD METHODS INSIDE CLASS

    def get_status(self):
        if self.days_on_bench > 30:
            return "URGENT"
        elif self.days_on_bench > 14:
            return "WARNING"

        return "OK"
    
# ADD METHODS 

    def __str__(self):
        return f"{self.name} ({self.skill}) - {self.days_on_bench} [{self.get_status}]"

# DESIGN A BENCH TRACKER CLASS 

class benchtracker:
    def __init__(self):
        self.consultant = []

    def add_consultant(self , consultant):
        self.consultant.append(consultant)

    def count_urgent(self):
        return sum(1 for c in self.consultant if c.get_status() == "URGENT")

    def sort_by_bench(self):
        self.consultant = sorted(self.consultant, key=lambda c: c.days_on_bench , reverse=True)

    def print_report(self):
        print("=== print report===")
        for c in self.consultant:
            print(c)
        print(f"\n Total urgent cases = {self.count_urgent()}")

# main execution

tracker = benchtracker()

tracker.add_consultant(consultant("PRABHAT", "PYTHON", 25))
tracker.add_consultant(consultant("OM", "JAVA", 40))
tracker.add_consultant(consultant("VIVEK", "C++", 10))
tracker.add_consultant(consultant("VAIBHAV", "C", 22))
tracker.add_consultant(consultant("RAJESH", "HTML", 59))

tracker.sort_by_bench()
tracker.print_report()



