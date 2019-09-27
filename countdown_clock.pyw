import PyQt5.QtCore as qtc
from PyQt5.QtCore import QTime, QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QLCDNumber, QDesktopWidget

targetTime = QDateTime.fromString("13-10-2019, 08:00:00", "dd-MM-yyyy, hh:mm:ss")

class CountdownClock(QLCDNumber):
    def __init__(self, parent=None):
        super(CountdownClock, self).__init__(parent)
        self.setStyleSheet("QLCDNumber { color: white; background-color: black}")
        self.setWindowFlags(qtc.Qt.WindowFlags() | qtc.Qt.FramelessWindowHint | qtc.Qt.WindowStaysOnTopHint)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(200, 90)
 
    def showTime(self):
        time = QDateTime.currentDateTime()
        diffSecs = time.secsTo(targetTime)
        diffHr = diffSecs // (60*60)
        diffMin = (diffSecs % (60*60)) // 60

        diffStr = "%d:%02d" % (diffHr, diffMin)

        self.setDigitCount(len(diffStr))

        self.display(diffStr)
		
    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = CountdownClock()
    clock.location_on_the_screen()
    clock.show()
    sys.exit(app.exec_())