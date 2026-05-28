import cv2
import numpy as np
import os

def detect_road_damage(image_path, output_path):

    # Read Image
    img = cv2.imread(image_path)

    # If image not loaded
    if img is None:

        return {
            "severity": "Unknown",
            "crack_count": 0,
            "pothole_count": 0
        }

    # Copy image for drawing
    annotated = img.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    # Blur image to reduce noise
    blur = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )

    # Edge Detection
    edges = cv2.Canny(
        blur,
        30,
        100
    )

    # Dilate edges to make cracks thicker
    kernel = np.ones((3,3), np.uint8)

    dilated = cv2.dilate(
        edges,
        kernel,
        iterations=1
    )

    # Find contours
    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    print("Contours Found:", len(contours))

    crack_count = 0
    pothole_count = 0

    # Detect damage
    for cnt in contours:

        area = cv2.contourArea(cnt)

        # Ignore tiny noise
        if area < 30:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        aspect_ratio = w / h

        # Crack Detection
        if aspect_ratio > 1.8:

            label = "Crack"

            color = (0,255,255)

            crack_count += 1

        # Pothole Detection
        else:

            label = "Pothole"

            color = (0,0,255)

            pothole_count += 1

        # Draw rectangle
        cv2.rectangle(
            annotated,
            (x,y),
            (x+w,y+h),
            color,
            2
        )

        # Put label
        cv2.putText(
            annotated,
            label,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    # Total damages
    total_damage = crack_count + pothole_count

    # Severity Logic
    if total_damage == 0:

        severity = "No Damage"

    elif total_damage <= 2:

        severity = "Low"

    elif total_damage <= 5:

        severity = "Medium"

    else:

        severity = "High"

    # Save output image
    cv2.imwrite(
        output_path,
        annotated
    )

    # Return results
    return {

        "severity": severity,

        "crack_count": crack_count,

        "pothole_count": pothole_count
    }