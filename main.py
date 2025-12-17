import pygame
import cv2
from ultralytics import YOLO
from add import markup, search, voiceover

# Load the YOLO model and fuse layers
model = YOLO("best.pt")
model.fuse()

# Initialize the pygame mixer
pygame.mixer.init()

# Set up video capture and voiceover activation
cap = cv2.VideoCapture(1)
voiceover.activate()

# Play the initial music
pygame.mixer.music.load("voice/Start.mp3")
pygame.mixer.music.play()

last_namber = -1  # To track the last played sound

while True:
    # Process webcam and detect objects
    centr = search.process_webcam_with_detection_low(model, cap)

    if centr:
        area_counts = {}  # Dictionary to count centers in each area

        for center in centr:
            point = center[0]  # Assuming center[0] is the (x, y) point
            area, n = markup.check_point_in_shapes(point, center[1])  # Get area for the point

            if area:  # If a valid area is returned
                area_counts[area] = area_counts.get(area, 0) + 1  # Increment area count

        # Find the area with the maximum count
        if area_counts:
            max_area = max(area_counts, key=area_counts.get)
            max_count = area_counts[max_area]  # Get count for this area

            namber = markup.find_shape_index_by_text(max_area)

            if namber is not None and last_namber != namber:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(f"voice/{namber}.mp3")
                pygame.mixer.music.play()
                last_namber = namber

    else:
        pygame.mixer.music.stop()
        last_namber = -1

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
