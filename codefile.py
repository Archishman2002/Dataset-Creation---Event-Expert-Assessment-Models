pip install faker

from faker import Faker
import random
import json

fake = Faker()

parameters_data = [
  {"parameter_id": 1, "parameter_name": "Mathematics"},
  {"parameter_id": 2, "parameter_name": "Science"},
  { "parameter_id": 3, "parameter_name": "English Language and Literature" },
  { "parameter_id": 4, "parameter_name": "History" },
  { "parameter_id": 5, "parameter_name": "Computer Science" },
  { "parameter_id": 6, "parameter_name": "Foreign Language" },
  { "parameter_id": 7, "parameter_name": "Physical Education" },
  { "parameter_id": 8, "parameter_name": "Economics" },
  { "parameter_id": 9, "parameter_name": "Art and Design" },
  { "parameter_id": 10, "parameter_name": "Psychology" },
  { "parameter_id": 11, "parameter_name": "Research Skills" },
  { "parameter_id": 12, "parameter_name": "Analytical Thinking" },
  { "parameter_id": 13, "parameter_name": "Writing Proficiency" },
  { "parameter_id": 14, "parameter_name": "Critical Reading" },
  { "parameter_id": 15, "parameter_name": "Problem Solving in Academic Context" },
  { "parameter_id": 16, "parameter_name": "Data Analysis" },
  { "parameter_id": 17, "parameter_name": "Presentation Skills" },
  { "parameter_id": 18, "parameter_name": "Time Management for Studies" },
  { "parameter_id": 19, "parameter_name": "Collaborative Learning" },
  { "parameter_id": 20, "parameter_name": "Understanding and Applying Concepts" },
  { "parameter_id": 21, "parameter_name": "Communication Skills" },
  { "parameter_id": 22, "parameter_name": "Team Collaboration" },
  { "parameter_id": 23, "parameter_name": "Creativity" },
  { "parameter_id": 24, "parameter_name": "Leadership" },
  { "parameter_id": 25, "parameter_name": "Technical Proficiency" },
  { "parameter_id": 26, "parameter_name": "Attention to Detail" },
  { "parameter_id": 27, "parameter_name": "Critical Thinking" },
  { "parameter_id": 28, "parameter_name": "Environmental Science" },
  { "parameter_id": 29, "parameter_name": "Political Science" },
  { "parameter_id": 30, "parameter_name": "Sociology" },
  { "parameter_id": 31, "parameter_name": "Anthropology" },
  { "parameter_id": 32, "parameter_name": "Geography" },
  { "parameter_id": 33, "parameter_name": "Cultural Studies" },
  { "parameter_id": 34, "parameter_name": "Music Theory" },
  { "parameter_id": 35, "parameter_name": "Dance Performance" },
  { "parameter_id": 36, "parameter_name": "Drama and Theater Arts" },
  { "parameter_id": 37, "parameter_name": "Culinary Arts" },
  { "parameter_id": 38, "parameter_name": "Fashion Design" },
  { "parameter_id": 39, "parameter_name": "Digital Marketing" },
  { "parameter_id": 40, "parameter_name": "Entrepreneurship" },
  { "parameter_id": 41, "parameter_name": "Supply Chain Management" },
  { "parameter_id": 42, "parameter_name": "Public Speaking" },
  { "parameter_id": 43, "parameter_name": "Conflict Resolution" },
  { "parameter_id": 44, "parameter_name": "Machine Learning" },
  { "parameter_id": 45, "parameter_name": "Blockchain Technology" },
  { "parameter_id": 46, "parameter_name": "Augmented Reality" },
  { "parameter_id": 47, "parameter_name": "Space Exploration" },
  { "parameter_id": 48, "parameter_name": "Neuroscience" },
  { "parameter_id": 49, "parameter_name": "Bioinformatics" },
  { "parameter_id": 50, "parameter_name": "Medical Ethics" },
  { "parameter_id": 51, "parameter_name": "Cybersecurity" },
  { "parameter_id": 52, "parameter_name": "Quantum Physics" },
  { "parameter_id": 53, "parameter_name": "Astrophysics" },
  { "parameter_id": 54, "parameter_name": "Renewable Energy" },
  { "parameter_id": 55, "parameter_name": "Astronomy" },
  { "parameter_id": 56, "parameter_name": "Psychiatry" },
  { "parameter_id": 57, "parameter_name": "Public Health Policy" },
  { "parameter_id": 58, "parameter_name": "Cognitive Science" },
  { "parameter_id": 59, "parameter_name": "Human Rights Law" },
  { "parameter_id": 60, "parameter_name": "Financial Literacy" },
  { "parameter_id": 61, "parameter_name": "Artificial Intelligence Ethics" },
  { "parameter_id": 62, "parameter_name": "Media Studies" },
  { "parameter_id": 63, "parameter_name": "Environmental Ethics" },
  { "parameter_id": 64, "parameter_name": "Data Privacy" },
  { "parameter_id": 65, "parameter_name": "Genetics" },
  { "parameter_id": 66, "parameter_name": "Robotics" },
  { "parameter_id": 67, "parameter_name": "Game Development" },
  { "parameter_id": 68, "parameter_name": "User Experience Design" },
  { "parameter_id": 69, "parameter_name": "Behavioral Economics" },
  { "parameter_id": 70, "parameter_name": "Geopolitics" },
  { "parameter_id": 71, "parameter_name": "Futurism" },
  { "parameter_id": 72, "parameter_name": "Cryptography" },
  { "parameter_id": 73, "parameter_name": "Biochemistry" },
  { "parameter_id": 74, "parameter_name": "Educational Technology" },
  { "parameter_id": 75, "parameter_name": "Remote Sensing" },
  { "parameter_id": 76, "parameter_name": "Nanotechnology" },
  { "parameter_id": 77, "parameter_name": "Organizational Psychology" },
  { "parameter_id": 78, "parameter_name": "Natural Language Processing" },
  { "parameter_id": 79, "parameter_name": "Artificial Neural Networks" },
  { "parameter_id": 80, "parameter_name": "Virtual Reality" },
  { "parameter_id": 81, "parameter_name": "Ecology" },
  { "parameter_id": 82, "parameter_name": "Bioethics" },
  { "parameter_id": 83, "parameter_name": "Sustainable Development" },
  { "parameter_id": 84, "parameter_name": "Quantitative Finance" },
  { "parameter_id": 85, "parameter_name": "Agricultural Sciences" },
  { "parameter_id": 86, "parameter_name": "Climate Change Policy" },
  { "parameter_id": 87, "parameter_name": "Transportation Engineering" },
  { "parameter_id": 88, "parameter_name": "Ecological Conservation" },
  { "parameter_id": 89, "parameter_name": "Social Entrepreneurship" },
  { "parameter_id": 90, "parameter_name": "Public Relations" },
  { "parameter_id": 91, "parameter_name": "Behavioral Ecology" },
  { "parameter_id": 92, "parameter_name": "Investment Management" },
  { "parameter_id": 93, "parameter_name": "Digital Forensics" },
  { "parameter_id": 94, "parameter_name": "Cancer Research" },
  { "parameter_id": 95, "parameter_name": "Human-Computer Interaction" },
  { "parameter_id": 96, "parameter_name": "Art Restoration" },
  { "parameter_id": 97, "parameter_name": "Historical Preservation" },
  { "parameter_id": 98, "parameter_name": "Public Policy Analysis" },
  { "parameter_id": 99, "parameter_name": "Intercultural Communication" },
  { "parameter_id": 100, "parameter_name": "Music Production" },
  { "parameter_id": 101, "parameter_name": "Oceanography" },
  { "parameter_id": 102, "parameter_name": "Ethnomusicology" },
  { "parameter_id": 103, "parameter_name": "Entrepreneurial Finance" },
  { "parameter_id": 104, "parameter_name": "Human Anatomy" },
  { "parameter_id": 105, "parameter_name": "Political Philosophy" },
  { "parameter_id": 106, "parameter_name": "Marine Biology" },
  { "parameter_id": 107, "parameter_name": "Global Governance" },
  { "parameter_id": 108, "parameter_name": "Corporate Law" },
  { "parameter_id": 109, "parameter_name": "Neurolinguistics" },
  { "parameter_id": 110, "parameter_name": "Experimental Psychology" },
  { "parameter_id": 111, "parameter_name": "Forensic Science" },
  { "parameter_id": 112, "parameter_name": "Behavioral Genetics" },
  { "parameter_id": 113, "parameter_name": "Urban Planning" },
  { "parameter_id": 114, "parameter_name": "Chemical Engineering" },
  { "parameter_id": 115, "parameter_name": "Human Resource Management" },
  { "parameter_id": 116, "parameter_name": "Cognitive Neuroscience" },
  { "parameter_id": 117, "parameter_name": "Medical Imaging" },
  { "parameter_id": 118, "parameter_name": "Journalism Ethics" },
  { "parameter_id": 119, "parameter_name": "Aviation Technology" },
  { "parameter_id": 120, "parameter_name": "Renewable Resources Management" },
  { "parameter_id": 121, "parameter_name": "Quantitative Biology" },
  { "parameter_id": 122, "parameter_name": "Cultural Anthropology" },
  { "parameter_id": 123, "parameter_name": "Finance and Accounting" },
  { "parameter_id": 124, "parameter_name": "Social Policy Analysis" },
  { "parameter_id": 125, "parameter_name": "Sports Medicine" },
  { "parameter_id": 126, "parameter_name": "Environmental Ethics" },
  { "parameter_id": 127, "parameter_name": "Music Composition" },
  { "parameter_id": 128, "parameter_name": "Geospatial Analysis" },
  { "parameter_id": 129, "parameter_name": "Public Administration" },
  { "parameter_id": 130, "parameter_name": "Digital Anthropology" },
  { "parameter_id": 131, "parameter_name": "Consumer Behavior" },
  { "parameter_id": 132, "parameter_name": "Health Economics" },
  { "parameter_id": 133, "parameter_name": "Educational Psychology" },
  { "parameter_id": 134, "parameter_name": "Ethical Hacking" },
  { "parameter_id": 135, "parameter_name": "International Development" },
  { "parameter_id": 136, "parameter_name": "Media Psychology" },
  { "parameter_id": 137, "parameter_name": "Behavioral Ecology" },
  { "parameter_id": 138, "parameter_name": "Criminal Justice Reform" },
  { "parameter_id": 139, "parameter_name": "Climate Science" },
  { "parameter_id": 140, "parameter_name": "Artificial Life" },
  { "parameter_id": 141, "parameter_name": "Hospitality Management" },
  { "parameter_id": 142, "parameter_name": "Population Genetics" },
  { "parameter_id": 143, "parameter_name": "Public Health Informatics" },
  { "parameter_id": 144, "parameter_name": "Fashion Merchandising" },
  { "parameter_id": 145, "parameter_name": "Healthcare Administration" },
  { "parameter_id": 146, "parameter_name": "Transportation Planning" },
  { "parameter_id": 147, "parameter_name": "Corporate Social Responsibility" },
  { "parameter_id": 148, "parameter_name": "Applied Linguistics" },
  { "parameter_id": 149, "parameter_name": "Space Technology" },
  { "parameter_id": 150, "parameter_name": "Industrial-Organizational Psychology" },
  { "parameter_id": 151, "parameter_name": "Sports Psychology" },
  { "parameter_id": 152, "parameter_name": "Biomedical Engineering" },
  { "parameter_id": 153, "parameter_name": "Digital Sociology" },
  { "parameter_id": 154, "parameter_name": "Agricultural Economics" },
  { "parameter_id": 155, "parameter_name": "Geochemistry" },
  { "parameter_id": 156, "parameter_name": "Fashion Technology" },
  { "parameter_id": 157, "parameter_name": "Political Economy" },
  { "parameter_id": 158, "parameter_name": "Behavioral Finance" },
  { "parameter_id": 159, "parameter_name": "Medical Anthropology" },
  { "parameter_id": 160, "parameter_name": "Space Science" },
  { "parameter_id": 161, "parameter_name": "Design Thinking" },
  { "parameter_id": 162, "parameter_name": "Environmental Engineering" },
  { "parameter_id": 163, "parameter_name": "Ecotourism" },
  { "parameter_id": 164, "parameter_name": "Urban Sociology" },
  { "parameter_id": 165, "parameter_name": "Health Policy Analysis" },
  { "parameter_id": 166, "parameter_name": "Artificial Intelligence Ethics" },
  { "parameter_id": 167, "parameter_name": "Quantum Computing" },
  { "parameter_id": 168, "parameter_name": "Cognitive Robotics" },
  { "parameter_id": 169, "parameter_name": "Data Science Ethics" },
  { "parameter_id": 170, "parameter_name": "Digital Humanities" },
  { "parameter_id": 171, "parameter_name": "Microbiology" },
  { "parameter_id": 172, "parameter_name": "Social Media Analytics" },
  { "parameter_id": 173, "parameter_name": "Nuclear Physics" },
  { "parameter_id": 174, "parameter_name": "Fashion Journalism" },
  { "parameter_id": 175, "parameter_name": "Urban Design" },
  { "parameter_id": 176, "parameter_name": "Developmental Psychology" },
  { "parameter_id": 177, "parameter_name": "Political Communication" },
  { "parameter_id": 178, "parameter_name": "Financial Mathematics" },
  { "parameter_id": 179, "parameter_name": "Medical Ethics" },
  { "parameter_id": 180, "parameter_name": "Digital Art" }
]

