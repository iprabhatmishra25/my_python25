def check_system_health(server_name, cpu, mem, threshold=80):

    """check the resources threshold"""

    worst=max(cpu,mem)
    return worst>=threshold
print(check_system_health("server1", 70 ,80))