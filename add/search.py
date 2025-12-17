import cv2
from add import markup
from add import extra
def process_webcam_with_detection_low(model, cap):
    center = []
    min_area = 800
    max_area = 1900

    ret, frame = cap.read()
    if not ret:
        extra.alarm("Не удалось подключиться к камере")
        return center  # Return empty center if frame capture fails

    results = model(frame, iou=0.8, conf=0.6, imgsz=640, verbose=False)

    if results[0].boxes is not None and len(results[0].boxes) > 0:
        print(f"Обнаружено {len(results[0].boxes)} объектов.")

        boxes = results[0].boxes.xyxy.numpy().astype(int)

        if results[0].boxes.id is not None:
            ids = results[0].boxes.id.numpy().astype(int)
        else:
            ids = [0] * len(boxes)

        filtered_boxes = []
        filtered_ids = []

        for box, id in zip(boxes, ids):
            width = box[2] - box[0]
            height = box[3] - box[1]
            area = width * height

            if min_area < area < max_area:
                filtered_boxes.append(box)
                filtered_ids.append(id)

        if len(filtered_boxes) > 0:
            for one_box in filtered_boxes:
                current_box = one_box
                center_x = (current_box[0] + current_box[2]) // 2
                center_y = (current_box[1] + current_box[3]) // 2
                center.append((center_x, center_y))

                # Draw bounding boxes and labels
                cv2.rectangle(frame, (current_box[0], current_box[1]), (current_box[2], current_box[3]), (100, 100, 100), 2)

    frame = markup.draw_shapes_on_frame(frame)  # Ensure this function is correctly implemented
    cv2.rectangle(frame, (80, 89), (517, 402), (255, 0, 0), 2)
    cv2.imshow("Detected Objects", frame)
    cv2.waitKey(1)
    return center