# Function to get a random parameter with its weight
def get_random_parameter():
    parameter = random.choice(parameters_data)
    return {'parameter_id': parameter['parameter_id'], 'parameter_name': parameter['parameter_name']}

# ASSESSMENT DATA MODEL
def generate_assessment_data():
    return {
        'assessment_id': fake.unique.random_number(),
        'assessment_title': fake.job(),
        'assessment_short_desc': fake.text(),
        'assessment_desc': fake.text(),
        'assessment_parameters': [
            {'parameter_id': get_random_parameter()['parameter_id'], 'parameter_weight': random.randint(1, 10)}
            for _ in range(random.randint(1, 5))
        ],
    }

# EVENT DATA MODEL
def generate_event_data():
    return {
        'event_id': fake.unique.random_number(),
        'event_name': fake.company(),
        'event_short_desc': fake.text(),
        'event_desc': fake.text(),
        'event_topic': {'topic': fake.word(), 'desc': fake.text()},
        'event_parameters': [
            {'parameter_id': get_random_parameter()['parameter_id'], 'parameter_weight': random.randint(1, 10)}
            for _ in range(random.randint(1, 5))
        ],
    }

# EXPERT PROGRAM DATA MODEL
def generate_expert_program_data():
    return {
        'program_id': fake.unique.random_number(),
        'program_type': fake.random_element(elements=('Online', 'Offline')),
        'program_name': fake.catch_phrase(),
        'program_desc': fake.text(),
        'program_topics': [
            {'id': fake.unique.random_number(), 'topic': fake.word()}
            for _ in range(random.randint(1, 3))
        ],
        'program_parameters': [
            {'parameter_id': get_random_parameter()['parameter_id'], 'parameter_weight': random.randint(1, 10)}
            for _ in range(random.randint(1, 5))
        ],
    }

