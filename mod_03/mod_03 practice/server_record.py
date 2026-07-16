# Create the starting server dictionary with 6 keys
server = {
    "name": "Web--Server-01",
    "environment": "Delivery",
    "IP": "192.168.1.50",
    "CPU percentage": 87,        
    "memory percentage": 66,
    "online status": "Active"
}

# (a) Print each key-value pair using a .items() loop with f-string formatting
print("Server Info")
for key, value in server.items():
    print(f"{key}: {value}")
print("-" * 20)

# (b) Add a "disk" key
server["disk"] = "526GB"
print(f"(b) Added disk key. New dictionary: {server}")
print("-" * 25)

# (c) Safely retrieve a "last_reboot" key using .get() with a default value
# Using .get() prevents the program from crashing if the key is missing
reboot_time = server.get("last_reboot", "Never Rebooted")
print(f"(c) Last Reboot: {reboot_time}")
print("-" * 20)

# (d) Check whether CPU is above 80 and print a status message
print("--- (d) CPU Alert Check ")
if server["CPU percentage"] > 80:
    print(f"ALERT: CPU usage is too high! Current usage: {server['CPU percentage']}%")
else:
    print(f"Normal: CPU usage is fine. Current usage: {server['CPU percentage']}%")