import os
import random
import pandas as pd

# Faculties and departments for EKSU
departments = {
    "Agricultural Science": [
        "Agricultural Economics and Extension Services",
        "Animal Production & Health Sciences",
        "Crop, Horticulture and Landscape Design",
        "Soil Resources and Environmental Management",
        "Forestry Resources and Wildlife Management",
        "Fisheries and Aquaculture Management"
    ],
    "Arts": [
        "Religious Studies", "Islamic Religious Studies/Arabic", "Christian Religious Studies",
        "English & Literary Studies", "History & International Studies", "Linguistics & Nigerian Languages",
        "Theatre and Media Arts", "French", "Yoruba", "Philosophy"
    ],
    "Education": [
        "English Education", "French Education", "Yoruba Education", "Education Christian Religious Studies",
        "Education Arabic Studies", "Education History", "Biology Education", "Mathematics Education",
        "Chemistry Education", "Basic/Integrated Science Education", "Computer Science Education",
        "Physics Education", "Social Studies", "Economics Education", "Political Science Education",
        "Geography Education", "Agricultural Education", "Library and Information Science",
        "Mechanical Technology", "Building and Woodwork Technology", "Electrical/Electronic Technology",
        "Business Education - Accounting", "Business Education - Marketing", "Business Education - Office Management",
        "Educational Technology", "Nursery & Primary/Early Childhood Education", "Test, Measurement and Evaluation",
        "Guidance and Counselling", "Human Kinetics/Physical & Health Education", "Health Education",
        "Adult Education", "Educational Management"
    ],
    "Engineering": [
        "Civil Engineering", "Computer Engineering", "Electrical/Electronic Engineering", "Mechanical Engineering"
    ],
    "Law": ["Law"],
    "Management Sciences": [
        "Accounting", "Banking and Finance", "Business Administration", "Actuarial Science",
        "Entrepreneurship", "Insurance", "Cooperative Studies", "Marketing",
        "Industrial Relations and Personnel Management"
    ],
    "Medicine": [
        "Medicine and Surgery", "Nursing", "Anatomy", "Physiology"
    ],
    "Science": [
        "Biochemistry", "Chemistry", "Industrial Chemistry", "Geology", "Geo-Physics", "Mathematics",
        "Computer Science", "Statistics", "Microbiology", "Physics", "Plant Sciences and Biotechnology",
        "Science Laboratory Technology", "Zoology"
    ],
    "Social Sciences": [
        "Economics", "Geography and Planning Science", "Tourism Studies",
        "Psychology", "Political Science", "Sociology", "Environmental Management"
    ]
}

# EKSU O'level grading scale
olevel_scale = {
    "A1": 8, "B2": 7, "B3": 6,
    "C4": 5, "C5": 4, "C6": 3,
    "D7": 2 #"E8": 1, "F9": 0
}

# Function to calculate EKSU screening score
def calculate_screening(utme, grades):
    utme_score = (utme / 400) * 60  # normalized UTME to 60%
    olevel_points = sum(olevel_scale[g] for g in grades)
    olevel_score = (olevel_points / 40) * 40  # normalized to 40%
    return round(utme_score + olevel_score, 2)

# Generate dataset
num_applicants = 10000
data = []

for _ in range(num_applicants):
    # Random faculty & department
    faculty = random.choice(list(departments.keys()))
    department = random.choice(departments[faculty])
    
    # UTME score
    utme_score = random.randint(140, 400)
    
    # O'level grades
    grades = random.choices(list(olevel_scale.keys()), k=5)
    olevel_points = [olevel_scale[g] for g in grades]
    olevel_avg = sum(olevel_points)
    
    # O'level valid (all >= C6)
    olevel_valid = all(score >= 3 for score in olevel_points) and sittings <= 2
    
    # Screening score
    screening_score = calculate_screening(utme_score, grades)
    
    # Sittings
    sittings = random.choice([1, 2])
    sittings_valid = sittings <= 2
    
    # Admission logic
    if utme_score >= 140 and screening_score >= 50 and olevel_valid and sittings_valid:
        admitted = "admitted"
    else:
        admitted = "not admitted"
    
    data.append([
        faculty, department, utme_score, screening_score, olevel_valid,
        sittings, admitted, ", ".join(grades)
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Faculty", "Department", "UTME_Score", "Screening_Score",
    "Olevel_Valid", "Sittings", "Admission_Status", "Olevel_Grades"
])

# Save to CSV (force to Data folder in your project)
base_dir = r"C:\Users\USER\Desktop\ADMISSION-COMPASS\Admission-Compass-ML\Data"
os.makedirs(base_dir, exist_ok=True)

file_path = os.path.join(base_dir, "EKSU.csv")
df.to_csv(file_path, index=False)

print("Dataset saved successfully at:", file_path)
print("Preview:")
print(df.head())