import cv2
import map

def find_best_c_value(gray_frame):
    best_c_value = 0
    best_score = float('-inf')

    for c_value in range(1, 16):
        # Apply adaptive thresholding
        thresh = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, c_value)

        # Evaluate the clarity of lines (you may adjust this scoring metric)
        score = cv2.Canny(thresh, 75, 175).mean()

        # Update the best parameters if the current result is better
        if score > best_score:
            best_score = score
            best_c_value = c_value                           

    return best_c_value

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the best C value
    best_c = find_best_c_value(gray)

    # Apply adaptive thresholding with the best C value
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, best_c)

    # Display the original and thresholded frames
    cv2.imshow('Original', frame)
    cv2.imshow('Adaptive Threshold', thresh)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
