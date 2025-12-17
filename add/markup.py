import cv2
import json

# Path to the JSON file containing shape data
json_filename = "1.json"
kf = 58  # Offset value for drawing shapes


def load_shapes():
    # Load shapes from the JSON file
    with open(json_filename, 'r') as f:
        return json.load(f)


def find_shape_index_by_text(text):
    # Find the index of a shape by its text label
    shapes = load_shapes()
    for index, shape in enumerate(shapes):
        if shape["text"] == text:
            return index
    return None  # Return None if the shape is not found


def is_point_in_rectangle(point, shape):
    # Check if a point is inside a rectangle defined by a shape
    x, y = point
    return (shape['x'] <= x <= shape['x'] + shape['width'] and
            shape['y'] - kf <= y <= shape['y'] + shape['height'] - kf)


def draw_shapes_on_frame(frame):
    # Draw shapes on the given frame
    shapes = load_shapes()
    for shape in shapes:
        if shape['type'] == 'rectangle':
            # Draw rectangle on the frame
            cv2.rectangle(frame,
                          (shape['x'], shape['y'] - kf),
                          (shape['x'] + shape['width'], shape['y'] + shape['height'] - kf),
                          (0, 255, 0), 2)  # Green color with thickness 2

            # Put text label on the rectangle
            cv2.putText(frame, shape['text'], (shape['x'], shape['y'] - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)  # White text
    return frame


def check_point_in_shapes(nail_x, nail_y):
    # Check if a point (nail) is inside any shape
    # Return the shape's text and index if found
    point = (nail_x, nail_y)
    shapes = load_shapes()

    for n, shape in enumerate(shapes):
        if shape['type'] == 'rectangle' and is_point_in_rectangle(point, shape):
            return shape['text'], n  # Return the text and index of the shape
    return None, None


def get_text():
    # Get a list of texts from all shapes
    shapes = load_shapes()
    return [shape['text'] for shape in shapes]  # Return a list of shape texts
