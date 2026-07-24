# CREATE A CLASS 

class Consultant:
    def __init__(self, name , skill , days_on_bench):
        self.name = name
        self.skill = skill
        self.days_on_bench = days_on_bench

    def get_status(self):
        if self.days_on_bench > 30:
            return ("URGENT","High Risk")
        elif self.days_on_bench > 14:
            return ("WARNING", "low risk")
        else:
            return ("OK", "right")

    def __str__(self):
        return f"{self.name} ({self.skill}) - {self.days_on_bench} [{self.get_status()}]"

# ADD A BENCH TRACKER CLASS

class BenchTracker:
    def __init__(self):
        self.Consultant = []

    def add_Consultant(self , Consultant):
        self.Consultant.append(Consultant)

    def urgent_count(self):
        return sum(1 for c in self.Consultant if c.get_status()[0] == "URGENT")

    def sort_by_bench(self):
        self.Consultant = sorted(self.Consultant, key=lambda c: c.days_on_bench , reverse=True )

    def filter_by_skill(self , skill):
        matching_Consultants =[
            c for c  in self.Consultants
            if c.skill.lower() == skill.strip().lower()
        ]
        return BenchTracker(matching_Consultants)

    def average_bench_days(self):
        if not self.Consultant:
            return 0.0
        return round(sum(c.days_on_bench for c in self.Consultants)/ len(self.Consultant),1,)

    def print_report(self):
            print("=== print report===")
            for c in self.Consultant:
                print(c)
            print(f"\n Total urgent cases = {self.urgent_count()}")
    
    # main execution
if __name__ == "__main__":

    tracker = BenchTracker()
    
    tracker.add_Consultant(Consultant("PRABHAT", "PYTHON", 25))
    tracker.add_Consultant(Consultant("OM", "JAVA", 40))
    tracker.add_Consultant(Consultant("VIVEK", "C++", 10))
    tracker.add_Consultant(Consultant("VAIBHAV", "C", 22))
    tracker.add_Consultant(Consultant("RAJESH", "HTML", 59))
    
    tracker.sort_by_bench()
    tracker.print_report()