# Generate synthetic datasets
num_samples = 100

assessment_data = [generate_assessment_data() for _ in range(num_samples)]
event_data = [generate_event_data() for _ in range(num_samples)]
expert_program_data = [generate_expert_program_data() for _ in range(num_samples)]

print("ASSESSMENT DATA:")
for assessment in assessment_data:
    print(f"Assessment ID: {assessment['assessment_id']}")
    print(f"Assessment Title: {assessment['assessment_title']}")
    print(f"Assessment Short Description: {assessment['assessment_short_desc']}")
    print(f"Assessment Description: {assessment['assessment_desc']}")
    print("Assessment Parameters:")
    for param in assessment['assessment_parameters']:
        print(f"  Parameter ID: {param['parameter_id']}, Weight: {param['parameter_weight']}")
    print("\n")


print("EVENT DATA:")
for event in event_data:
    print(f"Event ID: {event['event_id']}")
    print(f"Event Name: {event['event_name']}")
    print(f"Event Short Description: {event['event_short_desc']}")
    print(f"Event Description: {event['event_desc']}")
    print(f"Event Topic: {event['event_topic']['topic']}")
    print(f"Event Topic Description: {event['event_topic']['desc']}")
    print("Event Parameters:")
    for param in event['event_parameters']:
        print(f"  Parameter ID: {param['parameter_id']}, Weight: {param['parameter_weight']}")
    print("\n")


