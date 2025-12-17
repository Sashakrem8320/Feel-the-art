import sys
import json
import cv2
import numpy as np
from PyQt6 import QtWidgets, QtGui, QtCore

class ImageLabel(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.drawing = False
        self.start_point = None
        self.end_point = None
        self.shapes = []
        self.current_shape = None
        self.text = ""

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QtGui.QPainter(self)

        # Draw existing shapes
        for shape in self.shapes:
            painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.red, 2))
            if shape['type'] == 'rectangle':
                painter.drawRect(shape['x'], shape['y'], shape['width'], shape['height'])
            elif shape['type'] == 'circle':
                painter.drawEllipse(shape['x'], shape['y'], shape['width'], shape['height'])
            painter.drawText(shape['x'], shape['y'] - 5, shape['text'])


        # Draw the current shape if drawing
        if self.drawing and self.start_point and self.end_point:
            painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.blue, 2, QtCore.Qt.PenStyle.DashLine))
            x = min(self.start_point.x(), self.end_point.x())
            y = min(self.start_point.y(), self.end_point.y())
            width = abs(self.start_point.x() - self.end_point.x())
            height = abs(self.start_point.y() - self.end_point.y())
            if self.current_shape == 'rectangle':
                painter.drawRect(x, y, width, height)
            elif self.current_shape == 'circle':
                painter.drawEllipse(x, y, width, height)

    def mousePressEvent(self, event):
        if self.text:
            self.drawing = True
            self.start_point = event.pos()
            self.end_point = event.pos()  # Initialize end_point to start_point

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end_point = event.pos()  # Update end_point as the mouse moves
            self.update()  # Trigger a repaint

    def mouseReleaseEvent(self, event):
        if self.drawing:
            self.drawing = False
            self.end_point = event.pos()  # Finalize end_point
            self.add_shape()  # Add the shape to the list
            self.update()  # Trigger a repaint

    def add_shape(self):
        if self.start_point and self.end_point:
            x = min(self.start_point.x(), self.end_point.x())
            y = min(self.start_point.y(), self.end_point.y())
            width = abs(self.start_point.x() - self.end_point.x())
            height = abs(self.start_point.y() - self.end_point.y())
            shape_type = 'rectangle' if self.current_shape == 'rectangle' else 'circle'
            self.shapes.append({
                'type': shape_type,
                'x': x,
                'y': y,
                'width': width,
                'height': height,
                'text': self.text
            })
            self.start_point = None
            self.end_point = None
            self.text = ""
            self.current_shape = None

    def set_shape(self, shape):
        self.current_shape = shape

    def set_text(self, text):
        self.text = text

    def save_shapes(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.shapes, f)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Annotation Tool")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = ImageLabel()
        self.setCentralWidget(self.image_label)

        # Input for text
        self.text_input = QtWidgets.QLineEdit(self)
        self.text_input.setPlaceholderText("Введите текст для фигуры")
        self.text_input.setGeometry(10, 10, 200, 30)

        # Buttons
        button_width = 100
        button_height = 30

        self.rectangle_button = QtWidgets.QPushButton("Квадрат", self)
        self.rectangle_button.setGeometry(220, 10, button_width, button_height)
        self.rectangle_button.clicked.connect(lambda: self.set_shape('rectangle'))

        self.circle_button = QtWidgets.QPushButton("Круг", self)
        self.circle_button.setGeometry(330, 10, button_width, button_height)
        self.circle_button.clicked.connect(lambda: self.set_shape('circle'))

        self.save_button = QtWidgets.QPushButton("Сохранить", self)
        self.save_button.setGeometry(440, 10, button_width, button_height)
        self.save_button.clicked.connect(self.save_shapes)

        self.capture_button = QtWidgets.QPushButton("Захватить фото", self)
        self.capture_button.setGeometry(550, 10, button_width + 50, button_height)
        self.capture_button.clicked.connect(self.capture_image)

    def set_shape(self, shape):
        self.image_label.set_shape(shape)
        self.image_label.set_text(self.text_input.text())

    def save_shapes(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "", "JSON Files (*.json)")
        if filename:
            self.image_label.save_shapes(filename)

    def capture_image(self):
        cap = cv2.VideoCapture(0) #Если используется робот то 1
        ret, frame = cap.read()
        if ret:
            # Преобразуем изображение из BGR в RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Увеличиваем яркость изображения
            frame = cv2.convertScaleAbs(frame, alpha=1.5, beta=0)  # Увеличение яркости
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QtGui.QImage(frame.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
            self.image_label.setPixmap(QtGui.QPixmap.fromImage(q_img))
        cap.release()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

