#Federal University Oye Ekiti (FUOYE)
from pathlib import Path
import os
import random
import pandas as pd

#Faculties and Departments
departments = {
    "Arts": [
        "Theatre and Media Arts", " English and Literary Studies", 
        "History and International Studies","Linguistics and Language" 
    ],
    "Agriculture": [
        "Agricultural Economics and Extension", "Animal Production and Health", "Crop Science and Horticulture",
        "Fisheries and Aquaculture", "Food Science and Technology", "Hospitality and Tourism Management",
        "Soil Science and Land Resources Management", "Water Resources Management and Agrometeorology"
    ],
    "Basic Medical Science": [
        "Anatomy", "Medical Laboratory Science", "Nursing Science", "Physiology", "Radiology and Radiography"
    ],
    "Education": [
        "Health Education", "Human Kinetics", "Library and Information Science", 
        "Biology Education", "Chemistry Education", "Mathematics Education", "Physics Education", 
        "Guidance and Counselling"
    ],
    "Engineering": [
        "Agricultural and Bio-Resources Engineering", "Civil Engineering", "Computer Engineering",
        "Electrical and Electronics Engineering", "Mechanical Engineering", "Mechatronics Engineering",
        "Meterials and Metallurgical Engineering"
    ],
    "Environmental Design and Management": [
        "Architecture", "Building", "Estate Management", "Quantity Surveying", "Survey and Geo-informatics",
        "Urban and Regional Planning"
    ],
    "Management Sciences": [
        "Accounting", "Finance", "Business Administration", "Public Administration"
    ],
    "Science": [
        "Biochemistry", "Computer Science", "Microbiology", "Botany", "Zoology", "Chemistry", 
        "Geology", "Physics", "Mathematics", "Statistics", "Industrial Chemistry"
    ],
    "Pharmacy": [
        "Doctor of Pharmacy"
    ],
    "Law":[
        "Law"
    ],
    "Communications and Media Studies": [
        "Mass Communication", "Pulic Relations", "Journalism", "Broadcasting"
    ],
    "Social Sciences": [
        "Criminology and Security Studies", "Economics", "Political Science", 
        "Sociology", "Demography and Social Statistics", "Geography", "Psychology"
    ],
    "College of Medicine": [
        "Medicine and Surgery"
    ]

}

# o'level grading scale
olevel_scale = {
    'A1': 6, 'B2': 5, 'B3': 4, 'C4': 3,
    'C5': 2, 'C6': 1
}

#UTME Departmental Cut-offs (UTME Cut-Off)
UTME_CUTOFFS = {
    "Theatre and Media Arts": 200,
    "English and Literary Studies": 200,
    "History and International Studies": 180,
    "Linguistics and Languages": 180,

    "Anatomy": 180,
    "Medical Laboratory Science": 200,
    "Nursing": 220,
    "Physiology": 180,
    "Radiology and Radiography": 200,

    "Agricultural and Bio-Resources Engineering": 160,
    "Civil Engineering": 200,
    "Computer Engineering": 200,
    "Electrical and Electronics Engineering": 200,
    "Mechanical Engineering": 200,
    "Mechatronics Engineering": 220,
    "Metallurgical and Materials Engineering": 160,

    "Architecture": 210,
    "Building": 170,
    "Estate Management": 160,
    "Quantity Surveying": 170,
    "Surveying and Geoinformatics": 160,

    "Accounting": 200,
    "Finance": 160,
    "Business Administration": 200,
    "Public Administration": 160,

    "Biochemistry": 180,
    "Computer Science": 200,
    "Microbiology": 180,

    "Doctor of Pharmacy": 240,
    "Law": 240,
    "Mass Communication": 220,

    "Criminology and Security Studies": 200,
    "Economics": 180,
    "Political Science": 180,
    "Sociology": 160,

    "Medicine and Surgery": 260
}

DEFAULT_UTME_CUTOFF = 150

