import cv2
import json

def load_shapes(filename):
    with open(filename, 'r') as f:
        shapes = json.load(f)
    return shapes

def is_point_in_rectangle(point, shape):
    x, y = point
    return (shape['x'] <= x <= shape['x'] + shape['width'] and
            shape['y'] - shape['height'] <= y <= shape['y'])

def draw_shapes_on_frame(frame, shapes):
    height, width, _ = frame.shape  # Получаем размеры кадра

    for shape in shapes:
        if shape['type'] == 'rectangle':
            cv2.rectangle(frame,
                          (shape['x'], shape['y']),
                          (shape['x'] + shape['width'], shape['y'] - shape['height']),
                          (0, 255, 0), 2)
            cv2.putText(frame, shape['text'], (shape['x'], shape['y'] - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)  # Белый текст

    return frame

def check_point_in_shapes(point, shapes):
    for shape in shapes:
        if shape['type'] == 'rectangle' and is_point_in_rectangle(point, shape):
            print(f"Точка {point} попадает в фигуру: {shape['text']}")
            return shape['text']
    return None

def main(json_filename):
    # Загружаем фигуры из JSON файла
    shapes = load_shapes(json_filename)

    # Запускаем захват видео
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Ошибка: не удалось открыть веб-камеру.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Ошибка: не удалось захватить изображение.")
            break

        # Рисуем фигуры на захваченном кадре
        frame_with_shapes = draw_shapes_on_frame(frame, shapes)

        # Пример точки, которую мы проверяем (можно заменить на пользовательский ввод)
        point_to_check = (239, 337)  # Замените на ваши координаты точки
        text = check_point_in_shapes(point_to_check, shapes)

        # Показываем кадр
        cv2.imshow('Webcam with Shapes', frame_with_shapes)

        # Выход при нажатии 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    json_filename = "../1.json"  # Укажите имя вашего JSON файла
    main(json_filename)