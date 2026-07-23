# ==========================================
# Script Name: onboarding.py
# Purpose    : Automated Employee Onboarding Summary
# ==========================================

# 1. Employee & Equipment Variables
full_name = "Prabhat Mishra"
emp_id = 1042  # Stored as an integer
job_title = "Systems Administrator"
department = "Information Technology"
laptop_model = "MacBook Pro 16-inch"
raw_email = "   Prabhat.Mishra@YourCompany.com   "  # Messy raw email
temp_password = "Welcome2026!Secure"
start_date = "2026-08-03"

# 2. Data Cleaning & Calculations
# Clean email: remove leading/trailing whitespace and convert to lowercase
clean_email = raw_email.strip().lower()

# Format Employee ID to always be 6 digits with leading zeros
formatted_emp_id = f"{emp_id:06d}"

# Check if email ends with the valid company domain
company_domain = "@yourcompany.com"
email_valid = clean_email.endswith(company_domain)

# 3. Output - Formatted Onboarding Welcome Card
welcome_card = f"""
==================================================
            EMPLOYEE ONBOARDING CARD              
==================================================

[ EMPLOYEE DETAILS ]
--------------------------------------------------
Full Name      : {full_name}
Employee ID    : {formatted_emp_id}
Job Title      : {job_title}
Department     : {department}
Start Date     : {start_date}

[ SYSTEM & HARDWARE ACCESS ]
--------------------------------------------------
Assigned Hardware : {laptop_model}
Assigned Email    : {clean_email}
Temp Password     : {temp_password}

--------------------------------------------------
Email Domain Verified : {email_valid}
==================================================
"""

print(welcome_card)