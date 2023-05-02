from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel
from  PyQt6.QtCore import QTimer
from PyQt6 import uic
import time


class MainWindow(QMainWindow):
    """Main window class.

    Attributes:
        timer_text (QLabel): timer display.
        start_button (QPushButton): start button.
        interval (int): interval for timer.
        raw_seconds (int): raw seconds.
        timer (QTimer): timer.
        timer_started (bool): indicates if timer is started.
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/mainUi.ui", self)

        self.timer_text: QLabel = self.findChild(QLabel, "timeLabel")
        self.start_button: QPushButton = self.findChild(QPushButton, "startButton")

        self.interval: int = 25
        self.raw_seconds: int = self.interval * 60
        self.timer: QTimer = QTimer()
        self.timer_started: bool = False

        self.timer_text.setText("25:00")

        self.start_button.clicked.connect(self.start_or_pause_timer)
        self.timer.timeout.connect(self.tick)

        self.show()

    def start_or_pause_timer(self):
        """Starts or pauses timer
        """
        if not self.timer_started:
            self.timer_started = True
            self.timer.start(1000)
            self.start_button.setText("PAUSE")
        else:
            self.timer_started = False
            self.timer.stop()
            self.start_button.setText("START")

    def tick(self):
        """Handles tick event.
        """
        self.raw_seconds -= 1
        minutes = self.raw_seconds // 60
        seconds = self.raw_seconds % 60
        if seconds > 9:
            self.timer_text.setText(f"{minutes}:{seconds}")
        else:
            self.timer_text.setText(f"{minutes}:0{seconds}")

        if self.raw_seconds == 0:
            self.timer.stop()