#Departmental Aggregate Cut-Offs
AGGREGATE_CUTOFFS = {
    "Agricultural Economics and Extension": 57.8,
    "Animal Production and Health": 61.3,
    "Crop Science and Horticulture": 57.3,
    "Fisheries and Aquaculture": 50.3,
    "Food Science and Technology": 58.0,
    "Hospitality and Tourism Management": 58.45,

    "English and Literary Studies": 66.3,
    "History and International Studies": 67.8,
    "Linguistics and Languages": 65.3,
    "Theatre and Media Arts": 65.8,

    "Anatomy": 63.3,
    "Medical Laboratory Science": 72.3,
    "Nursing": 74.6,
    "Physiology": 61.5,
    "Radiology and Radiography": 71.3,

    "Mass Communication": 66.3,
    "Public Relations": 65.0,
    "Journalism": 64.0,
    "Broadcasting": 64.0,
    
    "Computer Science": 65.3,

    "Civil Engineering": 65.0,
    "Computer Engineering": 64.3,
    "Electrical and Electronics Engineering": 63.3,
    "Mechanical Engineering": 65.0,
    "Mechatronics Engineering": 65.0,
    "Agricultural and Bio-Resources Engineering": 55.0,

    "Architecture": 66.25,
    "Building": 57.5,
    "Estate Management": 57.5,
    "Quantity Surveying": 60.5,
    "Surveying andd Geo-informatics": 56.0,
    "Urban and Regional Planning": 56.0,

    "Biology Education": 55.0,
    "Chemistry Education": 55.0,
    "Mathematics Education": 55.5,
    "Physics Education": 53.6,
    "Guidance and Counselling": 59.05,
    "Health Education": 57.95,
    "Human Kinetics": 54.9,
    "Library and Information Science": 64.5,

    "Biochemistry": 63.75,
    "Microbiology": 65.75,
    "Pharmacy": 71.75,
    "Botany": 53.5,
    "Zoology": 55.5,
    "Chemistry": 62.5,
    "Geology": 59.5,
    "Industrial Chemistry": 60.5,
    "Mathematics":55.5,
    "Physics": 56.5,
    "Statistics": 54.5,
    "Demography and Social Statistics": 60.5,
    "Economics": 63.75,
    "Geogrsphy": 58.5,
    "Political Science": 62.5,
    "Psychology": 64.5,
    "Sociology": 63.95
}

DEFAULT_AGGREGATE_CUTOFF = 55.0

#Aggregate Score Calculator
def calculate_aggregate(utme, grades, sittings):
    utme_score = (utme / 400) * 60

    olevel_points = sum(olevel_scale[g] for g in grades)

    if sittings == 1:
        olevel_points += 10

    return round(utme_score + olevel_points, 2)

#Dataset Generation
num_applicants = 5000
data = []

for _ in range(num_applicants):
    faculty = random.choice(list(departments.keys()))
    department = random.choice(departments[faculty])

    utme_score = random.randint(140, 350)
    sittings = random.choice([1, 2])

    grades = random.choices(list(olevel_scale.keys()), k=5)
    olevel_points = [olevel_scale[g] for g in grades]

    aggregate_score = calculate_aggregate(utme_score, grades, sittings)

    utme_cutoff = UTME_CUTOFFS.get(department, DEFAULT_UTME_CUTOFF)
    aggregate_cutoff = AGGREGATE_CUTOFFS.get(department, DEFAULT_AGGREGATE_CUTOFF)

    olevel_valid = all(score >= 1 for score in olevel_points) and sittings <= 2
    utme_valid = utme_score >= utme_cutoff

    if utme_valid and olevel_valid and aggregate_score >= aggregate_cutoff:
        admitted = "admitted"
    else:
        admitted = "not admitted"

    data.append([
        faculty,
        department,
        utme_score,
        utme_cutoff,
        aggregate_score,
        aggregate_cutoff,
        olevel_valid,
        sittings,
        admitted,
        ", ".join(grades)
    ])

# ==============================
# Create DataFrame
# ==============================
df = pd.DataFrame(data, columns=[
    "Faculty",
    "Department",
    "UTME_Score",
    "UTME_Cutoff",
    "Aggregate_Score",
    "Aggregate_Cutoff",
    "Olevel_Valid",
    "Sittings",
    "Admission_Status",
    "Olevel_Grades"
])

# ==============================
# Save to Data Folder
# ==============================
ROOT_DIR = Path(__file__).resolve().parent.parent
base_dir = ROOT_DIR / "Data"
os.makedirs(base_dir, exist_ok=True)

file_path = os.path.join(base_dir, "FUOYE.csv")
df.to_csv(file_path, index=False)

print("FUOYE dataset saved successfully at:", file_path)
print("Preview:")
print(df.head())