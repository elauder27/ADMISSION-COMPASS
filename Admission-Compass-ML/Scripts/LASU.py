from pathlib import Path
import os
import random
import pandas as pd

# Faculties and departments
departments = {
    "Arts": [
        "English Language", "Linguistics", "Philosophy", "History and International studies",
        "Theatre Arts", "Music", "Christian Religious Studies", "Arabic", "French", "Islamic Studies", "Peace Studies",
        "Portuguese / English", "Yoruba"
    ],
    "Social Sciences": [
        "Economics", "Political Science", "Geography and Planning",
        "Psychology", "Sociology"
    ],
    "Management Sciences": [
        "Business Administration", "Industrial Relations and Human Resouce Management", "Insurance",
        "Accounting", "Banking and Finance", "Project Management", "Taxation",
        "Marketing", "Public Administration", "Local Government Development and Administration"
    ],
    "Law": [
        "Common/Civil Law", "Common/Islamic Law"
        # "Jurisprudence International Law", "Law", "International and Islamic Law",
        # "Public and Private Law", "Business Law"
    ],
    "Science": [
        "Mathematics", "Physics", "Chemistry", "Computer Science", "Zoology", "Fisheries and Aquatic Biology",
        "Botany", "Microbiology", "Biochemistry", "Science Laboratory Technology"
    ],
    "Engineering": [
        "Chemical Engineering", "Electronic and Computer Engineering", "Civil Engineering",
        "Mechanical Engineering", "Industrial Enginerring", "Aeronautical and Astronautical Engineering"
    ],
    "Education": [
        "Biology Education", "Business Education", "Chemistry Education", "Christian Religious Studies Education",
        "Computer Science Education", "Early Childhood Education", "Economics Education", "Educational Management",
        "English Education", "French Education", "Geography Education", "Guidance & Counselling", "Health Education",
        "History Education", "Islamic Studies Education", "Mathematics Education", "Physical & Health Education",
        "Physics Education", "Political Science Education", "Special Education", "Technology & Vocational Education", "Yoruba Education", "Arabic Education"
    ],
    #  "Clinical Science": [
    #     "Medicine", "Surgery", "Nursing", "Anasthesia",
    #     "Behavioural Medicine", "Community Health and Primary Care",
    #     "Obstetrics and Gynaecologist", "Pediatric and Child Health", "Radiology"
    # ],
    # "Allied Health Science": [
    #     "Physiotherapy", "Medical Laboratory Science", "Radiography"
    # ],
    # "Basic Medical Sciences": [
    #     "Anatomy", "Chemical Pathology", "Hematology and Blood Transfusion",
    #     "Medical Biochemistry", "Medical Microbiology and Parasitology",
    #     "Pathology and Forensic Medicine", "Pharmacology", "Physiology"
    # ],
    # "Dentistry": [
    #     "Child Dental Health", "Oral and Maxillofacial Surgery", "Oral Pathology/Oral Medicine",
    #     "Preventive Dentistry", "Restorative Dentistry"
    # ],
    "College of MEdicine": [
        "Dentistry", "Medical Laboratory Science", "Medicine & Surgery", "Nursing", "Pharmacy",
        "Pharmacology", "Physiology", "Physiotherapy", "Radiography & Radiation Science"
    ],
    "Environmental Science": [
        "Architecture", "Building", "Estate Management", "Environmental Management", "Fine Arts", "Industrial Design",
        "Survey and Geo-Informatics", "Quantity Surveying", "Urban and Regional Planning"
    ],
    "Agriculture": [
        "Agricultural Economics", "Agricultural Extension & Rural Development", "Animal Science", "Crop Production"
    ],
    "Communication and Media Studies": [
        "Mass Communication"
        # "Broadcasting", "Journalism", "Public Relations and Advertising"
    ],
    "Scool of Transport": [
        "Transport Management and Operations", "Logistics and Supply Chain Management"
        # "Transport Planning and Policy", "Transport Technology and Infrastructure"
    ],
    "Scool of Library Archival and Information Science": [
        "Library and information Science"
        # "Collection Development", "Readers Services", "Technical Services"
    ]
}

# o'level grading scale
olevel_scale = {
    'A1': 10, 'B2': 9, 'B3': 8, 'C4': 7,
    'C5': 6, 'C6': 5
}

# Simulate dataset
num_applicants = 10000
data = []

for _ in range(num_applicants):
    faculty = random.choice(list(departments.keys()))
    department = random.choice(departments[faculty])

    # Simulate UTME score
    utme_score = random.randint(120, 400)

    # Simulate O'level grades and score
    grades = random.choices(list(olevel_scale.keys()), k=5)
    olevel_points = [olevel_scale[g] for g in grades]
    olevel_avg = sum(olevel_points)

    # screening score calculation: 50% UTME + 50% O'level
    screening_score = round((utme_score / 8) + sum(olevel_points), 2)

    # O'level passed (assume pass if no F9 or more than 2 sittings)
    sittings = random.choice([1, 2, 3])  # simulate
    olevel_passed = (all(score > 0 for score in olevel_points)
                     and sittings <= 2)

    # Admission logic
    if utme_score >= 195 and screening_score >= 50 and olevel_passed:
        admitted = "admitted"
    else:
        admitted = "not admitted"

    data.append([
        faculty, department, utme_score, screening_score, olevel_passed, admitted, ", ".join(
            grades)
    ])

# Create dataframe
df = pd.DataFrame(data, columns=[
    "faculty", "department", "utme_score",
    "screening_score", "olevel_passed", "admitted", "olevel_grades"
])

# Save to CSV

# ... your data generation code ...

ROOT_DIR = Path(__file__).resolve().parent.parent
# get the file path dynamically, note to Chosen:
# # don't hard code file paths like this base_dir = r"C:\Users\USER\Desktop\ADMISSION-COMPASS\Admission-Compass-ML\Data"

base_dir = ROOT_DIR / "Data"

os.makedirs(base_dir, exist_ok=True)

file_path = os.path.join(base_dir, "LASU.csv")
df.to_csv(file_path, index=False)

print("Dataset saved successfully at:", file_path)

print("Dataset generated successfully!")
