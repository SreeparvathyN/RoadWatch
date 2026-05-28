from flask import Flask, render_template, request
from detection import detect_road_damage
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

# =========================================
# Folders
# =========================================

UPLOAD_FOLDER = 'static/uploads/images'
RESULT_FOLDER = 'static/results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# =========================================
# Home Page
# =========================================

@app.route('/')
def home():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

# =========================================
# About Page
# =========================================

@app.route('/about')
def about():
    return render_template('about.html')

# =========================================
# Dashboard Page
# =========================================

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('roadwatch.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT image_name, damage_type, severity, status, date_time
        FROM complaints
        ORDER BY id DESC
    """)

    complaints = cursor.fetchall()
    conn.close()

    return render_template('dashboard.html', complaints=complaints)

# =========================================
# Upload + Detection Route
# =========================================

@app.route('/upload', methods=['POST'])
def upload():

    image = request.files.get('image')

    if not image or image.filename == '':
        return "No image selected"

    # Save input image
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # Output image path
    output_path = os.path.join(RESULT_FOLDER, image.filename)

    # Run AI detection
    result = detect_road_damage(image_path, output_path)

    # Get results FIRST (IMPORTANT FIX)
    crack_count = result.get('crack_count', 0)
    pothole_count = result.get('pothole_count', 0)
    severity = result.get('severity', 'Unknown')

    # Decide damage type
    damage_type = "Road Damage"

    if pothole_count > crack_count:
        damage_type = "Pothole"
    elif crack_count > pothole_count:
        damage_type = "Crack"

    # Save to database
    conn = sqlite3.connect('roadwatch.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO complaints
        (image_name, damage_type, severity, status, date_time)
        VALUES (?, ?, ?, ?, ?)
    """, (
        image.filename,
        damage_type,
        severity,
        "Pending",
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ))

    conn.commit()
    conn.close()

    # Details for UI
    damage_details = f"""
Cracks Detected: {crack_count}
Potholes Detected: {pothole_count}
"""

    return render_template(
        'result.html',
        image_path='/' + output_path,
        severity=severity,
        damage_details=damage_details
    )

# =========================================
# Run App
# =========================================

if __name__ == '__main__':
    app.run(debug=True)