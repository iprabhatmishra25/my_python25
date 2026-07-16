# Starting list of IP addresses

ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.5"]
print("Starting list:      ", ips)

# (a) Add two more IPs to the end
# We use .extend() to add multiple items at once
ips.extend(["10.0.0.6", "10.0.0.7"])
print("After adding two:   ", ips)

# (b) Insert "10.0.0.1" as the first item
# Index 0 is the very first position in Python
ips.insert(0, "10.0.0.1")
print("After inserting:  ", ips)

# (c) Remove "10.0.1.3"
# We use .remove() to delete a specific item by name

ips.remove("10.0.0.3")
print("After removing:  ", ips)

# (d) Sort the list
# We use .sort() to put the IPs in order\

ips.sort()
print("After sorting:  " , ips)
      
# (e) Use a list comprehension to keep only IPs starting with "10.0.1"
# .startswith() checks how each IP string begins
filtered_ips = [ip for ip in ips if ip.startswith("10.0.1")]
print("(e) Filtered list (10.0.1):", filtered_ips)