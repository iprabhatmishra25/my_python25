import string

# ===================================================================
# Step 1: Create the incident_report.txt file (at least 8 lines)
# ===================================================================
incident_content = """Incident ID: INC-84920 - Primary Database Server Outage
On Monday at 08:30 AM, the primary database server experienced a heavy crash.
The sudden outage resulted from high memory utilization and CPU spike.
Database services were unresponsive for approximately forty-five minutes.
The core infrastructure team immediately initiated recovery procedures.
Services were fully restored after rolling back the recent database update.
All operational systems were verified and confirmed stable by 09:45 AM.
A root cause analysis is currently underway to prevent future incidents.
"""

filename = "incident_report.txt"

# Write the text file
with open(filename, "w", encoding="utf-8") as f:
    f.write(incident_content)

print(f"✅ Created file '{filename}' successfully.\n")


# ===================================================================
# Step 2: Read file and compute stats
# ===================================================================
line_count = 0
word_count = 0
char_count = 0
word_freq = {}

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        line_count += 1
        
        # Characters excluding newlines (\n or \r)
        char_count += len(line.rstrip("\r\n"))
        
        # Split line into words
        words = line.split()
        word_count += len(words)
        
        # Count word frequencies (case-insensitive, ignoring words < 4 chars)
        for word in words:
            # Clean punctuation from words (e.g., "outage." -> "outage")
            cleaned_word = word.strip(string.punctuation).lower()
            
            if len(cleaned_word) >= 4:
                word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1


# ===================================================================
# Step 3: Find 5 most common words
# ===================================================================
# Sort dictionary by count descending using sorted()
top_5_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:5]


# ===================================================================
# Step 4: Print Results
# ===================================================================
print("=" * 45)
print("      INCIDENT REPORT TEXT ANALYSIS")
print("=" * 45)
print(f"• Total Lines:              {line_count}")
print(f"• Total Words:              {word_count}")
print(f"• Total Characters:         {char_count} (excluding newlines)")
print("-" * 45)
print("• 5 Most Common Words (>= 4 letters):")
for word, count in top_5_words:
    print(f"   - '{word}': {count} time(s)")
print("=" * 45)