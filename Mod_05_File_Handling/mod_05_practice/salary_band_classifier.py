import csv

# ===================================================================
# Step 1: Create staff.csv with sample data
# ===================================================================
staff_data = [
    ["name", "role", "salary"],
    ["Aarav Sharma", "Software Engineer", "55000"],
    ["Priya Nair", "Senior Analyst", "95000"],
    ["Rohan Mehta", "DevOps Specialist", "75000"],
    ["Sneha Kapur", "Junior QA Engineer", "48000"],
    ["Vikram Patel", "Tech Lead", "120000"],
    ["Ananya Rao", "Frontend Developer", "60000"],
    ["Karan Singh", "Data Scientist", "88000"]
]

with open("staff.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(staff_data)

print(" 'staff.csv' created successfully.")


# ===================================================================
# Step 2: Read staff.csv, classify salary bands, and write staff_banded.csv
# ===================================================================
with open("staff.csv", "r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    
    # Prepare fieldnames for the new CSV (original columns + 'band')
    fieldnames = reader.fieldnames + ["band"]
    
    banded_records = []
    
    for row in reader:
        # Convert salary to integer
        salary = int(row["salary"])
        
        # Determine Salary Band
        if salary < 60000:
            band = "Junior"
        elif 60000 <= salary <= 90000:
            band = "Mid"
        else:
            band = "Senior"
            
        # Add the band to the row dictionary
        row["band"] = band
        banded_records.append(row)

# Write to staff_banded.csv
with open("staff_banded.csv", "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(banded_records)

print(" 'staff_banded.csv' generated successfully.\n")


# ===================================================================
# Step 3: Display output contents for verification
# ===================================================================
print("--- Contents of staff_banded.csv ---")
with open("staff_banded.csv", "r", encoding="utf-8") as f:
    print(f.read())