def GREET_USER(name):  # 1. 'def' starts the function, 'name' is the input (parameter)
    message = f"HELLO, {name.upper()}!" # 2. The task it performs (output in CAPS!)
    return message     # 3. 'return' sends the result back

# Calling the function:
output = GREET_USER("clover")
print(output)  