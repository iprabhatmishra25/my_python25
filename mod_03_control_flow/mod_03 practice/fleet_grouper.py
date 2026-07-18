# The starting list of 6 server dictionaries
servers = [
    {"name": "web-prod-01", "env": "production", "cpu": 45},
    {"name": "db-prod-01", "env": "production", "cpu": 75},
    {"name": "web-stage-01", "env": "staging", "cpu": 30},
    {"name": "api-stage-01", "env": "staging", "cpu": 50},
    {"name": "test-dev-01", "env": "dev", "cpu": 20},
    {"name": "test-dev-02", "env": "dev", "cpu": 10}
]

# (a) Group all server names by environment
# ==========================================
# We set up an empty dictionary with empty lists for each environment
grouped_servers = {
    "production": [],
    "staging": [],
    "dev": []
}

# Loop through each server and add its name to the right list
for s in servers:
    environment = s["env"]
    name = s["name"]
    grouped_servers[environment].append(name)

print("--- (a) Grouped Server Names ---")
print(grouped_servers)
print("-" * 50)

# (b) Calculate average CPU per environment
# ==========================================
# We will create an empty dictionary to hold the results
cpu_averages = {}

# Go through each environment to find the CPU values
for target_env in ["production", "staging", "dev"]:
    total_cpu = 0
    count = 0
    
    # Check all servers to see if they match the current environment
    for s in servers:
        if s["env"] == target_env:
            total_cpu += s["cpu"]
            count += 1
            
    # Calculate the average (Total CPU divided by the count of servers)
    if count > 0:
        cpu_averages[target_env] = total_cpu / count
    else:
        cpu_averages[target_env] = 0


# (c) Print a summary table
# ==========================================
print("--- Summary Table ---")
# Using headers for our table
print(f"{'Environment':<15} | {'Server Count':<12} | {'Avg CPU (%)':<12}")
print("-" * 47)

# Loop through environments to print their stats nicely aligned
for env in ["production", "staging", "dev"]:
    server_count = len(grouped_servers[env])
    avg_cpu = cpu_averages[env]
    
    # :<15 forces left-alignment with spaces to look clean 
    print(f"{env:<15} | {server_count:<12} | {avg_cpu:<12.1f}")