import os
import random
import pandas as pd

# Faculties and departments for UNILAG
departments = {
    "Arts": [
        "Creative Arts", "English", "French", "Russian", "History & Strategic Studies",
        "Linguistic Igbo/Yoruba", "Chinese", "Philosophy",
        "Christian Religious Studies", "Islamic Religious Studies"
    ],
    "Basic Medical Sciences": ["Pharmacology", "Physiology", "Medical Laboratory Science"],
    "Clinical Sciences": ["Medicine and Surgery", "Nursing", "Physiotherapy", "Radiography"],
    "Dental Sciences": ["Dentistry"],
    "Education": [
        "Adult Education", "Education Economics", "Business Education", "Education Islamic Religious Studies",
        "Education Igbo", "Education English", "Early Childhood Education", "Education Yoruba",
        "Education French", "Education History", "Education Christian Religious Studies",
        "Education Geography", "Educational Administration", "Educational Foundations", "Health Education",
        "Human Kinetics Education", "Education Biology", "Education Chemistry", "Education Home Economics",
        "Integrated Science Education", "Education Mathematics", "Education Physics", "Technology Education"
    ],
    "Engineering": [
        "Biomedical Engineering", "Chemical & Petroleum Engineering", "Civil & Environmental Engineering",
        "Computer Engineering", "Electrical & Electronics Engineering", "Mechanical Engineering",
        "Metallurgical & Material Engineering", "Surveying & Geoinformatics Engineering", "Systems Engineering"
    ],
    "Environmental Sciences": [
        "Architecture", "Building", "Estate Management", "Quantity Surveying", "Urban & Regional Planning"
    ],
    "Law": ["Law"],
    "Management Sciences": ["Accounting", "Actuarial Science", "Insurance", "Business Administration", "Finance", "IRPM"],
    "Pharmacy": ["Pharmacy"],
    "Science": [
        "Botany", "Cell Biology & Genetics", "Chemistry", "Computer Science", "Geology", "Geophysics",
        "Marine Biology", "Fisheries", "Mathematics", "Industrial Mathematics", "Statistics", "Microbiology",
        "Physics", "Zoology"
    ],
    "Social Sciences": ["Economics", "Geography", "Mass Communication", "Political Science", "Psychology", "Social Work", "Sociology"]
}

# O'level grading scale for UNILAG
olevel_scale = {
    "A1": 4.0, "B2": 3.6, "B3": 3.2,
    "C4": 2.8, "C5": 2.4, "C6": 2.0
}

# Merit cut-off marks (2021/2022 sample values from UNILAG website – extend with full PDF data)
unilag_cutoffs = {
    "Medicine and Surgery": 80.8,
    "Dentistry": 77.4,
    "Nursing": 70.875,
    "Pharmacy": 76.125,
    "Medical Laboratory Science": 74.675,
    "Pharmacology": 72.625,
    "Physiology": 71.55,
    "Physiotherapy": 73.75,
    "Radiography": 72.525,
    "Law": 68.65,
    "Accounting": 74.1,
    "Business Administration": 68.65,
    "Actuarial Science": 61.875,
    "Finance": 68.9,
    "Insurance": 67.125,
    "ER & HRM": 66.95,
    "Computer Science": 71.75,
    "Mass Communication": 72.35,
    "Economics": 69.95,
    "Political Science": 68.6,
    "Psychology": 67.4,
    "Sociology": 66.15,
    "Creative Arts": 67.05,
    "English": 68.175,
    "French": 66.55,
    "Russian": 67.65,
    "History & Strategic Studies": 68.6,
    "Linguistic Igbo/Yoruba": 61.175,
    "Chinese": 66.7,
    "Philosophy": 67.4,
    "Christian Religious Studies": 61.625,
    "Islamic Religious Studies": 60.225,
    # Default fallback
    "Other": 50
}

# Function to get cutoff for department
def get_cutoff(department):
    return unilag_cutoffs.get(department, unilag_cutoffs["Other"])

# Function to calculate UNILAG aggregate
def calculate_aggregate(utme, grades, post_utme):
    utme_score = utme / 8  # max 50
    olevel_points = sum(olevel_scale[g] for g in grades)  # max 20
    post_utme_score = post_utme  # raw score, max 30
    return round(utme_score + olevel_points + post_utme_score, 2)

# Generate dataset
num_applicants = 10000
data = []

for _ in range(num_applicants):
    # Random faculty & department
    faculty = random.choice(list(departments.keys()))
    department = random.choice(departments[faculty])
    
    # UTME score (≥200 for UNILAG)
    utme_score = random.randint(200, 400)
    
    # O'level grades (5 subjects, valid if all ≥ C6)
    grades = random.choices(list(olevel_scale.keys()), k=5)
    olevel_points = sum(olevel_scale[g] for g in grades)
    olevel_valid = all(olevel_scale[g] >= 2.0 for g in grades)
    
    # Post-UTME (0–30 raw)
    post_utme = random.randint(0, 30)
    
    # Aggregate
    aggregate = calculate_aggregate(utme_score, grades, post_utme)
    
    # Admission logic (basic)
    #if utme_score >= 200 and post_utme >= 12 and aggregate >= 50 and olevel_valid:
     #   admitted = "admitted"
    #else:
     #   admitted = "not admitted"
    cutoff = get_cutoff(department)
    if utme_score < 200 or post_utme < 12 or aggregate < 50 or not olevel_valid:
        status = "not admitted"
    elif aggregate >= cutoff:
        status = "admitted"
    else:
        status = "considered"
    
    data.append([
        faculty, department, utme_score, ", ".join(grades),
        post_utme, aggregate, cutoff, status # or admitted
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Faculty", "Department", "UTME_Score", "Olevel_Grades",
    "Post_UTME_Score", "Aggregate", "Cutoff", "Admission_Status"
])

# Save to CSV
base_dir = r"C:\Users\USER\Desktop\ADMISSION-COMPASS\Admission-Compass-ML\Data"
os.makedirs(base_dir, exist_ok=True)
file_path = os.path.join(base_dir, "UNILAG.csv")
df.to_csv(file_path, index=False)

print("Dataset saved successfully at:", file_path)
print("Preview:")
print(df.head())
