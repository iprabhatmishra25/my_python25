# The starting lists of user login IDs
sys_a = [1001, 1002, 1003, 1004, 1001, 1002]
sys_b = [1002, 1003, 1005, 1006]

# Convert the lists into sets to remove duplicates automatically
set_a = set(sys_a)
set_b = set(sys_b)

# (a) Find how many unique IDs are in each system
print(f"(a) Unique IDs in System A: {set_a} (Total: {len(set_a)})")
print(f"    Unique IDs in System B: {set_b} (Total: {len(set_b)})")
print("-" * 50)

# (b) Which IDs exist in both systems (Intersection)
both_systems = set_a.intersection(set_b)
print(f"(b) IDs in BOTH systems: {both_systems}")
print("-" * 50)

# (c) Which IDs are only in system A (Difference)
only_in_a = set_a.difference(set_b)
print(f"(c) IDs ONLY in System A: {only_in_a}")
print("-" * 50)

# (d) Which IDs are only in system B (New users to provision)
only_in_b = set_b.difference(set_a)
print(f"(d) IDs ONLY in System B (New users): {only_in_b}")
print("-" * 50)

# (e) The total number of unique IDs across both systems (Union)
all_unique_ids = set_a.union(set_b)
print(f"(e) Combined unique IDs: {all_unique_ids}")
print(f"    Total count across both systems: {len(all_unique_ids)}")
