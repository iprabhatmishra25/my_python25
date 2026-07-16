# 1. IMMUTABLE CONFIG TUPLE
# =====================================================================
# This tuple holds the inventory date, company name, and currency code.
# Because it is a tuple, these values cannot be accidentally modified.
asset_meta = ("2026-07-16", "GlobalCorp IT", "INR")

# Unpack the tuple into three separate variables for headers
inventory_date, company_name, currency = asset_meta

# 2. ASSETS LIST (Our master database)
# =====================================================================
# A list of dictionaries representing our IT assets.
assets = [
    {
        "asset_id": "AST-101",
        "type": "laptop",
        "owner": "Prabhat",
        "location": "Mumbai",
        "purchase_year": 2023,
        "value_inr": 85000,
    },
    {
        "asset_id": "AST-102",
        "type": "server",
        "owner": "unassigned",
        "location": "Bengaluru",
        "purchase_year": 2020,
        "value_inr": 250000,
    },
    {
        "asset_id": "AST-103",
        "type": "network",
        "owner": "unassigned",
        "location": "Mumbai",
        "purchase_year": 2021,
        "value_inr": 120000,
    },
    {
        "asset_id": "AST-104",
        "type": "phone",
        "owner": "Ananya",
        "location": "Delhi",
        "purchase_year": 2024,
        "value_inr": 60000,
    },
    {
        "asset_id": "AST-105",
        "type": "laptop",
        "owner": "Ayush",
        "location": "Bengaluru",
        "purchase_year": 2025,
        "value_inr": 95000,
    },
    {
        "asset_id": "AST-106",
        "type": "server",
        "owner": "unassigned",
        "location": "Chennai",
        "purchase_year": 2019,
        "value_inr": 300000,
    },
]

# Print Output Header using the unpacked tuple variables
print("=" * 60)
print(f"       {company_name.upper()} IT ASSET INVENTORY REPORT")
print(f"       Date: {inventory_date} | Currency: {currency}")
print("=" * 60)

# 3. GROUP BY TYPE (Dictionary of Lists)
# =====================================================================
# Initialize an empty list for each allowed asset type
grouped_by_type = {"laptop": [], "server": [], "network": [], "phone": []}

# Populating the dictionary with asset IDs matching their types
for asset in assets:
    asset_type = asset["type"]
    asset_id = asset["asset_id"]
    grouped_by_type[asset_type].append(asset_id)

print("\n[+] Assets Grouped by Type:")
for asset_type, ids in grouped_by_type.items():
    print(f"  * {asset_type.capitalize()}: {ids}")

# 4. UNIQUE LOCATIONS (Sets)
# =====================================================================
# Using a set to automatically extract unique cities
locations_set = set()
for asset in assets:
    locations_set.add(asset["location"])

# Convert set to a sorted list for readable presentation
sorted_locations = sorted(list(locations_set))

print("\n[+] Office Locations with Assets:")
print(f"  * Total Unique Locations: {len(locations_set)}")
print(f"  * Cities: {', '.join(sorted_locations)}")


# 5. FINANCIAL SUMMARY
# =====================================================================
total_value = 0
most_expensive_asset = None
highest_value = 0

# Dictionary to hold running total of values per type
value_by_type = {"laptop": 0, "server": 0, "network": 0, "phone": 0}

for asset in assets:
    value = asset["value_inr"]
    total_value += value

    # Accumulate value by asset type
    value_by_type[asset["type"]] += value

    # Find the most expensive asset
    if value > highest_value:
        highest_value = value
        most_expensive_asset = asset["asset_id"]

# Calculations
average_value = total_value / len(assets)

print("\n[+] Financial Summary:")
print(f"  * Total Asset Value: {currency} {total_value:,}")
print(f"  * Average Value per Asset: {currency} {average_value:,.2f}")
print(
    f"  * Most Expensive Asset: {most_expensive_asset} ({currency} {highest_value:,})"
)
print("  * Total Value by Type:")
for asset_type, val in value_by_type.items():
    print(f"    - {asset_type.capitalize()}: {currency} {val:,}")

# 6. AGEING REPORT (List Comprehension)
# =====================================================================
# Extracts IDs of assets purchased before 2022 (older than 4 years in 2026)
flagged_for_replacement = [
    asset["asset_id"] for asset in assets if asset["purchase_year"] < 2022
]

print("\n[+] Ageing Report (Flagged for Replacement):")
if flagged_for_replacement:
    print(f"  * Review Required: {flagged_for_replacement}")
else:
    print("  * No assets require replacement at this time.")

print("=" * 60)