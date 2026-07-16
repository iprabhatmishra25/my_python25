# =====================================================================
# 1. SETUP: Create our starting list
# =====================================================================
print("--- 1. Starting List ---")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
print("-" * 40)

# =====================================================================
# 2. ADDING ITEMS
# =====================================================================
print("--- 2. Adding Items ---")

# .append() -> Adds an item to the VERY END of the list
fruits.append("orange")
print("After append('orange'):", fruits)

# .insert() -> Adds an item at a SPECIFIC index/position (index, item)
fruits.insert(1, "blueberry")  # Puts blueberry at index 1 (second place)
print("After insert(1, 'blueberry'):", fruits)

# .extend() -> Adds multiple items from another list to the end
more_fruits = ["mango", "grapes"]
fruits.extend(more_fruits)
print("After extend(more_fruits):", fruits)
print("-" * 40)

# =====================================================================
# 3. REMOVING ITEMS
# =====================================================================
print("--- 3. Removing Items ---")

# .remove() -> Removes the first item that matches the value
fruits.remove("banana")
print("After remove('banana'):", fruits)

# .pop() -> Removes and returns the last item (or at a specific index)
removed_item = fruits.pop()  # Removes the last item
print(f"After pop() (Removed '{removed_item}'):", fruits)

specific_pop = fruits.pop(2)  # Removes the item at index 2
print(f"After pop(2) (Removed '{specific_pop}'):", fruits)
print("-" * 40)

# =====================================================================
# 4. FINDING & COUNTING ITEMS
# =====================================================================
print("--- 4. Finding & Counting ---")

# Let's add an extra 'apple' to show how count works
fruits.append("apple")
print("Current list:", fruits)

# .count() -> Counts how many times an item appears
apple_count = fruits.count("apple")
print(f"How many apples? {apple_count}")

# .index() -> Finds the position/index of the first matching item
apple_position = fruits.index("apple")
print(f"Where is the first 'apple' located? Index {apple_position}")
print("-" * 40)

# =====================================================================
# 5. SORTING & REVERSING
# =====================================================================
print("--- 5. Sorting & Reversing ---")

# .reverse() -> Flips the list completely upside down
fruits.reverse()
print("After reverse():", fruits)

# .sort() -> Sorts the list alphabetically (or numerically for numbers)
fruits.sort()
print("After sort() (Alphabetical):", fruits)

# .sort(reverse=True) -> Sorts in reverse alphabetical order
fruits.sort(reverse=True)
print("After sort(reverse=True):", fruits)
print("-" * 40)

# =====================================================================
# 6. COPYING & CLEARING
# =====================================================================
print("--- 6. Copying & Clearing ---")

# .copy() -> Creates a separate duplicate clone of the list
fruits_clone = fruits.copy()
print("Cloned list:", fruits_clone)

# .clear() -> Empties the entire list out completely
fruits.clear()
print("After clear():", fruits)
print("Is the clone still safe?", fruits_clone)
print("-" * 40)