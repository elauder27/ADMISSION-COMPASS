import random
import pandas as pd

# Faculties and departments
departments = {
    "Agriculture": [
        "Agricultural Economics and Extension Services", "Animal Production, Fisheries and Aquaculture", "Crop Production", "Food Science and Technology"
    ],
    "Allied Health Science": [
        "Environmental Health Science", "Medical Laboratory Science", "Public Health"
    ],
    "Arts": [
        "Arabic and French", "English Language and Linguistics", "Fine and Applied Arts", "Performing Arts and Film Studies",
        "Religions, History and Heritage Studies"
    ],
    "Education": [
        "Business and Entrepreneurship Education", "Early Childhood and Primary Education", 
        "Human Kinetic and Health Education", "Special Education", "Educational Management", "Arts and Science Education"
    ],
    "Engineering and Technology": [
        "Aeronautics and Astronautics Engineering", "Civil and Environmental Engineering",
        "Electrical and Computer Engineering", "Food and Agricultural Engineering",
        "Materials Science and Engineering", "Mechanical Engineering"
    ],
    "Information and Communication Technology": [
        "Computer Science", "Library and Information Science", "Mass Communication"
    ],
    "Law": [
        "Jurisprudence and Public Law", "Business and Private Law", "Common Law"
    ],
    "Management and Social Sciences": [
       "Business and Entrepreneurship", "Accounting and Finance", "Economics and Development Studies",
       "Tourism and Hospitality Management", "Politics and Governance"
    ],
    "Pure and Applied Science": [
        "Microbiology", "Biochemistry", "Zoology", "Chemical, Geological and Physical Sciences",
        "Geology and Mineral Sciences", "Chemistry and Industrial Chemistry", "Environmental Management and Toxicology",
        "Mathematics and Statistics", "Plant and Environmental Biology"
    ]
}

# o'level grading scale
olevel_scale = {
     'A1': 10, 'B2': 9, 'B3': 8, 'C4': 7,
    'C5': 6, 'C6': 5
}

# Departmental cut-off marks (KWASU 2025/2026 examples)
department_cutoffs = {
    "Medicine and Surgery": 280,
    "Medical Laboratory Science": 280,
    "Computer Science": 200,
    "Mass Communication": 200,
    "Architecture": 200,
    "Business and Entrepreneurship": 160,  # closest to Business Admin
    "Accounting and Finance": 160,
    "Civil and Environmental Engineering": 220,
    "Mechanical Engineering": 220,
    "Electrical and Computer Engineering": 230,
    # default general cutoff
    "default": 140
}

# Simulate dataset
num_applicants = 10000
data = []

for _ in range(num_applicants):
    faculty = random.choice(list(departments.keys()))
    department = random.choice(departments[faculty])
    
    #Simulate UTME score
    utme_score = random.randint(120, 400)
    
    #Simulate O'level grades and score
    grades = random.choices (list(olevel_scale.keys()), k=5)
    olevel_points = [olevel_scale[g] for g in grades]
    olevel_avg = sum(olevel_points)

    #screening score calculation: 50% UTME + 50% O'level
    screening_score = round((utme_score / 8) + sum(olevel_points), 2)
    
    # O'level passed (assume pass if all >= C6, max 2 sittings allowed)
    sittings = random.choice([1, 2, 3])  # simulate
    olevel_passed = all(score > 0 for score in olevel_points) and sittings <= 2
    
     # Department-specific cutoff
    cutoff = department_cutoffs.get(department, department_cutoffs["default"])

    # Admission logic
    if utme_score >= 140 and screening_score >= cutoff and olevel_passed:
        admitted = "admitted"
    else:
        admitted = "not admitted"
    
    data.append([
        faculty, department, utme_score, screening_score, olevel_passed, admitted, ", ".join(grades)
    ])

# Create dataframe
df = pd.DataFrame(data, columns=[
    "faculty", "department", "utme_score",
    "screening_score", "olevel_passed", "admitted", "olevel_grades"
])

# Save to CSV
import os
import pandas as pd
import random

# ... your data generation code ...

# Construct full path to save the file reliably
# Ensure Data folder exists
os.makedirs("Data", exist_ok=True)
data_path = os.path.join("Data", "KWASU.csv")
df.to_csv(data_path, index=False)

print("Dataset generated successfully!")