print("EXPERT PROGRAM DATA:")
for program in expert_program_data:
    print(f"Program ID: {program['program_id']}")
    print(f"Program Type: {program['program_type']}")
    print(f"Program Name: {program['program_name']}")
    print(f"Program Description: {program['program_desc']}")
    print("Program Topics:")
    for topic in program['program_topics']:
        print(f"  Topic ID: {topic['id']}, Topic: {topic['topic']}")
    print("Program Parameters:")
    for param in program['program_parameters']:
        print(f"  Parameter ID: {param['parameter_id']}, Weight: {param['parameter_weight']}")
    print("\n")

import csv

# Function to write data to CSV
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        for row in data:
            writer.writerow(row)

# Export ASSESSMENT DATA to CSV
assessment_csv_filename = 'assessment_data.csv'
write_to_csv(assessment_data, assessment_csv_filename)
print(f"ASSESSMENT DATA written to {assessment_csv_filename}")

# Export EVENT DATA to CSV
event_csv_filename = 'event_data.csv'
write_to_csv(event_data, event_csv_filename)
print(f"EVENT DATA written to {event_csv_filename}")

# Export EXPERT PROGRAM DATA to CSV
expert_program_csv_filename = 'expert_program_data.csv'
write_to_csv(expert_program_data, expert_program_csv_filename)
print(f"EXPERT PROGRAM DATA written to {expert_program_csv_filename}")

from google.colab import files

# Function to download a file
def download_file(filename):
    files.download(filename)

# Download ASSESSMENT DATA CSV
download_file(assessment_csv_filename)

# Download EVENT DATA CSV
download_file(event_csv_filename)

# Download EXPERT PROGRAM DATA CSV
download_file(expert_program_csv_filename)
