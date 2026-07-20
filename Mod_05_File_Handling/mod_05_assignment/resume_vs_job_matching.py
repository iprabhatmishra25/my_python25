import os

# ===================================================================
# Task B1 — Prepare Input Files
# ===================================================================
def setup_files():
    """Creates the 'resumes/' folder, 5 candidate files, and 'job_description.txt'."""
    os.makedirs("resumes", exist_ok=True)

    jd_content = """Job Title: Python Developer
Required Skills: Python, Django, SQL, REST API, Git
Experience: 2+ years
Location: Remote
"""
    with open("job_description.txt", "w", encoding="utf-8") as f:
        f.write(jd_content)

    resumes = {
        "candidate1.txt": "Experienced backend developer with 3 years in Python, Django, and SQL databases. Strong git workflow knowledge.",
        "candidate2.txt": "Frontend engineer specializing in React, HTML, CSS, and basic JavaScript. Interested in learning backend technologies.",
        "candidate3.txt": "Software engineer proficient in Python, REST API development, SQL, Git, and Django web frameworks.",
        "candidate4.txt": "Data analyst with hands-on experience using Python, SQL, Tableau, and Excel for statistical analysis.",
        "candidate5.txt": "DevOps enthusiast with experience in Linux, Docker, Git, REST API integrations, and Python scripting."
    }

    for filename, text in resumes.items():
        with open(os.path.join("resumes", filename), "w", encoding="utf-8") as f:
            f.write(text)


# ===================================================================
# Task B2 — Extract Required Skills from Job Description
# ===================================================================
def extract_jd_skills(filepath="job_description.txt"):
    """Reads job_description.txt and extracts required skills as a lowercase list."""
    skills = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("Required Skills:"):
                raw_skills = line.split(":", 1)[1]
                skills = [skill.strip().lower() for skill in raw_skills.split(",")]
                break
    return skills


# ===================================================================
# Task B3 — Scan Resumes Folder
# ===================================================================
def scan_resumes(folder="resumes"):
    """Scans the resumes folder and returns a dictionary of lowercase text per file."""
    resumes_data = {}
    if not os.path.exists(folder):
        return resumes_data

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                resumes_data[filename] = file.read().lower()
                
    return resumes_data


# ===================================================================
# Task B4 — Match Skills and Score Candidates
# ===================================================================
def match_candidates(jd_skills, resumes_data):
    """Calculates match percentage and matched skills list for each candidate."""
    scores = {}
    detailed_matches = {}
    total_jd_skills = len(jd_skills)

    if total_jd_skills == 0:
        return scores, detailed_matches

    for filename, text in resumes_data.items():
        matched = [skill for skill in jd_skills if skill in text]
        match_percentage = round((len(matched) / total_jd_skills) * 100, 1)
        
        scores[filename] = match_percentage
        detailed_matches[filename] = matched

    return scores, detailed_matches


# ===================================================================
# Task B5 — Generate Shortlist Report
# ===================================================================
def generate_report(scores, detailed_matches, threshold=40.0, output_file="shortlist_report.txt"):
    """Sorts candidates, filters by threshold, and writes shortlist_report.txt."""
    # Sort candidates by match percentage descending
    sorted_candidates = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    report_lines = [
        "===== Candidate Shortlist Report =====",
        "Job Title: Python Developer\n"
    ]

    rank = 1
    for filename, score in sorted_candidates:
        if score >= threshold:
            matched_str = ", ".join(detailed_matches[filename])
            report_lines.append(f"{rank}. {filename} - {score}% match")
            report_lines.append(f"   Matched Skills: {matched_str}\n")
            rank += 1

    report_content = "\n".join(report_lines)
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report_content)

    return report_content


# ===================================================================
# Execution Pipeline
# ===================================================================
if __name__ == "__main__":
    print("Setting up directories and sample files...")
    setup_files()

    print("Extracting skills from Job Description...")
    jd_skills = extract_jd_skills("job_description.txt")
    print(f"   Required Skills: {jd_skills}")

    print("Scanning resumes folder...")
    resumes_data = scan_resumes("resumes")
    print(f"   Scanned {len(resumes_data)} candidate files.")

    print(" Scoring candidates...")
    scores, detailed_matches = match_candidates(jd_skills, resumes_data)

    print("Generating shortlist report...")
    report = generate_report(scores, detailed_matches, threshold=40.0)

    print("\n" + report)
    print("Pipeline complete. 'shortlist_report.txt' generated successfully!")