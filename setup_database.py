import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('college_chatbot.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create tables with updated structure for the courses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    school TEXT NOT NULL,
    duration TEXT NOT NULL,
    fee TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS infrastructure (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    details TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS building_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    building_name TEXT NOT NULL,
    image_link TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS course_facilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    facility TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS hostel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hostel_name TEXT NOT NULL,
    facility TEXT NOT NULL,
    fee TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS address (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address_details TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS application_link (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS map (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    map_link TEXT NOT NULL
);
''')

# Insert updated data into the courses table
courses_data = [
    ('B.Tech - Computer Science and Engineering', 'School of Engineering & Technology', '4 years', '₹75,000-₹1,12,500 per semester'),
    ('B.Tech - Artificial Intelligence & Data Science', 'School of Engineering & Technology', '4 years', '₹75,000-₹1,12,500 per semester'),
    ('B.Tech - Information Technology', 'School of Engineering & Technology', '4 years', '₹75,000-₹1,12,500 per semester'),
    ('B.Tech - Mechanical Engineering', 'School of Engineering & Technology', '4 years', '₹50,000 per semester'),
    ('B.A LL.B. (Hons.)', 'School of Law', '5 years', '₹1,00,000 per semester'),
    ('B.B.A LL.B. (Hons.)', 'School of Law', '5 years', '₹1,00,000 per semester'),
    ('B.Com LL.B. (Hons.)', 'School of Law', '5 years', '₹87,500 per semester'),
    ('B.Sc Nursing', 'School of Nursing', '4 years', '₹2,00,000 per year'),
    ('B.P.T. Bachelor of Physiotherapy', 'School of Physiotherapy', '4 years', '₹1,50,000 per year'),
    ('M.P.T (Orthopaedics, Cardiopulmonary Sciences, Neurological Sciences, Sports)', 'School of Physiotherapy', '2 years', '₹1,50,000 per year'),
    ('B.Sc (Hons.) Agriculture', 'School of Agricultural Sciences', '4 years', '₹87,500 per semester'),
    ('B.Sc (Hons.) Horticulture', 'School of Agricultural Sciences', '4 years', '₹50,000 per semester'),
    ('B.Sc (Various specializations)', 'School of Allied Health Sciences', '3 years', '₹1,00,000 - ₹2,00,000 per year'),
    ('M.Sc (Various specializations)', 'School of Allied Health Sciences', '2 years', '₹1,00,000 - ₹2,00,000 per year'),
    ('B.Pharm', 'School of Pharmacy', '4 years', '₹1,75,000 per year'),
    ('D.Pharm', 'School of Pharmacy', '2 years', '₹1,00,000 per year'),
    ('B.B.A.', 'School of Management', '3 years', '₹20,000 per semester'),
    ('B.H.A.', 'School of Management', '3 years', '₹50,000 per semester'),
    ('M.B.A.', 'School of Management', '2 years', '₹75,000 per semester'),
    ('M.H.A.', 'School of Management', '2 years', '₹50,000 per semester'),
    ('B.Arch', 'School of Architecture', '5 years', '₹50,000 per semester'),
    ('B.Com', 'School of Arts and Science', '3 years', '₹20,000 - ₹30,000 per semester'),
    ('B.C.A.', 'School of Arts and Science', '3 years', '₹20,000 - ₹30,000 per semester'),
    ('B.Sc (Computer Science, AI & DS, IT)', 'School of Arts and Science', '3 years', '₹20,000 - ₹30,000 per semester'),
    ('MCA', 'School of Arts and Science', '2 years', '₹50,000 per semester')
]

# Insert data into the courses table
cursor.executemany('''
INSERT INTO courses (name, school, duration, fee) VALUES (?, ?, ?, ?);
''', courses_data)

# Insert updated data into the course facilities table
course_facilities_data = [
    ('B.Tech - Computer Science and Engineering', 'Advanced Programming Labs'),
    ('B.Tech - Artificial Intelligence & Data Science', 'AI & Data Science Labs'),
    ('B.Tech - Information Technology', 'IT Infrastructure and Labs'),
    ('B.Tech - Mechanical Engineering', 'State-of-the-Art Workshops'),
    ('B.Sc Nursing', 'Modern Nursing Labs'),
    ('B.P.T. Bachelor of Physiotherapy', 'Physiotherapy Equipment'),
    ('B.Pharm', 'Pharmacy Labs and Equipment'),
    ('B.Arch', 'Design Studios'),
    ('B.Com', 'Commerce Labs'),
    ('B.C.A.', 'Computer Labs')
]

# Insert data into the course facilities table
cursor.executemany('''
INSERT INTO course_facilities (course_name, facility) VALUES (?, ?);
''', course_facilities_data)

# Insert data into other tables
cursor.execute('''
INSERT INTO infrastructure (details) VALUES 
('Modern classrooms, well-equipped labs, libraries, and sports facilities');
''')

cursor.execute('''
INSERT INTO contact (phone, email) VALUES 
('+91-1234567890', 'info@dsu.edu');
''')

cursor.execute('''
INSERT INTO building_images (building_name, image_link) VALUES 
('Academic Block', 'static/images/academic_block.jpeg'),
('Hospital Block', 'static/images/hospital_block.jpeg'),
('Hostel Block', 'static/images/hostel_block.jpeg'),
('Engineering Block', 'static/images/engineering_block.jpeg');
''')

cursor.execute('''
INSERT INTO hostel (hostel_name, facility, fee) VALUES 
('Boys Hostel', 'Wi-Fi, 24/7 Security, Gym', '₹50,000 per year'),
('Girls Hostel', 'Wi-Fi, 24/7 Security, Gym', '₹50,000 per year');
''')

cursor.execute('''
INSERT INTO address (address_details) VALUES 
('NH-45, Trichy Chennai Trunk Road Samayapuram, near Samayapuram Toll Plaza, Tiruchirappalli, Tamil Nadu 621112.');
''')

cursor.execute('''
INSERT INTO application_link (link) VALUES 
('https://admissions.dsuniversity.ac.in/');
''')

cursor.execute('''
INSERT INTO map (map_link) VALUES 
('https://maps.app.goo.gl/7Y2khEtZVPEZ2ZNK7');
''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Database setup complete.")
