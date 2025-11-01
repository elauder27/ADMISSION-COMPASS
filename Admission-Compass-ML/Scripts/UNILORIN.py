import os
from pathlib import Path
import random
import pandas as pd

# Faculties and Departments for UNILORIN
departments = {
    "Agriculture": [
        "Agricultural Economics and Farm Management",
        "Agricultural Extension and Rural Development",
        "Agronomy",
        "Animal Production",
        "Crop Protection",
        "Home Economics and Food Science",
        "Forest Resources Management",
        "Aquaculture and Fisheries"
    ],
    "Arts": [
        "Arabic", "English", "French",
        "History and International Studies",
        "Linguistics and Nigerian Languages",
        "Performing Arts",
        "Religions (Christian/Islamic/Comparative)",
        "Yoruba"
    ],
    "Education": [
        "Adult and Primary Education",
        "Arts Education",
        "Counsellor Education",
        "Educational Management",
        "Educational Technology",
        "Health Promotion and Environmental Health Education",
        "Human Kinetics Education",
        "Science Education",
        "Social Sciences Education"
    ],
    "Engineering and Technology": [
        "Agricultural and Biosystems Engineering",
        "Biomedical Engineering",
        "Chemical Engineering",
        "Civil Engineering",
        "Computer Engineering",
        "Electrical and Electronics Engineering",
        "Food & Bioprocess Engineering",
        "Materials & Metallurgical Engineering",
        "Mechanical Engineering",
        "Water Resources & Environmental Engineering"
    ],
    "Law": ["Law"],
    "Life Sciences": [
        "Microbiology", "Plant Biology", "Zoology", "Biochemistry"
    ],
    "Management Sciences": [
        "Accounting", "Finance", "Business Administration",
        "Marketing", "Industrial Relations and Personnel Management",
        "Public Administration"
    ],
    "Physical Sciences": [
        "Chemistry", "Industrial Chemistry", "Physics",
        "Mathematics", "Statistics", "Geology", "Geophysics", "Computer Science"
    ],
    "Social Sciences": [
        "Economics", "Geography", "Political Science",
        "Psychology", "Social Work", "Sociology"
    ],
    "Communication and Information Sciences": [
        "Computer Science", "Information and Communication Science",
        "Library and Information Science", "Telecommunication Science"
    ],
    "Environmental Sciences": [
        "Architecture", "Estate Management", "Quantity Surveying",
        "Surveying and Geo-informatics", "Urban and Regional Planning"
    ],
    "Basic Medical Sciences": [
        "Anatomy", "Physiology", "Biomedical Science"
    ],
    "Clinical Sciences": [
        "Medicine and Surgery", "Nursing Science"
    ],
    "Pharmaceutical Sciences": [
        "Pharmacy"
    ],
    "Veterinary Medicine": [
        "Veterinary Medicine"
    ],
    "Agriculture and Renewable Natural Resources": [
        "Forestry and Wildlife Management",
        "Fisheries and Aquaculture"
    ]
}

# UNILORIN O’level grading scale (4.0 max)
olevel_scale = {
    "A1": 4.0, "B2": 3.6, "B3": 3.2,
    "C4": 2.8, "C5": 2.4, "C6": 2.0
}

# Function to calculate UNILORIN screening score
def calculate_unilorin_aggregate(utme, post_utme, grades):
    utme_score = (utme / 400) * 50  # 50%
    post_utme_score = (post_utme / 30) * 30  # 30%
    olevel_points = sum(olevel_scale[g] for g in grades)
    olevel_avg = olevel_points / 5
    olevel_score = olevel_avg * 5  # scaled to 20%
    total = utme_score + post_utme_score + olevel_score
    return round(total, 2)

# Generate dataset
num_applicants = 10000
data = []

for _ in range(num_applicants):
    faculty = random.choice(list(departments.keys()))
    department = random.choice(departments[faculty])

    # Random scores
    utme_score = random.randint(140, 400)
    post_utme_score = round(random.uniform(0, 30), 2)
    grades = random.choices(list(olevel_scale.keys()), k=5)
    sittings = random.choice([1, 2])

    # Calculate screening score
    aggregate_score = calculate_unilorin_aggregate(utme_score, post_utme_score, grades)

    # O’level validity (no fail, max 2 sittings)
    olevel_valid = all(olevel_scale[g] >= 2.0 for g in grades)
    sittings_valid = sittings <= 2

    # Admission decision logic
    if utme_score >= 180 and aggregate_score >= 50 and olevel_valid and sittings_valid:
        admission_status = "admitted"
    else:
        admission_status = "not admitted"

    data.append([
        faculty, department, utme_score, post_utme_score, aggregate_score,
        olevel_valid, sittings, admission_status, ", ".join(grades)
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Faculty", "Department", "UTME_Score", "Post_UTME_Score",
    "Aggregate_Score", "Olevel_Valid", "Sittings",
    "Admission_Status", "Olevel_Grades"
])

# Save to CSV in your project’s Data folder
ROOT_DIR = Path(__file__).resolve().parent.parent
base_dir = ROOT_DIR / "Data"
os.makedirs(base_dir, exist_ok=True)

file_path = os.path.join(base_dir, "UNILORIN.csv")
df.to_csv(file_path, index=False)

print("✅ UNILORIN dataset saved successfully at:", file_path)
print("Preview:")
print(df.head())
