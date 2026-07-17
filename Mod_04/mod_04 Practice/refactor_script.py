
# 1. Functional Definitions
def calculate_average_cpu(servers: list) -> float:
    """Calculates and returns the average CPU usage across all servers."""
    if not servers:
        return 0.0
    total_cpu = sum(server["cpu"] for server in servers)
    return total_cpu / len(servers)


def check_cpu_alerts(servers: list, threshold: int = 80) -> None:
    """Checks each server and prints an alert if its CPU exceeds the threshold."""
    for server in servers:
        if server["cpu"] > threshold:
            print(f"ALERT: {server['name']} cpu={server['cpu']}%")


def display_metrics(average_cpu: float) -> None:
    """Prints the final system metrics to the console."""
    print(f"Average CPU: {average_cpu:.1f}%")


# 2. Main Execution Block
if __name__ == "__main__":
    # Input data
    servers = [
        {"name": "web", "cpu": 45},
        {"name": "db", "cpu": 92},
        {"name": "api", "cpu": 70}
    ]
    
    # Run alert checks
    check_cpu_alerts(servers, threshold=80)
    
    # Calculate and display the summary statistics
    avg_usage = calculate_average_cpu(servers)
    display_metrics(avg_usage)