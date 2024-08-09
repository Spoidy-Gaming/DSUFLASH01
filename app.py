from flask import Flask, request, jsonify, render_template
import re
import sqlite3
from twilio.rest import Client

app = Flask(__name__)

account_sid = 'ACd99b87f144e524f1f3f85c00b7a3aa9a'
auth_token = '075cd9dd1401bd906fb8455dcbd44a19'
twilio_phone_number = 'whatsapp:+14155238886'  # Replace with your Twilio number
twilio_client = Client(account_sid, auth_token)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('college_chatbot.db')
    cursor = conn.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    conn.close()
    return (result[0] if result else None) if one else result

@app.route('/send_whatsapp', methods=['POST'])
def send_whatsapp():
    phone_number = request.form.get('phone_number')
    message_body = request.form.get('message')
    try:
        message_sid = send_whatsapp_message(phone_number, message_body)
        return jsonify({"status": "Message sent", "sid": message_sid})
    except Exception as e:
        return jsonify({"status": "Failed to send message", "error": str(e)})

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    query = request.form.get('query').lower()
    response = get_response(query)
    return jsonify(response)

if __name__ == '_main_':
    app.run(debug=True)
