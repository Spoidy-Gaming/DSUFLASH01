from flask import Flask, request, jsonify
import sqlite3

app = Flask(_name_)

def connect_db():
    conn = sqlite3.connect('college_chatbot.db')  # Name of the SQLite database file
    return conn

# Function to respond to various queries
def respond_to_query(query):
    query = query.lower()
    conn = connect_db()
    cursor = conn.cursor()

    if query in ["course list", "courses", "course"]:
        cursor.execute("SELECT course_name FROM courses")
        courses = cursor.fetchall()
        course_list = ', '.join([course[0] for course in courses])
        return f"DSU offers the following courses: {course_list}"

    elif query in ["hostel fee", "hostel"]:
        cursor.execute("SELECT hostel_name, fee FROM hostel")
        hostels = cursor.fetchall()
        return ', '.join([f"{hostel[0]}: {hostel[1]}" for hostel in hostels])

    elif query in ["location", "where is dsu", "address"]:
        cursor.execute("SELECT address_details FROM address")
        address_info = cursor.fetchone()
        return address_info[0] if address_info else "Address information not available."

    elif query in ["infrastructure", "facilities"]:
        cursor.execute("SELECT details FROM infrastructure")
        infrastructure = cursor.fetchone()
        return infrastructure[0] if infrastructure else "Infrastructure details not available."

    elif query in ["contact", "how to contact", "contact details"]:
        cursor.execute("SELECT phone, email FROM contact")
        contact_info = cursor.fetchone()
        return f"You can contact DSU at {contact_info[0]} or email us at {contact_info[1]}"

    elif query in ["application link", "apply", "admission link"]:
        cursor.execute("SELECT link FROM application_link")
        app_link = cursor.fetchone()
        return app_link[0] if app_link else "Application link not available."

    elif query in ["building images", "campus images", "pictures"]:
        cursor.execute("SELECT building_name, image_link FROM building_images")
        buildings = cursor.fetchall()
        return ', '.join([f"{building[0]}: {building[1]}" for building in buildings])

    # Additional queries for course facilities, hostel facilities, map link, and specific building images
    elif 'course facility' in query:
        course_name = query.replace('course facility', '').strip()
        cursor.execute("SELECT facility FROM course_facilities WHERE LOWER(course_name) = ?", (course_name.lower(),))
        facility = cursor.fetchone()
        return facility[0] if facility else "Course facility information not available."

    elif query in ["hostel facilities", "hostel"]:
        cursor.execute("SELECT hostel_name, facilities FROM hostel")
        hostels = cursor.fetchall()
        return ', '.join([f"{hostel[0]}: {hostel[1]}" for hostel in hostels])

    elif 'course fee' in query:
        course_name = query.replace('course fee', '').strip()
        cursor.execute("SELECT fee FROM courses WHERE LOWER(course_name) = ?", (course_name.lower(),))
        fee = cursor.fetchone()
        return fee[0] if fee else "Course fee information not available."
    
    elif query in ["map link", "location map"]:
        cursor.execute("SELECT map_link FROM map")
        map_info = cursor.fetchone()
        return map_info[0] if map_info else "Map link not available."

    elif 'academic block' in query:
        cursor.execute("SELECT image_link FROM building_images WHERE building_name = 'Academic Block'")
        image_link = cursor.fetchone()
        return image_link[0] if image_link else "Academic Block image not available."
    elif 'hospital block' in query:
        cursor.execute("SELECT image_link FROM building_images WHERE building_name = 'Hospital Block'")
        image_link = cursor.fetchone()
        return image_link[0] if image_link else "Hospital Block image not available."
    elif 'hostel block' in query:
        cursor.execute("SELECT image_link FROM building_images WHERE building_name = 'Hostel Block'")
        image_link = cursor.fetchone()
        return image_link[0] if image_link else "Hostel Block image not available."
    elif 'engineering block' in query:
        cursor.execute("SELECT image_link FROM building_images WHERE building_name = 'Engineering Block'")
        image_link = cursor.fetchone()
        return image_link[0] if image_link else "Engineering Block image not available."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

    conn.close()

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_text = data.get('query', '').strip()

    # Get the response from the respond_to_query function
    response = respond_to_query(query_text)

    return jsonify({'response': response})

if _name_ == '_main_':
    app.run(debug=True)
