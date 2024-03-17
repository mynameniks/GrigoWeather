import os
import sys
import json
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from functions import Functions

class MainWindow(object):
    def ui_setup(self, main_window):
        self.main_window = main_window

        self.main_window.setObjectName("MainWindow")
        self.main_window.setGeometry(QtCore.QRect(1000, 300, 362, 493))
        self.main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.background = QtWidgets.QWidget(self.main_window)
        self.background.setObjectName('background')
        self.background.setGeometry(QtCore.QRect(0, 0, 362, 493))
        self.background.setStyleSheet(
            "background-color: rgb(5, 5, 5);\n"
            "border: solid;\n"
            "border-width: 1px;\n"
            "border-color: rgb(100, 100, 100);\n"
            "border-radius: 10px;"
        )

        self.close_app_button = QtWidgets.QPushButton(self.background)
        self.close_app_button.setObjectName('close_app_button')
        self.close_app_button.setGeometry(QtCore.QRect(330, 2, 20, 20))
        self.close_app_button.setStyleSheet(
            "#close_app_button {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "image: url(../assets/icons/close_app_static.png);\n"
            "border: none;\n"
            "}\n"
            "#close_app_button:hover {\n"
            "image: url(../assets/icons/close_app_hover.png);\n"
            "}\n"
            "#close_app_button:pressed {\n"
            "image: url(../assets/icons/close_app_pressed.png);\n"
            "}"
        )

        self.hide_app_button = QtWidgets.QPushButton(self.background)
        self.hide_app_button.setObjectName('hide_app_button')
        self.hide_app_button.setGeometry(QtCore.QRect(310, 10, 14, 14))
        self.hide_app_button.setStyleSheet(
            "#hide_app_button {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "image: url(../assets/icons/hide_app_static.png);\n"
            "border: none;\n"
            "}\n"
            "#hide_app_button:hover {\n"
            "image: url(../assets/icons/hide_app_hover.png);\n"
            "}\n"
            "#hide_app_button:pressed {\n"
            "image: url(../assets/icons/hide_app_pressed.png);\n"
            "}"
        )


        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setPointSize(10)

        self.app_logo = QtWidgets.QLabel(self.background)
        self.app_logo.setObjectName('app_logo')
        self.app_logo.setGeometry(QtCore.QRect(10, 2, 200, 20))
        self.app_logo.setFont(font)
        self.app_logo.setText('GRIGO WEATHER')
        self.app_logo.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(200, 200, 200);\n"
            "border: none;"
        )


        self.main_body = QtWidgets.QWidget(self.background)
        self.main_body.setObjectName("dark_mask")
        self.main_body.setGeometry(QtCore.QRect(1, 22, 360, 469))
        self.main_body.setStyleSheet(
            "background-color: rgb(17, 17, 17);\n"
            "border: none;\n"
            "border-radius: 10px;"
        )

        self.data_body = QtWidgets.QWidget(self.main_body)
        self.data_body.setObjectName('data_body')
        self.data_body.setGeometry(QtCore.QRect(10, 70, 340, 390))
        self.data_body.setStyleSheet(
            "background-color: rgb(10, 10, 10);\n"
            "border-radius: 10px;"
        )

        self.current_temp_body = QtWidgets.QWidget(self.data_body)
        self.current_temp_body.setObjectName('current_temp_body')
        self.current_temp_body.setGeometry(QtCore.QRect(10, 10, 180, 220))
        self.current_temp_body.setStyleSheet(
            "background-color: rgb(17, 17, 17);\n"
            "border-radius: 10px;"
        )

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setPointSize(13)

        self.weather_icon = QtWidgets.QWidget(self.current_temp_body)
        self.weather_icon.setObjectName('weather_icon')
        self.weather_icon.setGeometry(QtCore.QRect(5, 5, 20, 20))
        self.weather_icon.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "image: url(../assets/icons/temperature.png);\n"
        )

        font.setPointSize(12)

        self.weather_label = QtWidgets.QLabel(self.current_temp_body)
        self.weather_label.setObjectName('weather_label')
        self.weather_label.setGeometry(QtCore.QRect(26, 4, 160, 20))
        self.weather_label.setFont(font)
        self.weather_label.setText('WEATHER')
        self.weather_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(175, 175, 175);"
        )

        self.current_weather_image = QtWidgets.QWidget(self.current_temp_body)
        self.current_weather_image.setObjectName('current_weather_image')
        self.current_weather_image.setGeometry(QtCore.QRect(15, 10, 150, 130))
        self.current_weather_image.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
        )
        self.current_weather_image.close()

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setPointSize(48)

        self.current_temp_label = QtWidgets.QLabel(self.current_temp_body)
        self.current_temp_label.setObjectName('current_temp_label')
        self.current_temp_label.setGeometry(QtCore.QRect(10, 120, 160, 80))
        self.current_temp_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.current_temp_label.setFont(font)
        self.current_temp_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.current_temp_label.close()

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setPointSize(15)

        self.ranges_temp_label = QtWidgets.QLabel(self.current_temp_body)
        self.ranges_temp_label.setObjectName('highest_temp_label')
        self.ranges_temp_label.setGeometry(QtCore.QRect(15, 180, 150, 30))
        self.ranges_temp_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.ranges_temp_label.setFont(font)
        self.ranges_temp_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.ranges_temp_label.close()

        self.pressure_body = QtWidgets.QWidget(self.data_body)
        self.pressure_body.setObjectName('pressure_body')
        self.pressure_body.setGeometry(QtCore.QRect(200, 10, 130, 105))
        self.pressure_body.setStyleSheet(
            "background-color: rgb(17, 17, 17);\n"
            "border-radius: 10px;"
        )

        self.pressure_icon = QtWidgets.QWidget(self.pressure_body)
        self.pressure_icon.setObjectName('pressure_icon')
        self.pressure_icon.setGeometry(QtCore.QRect(5, 5, 20, 20))
        self.pressure_icon.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "image: url(../assets/icons/pressure.png);\n"
        )

        font.setPointSize(12)

        self.pressure_label = QtWidgets.QLabel(self.pressure_body)
        self.pressure_label.setObjectName('pressure_label')
        self.pressure_label.setGeometry(QtCore.QRect(26, 4, 75, 20))
        self.pressure_label.setFont(font)
        self.pressure_label.setText('PRESSURE')
        self.pressure_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(175, 175, 175);"
        )

        self.pressure_bar = QtWidgets.QProgressBar(self.pressure_body)
        self.pressure_bar.setObjectName('pressure_bar')
        self.pressure_bar.setGeometry(QtCore.QRect(7, 63, 115, 5))
        self.pressure_bar.setMinimum(975)
        self.pressure_bar.setMaximum(1075)
        self.pressure_bar.setTextVisible(False)
        self.pressure_bar.setStyleSheet(
            "#pressure_bar {\n"
            "border-radius: 2px;\n"
            "background-color: rgb(10, 10, 10);\n"
            "}\n"
            "#pressure_bar:chunk {\n"
            "border-radius: 2px;\n"
            "background-color: rgb(200, 200, 200);\n"
            "}"
        )
        self.pressure_bar.close()

        font.setPointSize(15)

        self.pressure_object = QtWidgets.QLabel(self.pressure_body)
        self.pressure_object.setObjectName('pressure_object')
        self.pressure_object.setGeometry(QtCore.QRect(5, 38, 115, 30))
        self.pressure_object.setAlignment(QtCore.Qt.AlignHCenter)
        self.pressure_object.setFont(font)
        self.pressure_object.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.pressure_object.close()


        self.humidity_body = QtWidgets.QWidget(self.data_body)
        self.humidity_body.setObjectName('humidity_body')
        self.humidity_body.setGeometry(QtCore.QRect(200, 125, 130, 105))
        self.humidity_body.setStyleSheet(
            "background-color: rgb(17, 17, 17);\n"
            "border-radius: 10px;"
        )

        self.humidity_icon = QtWidgets.QWidget(self.humidity_body)
        self.humidity_icon.setObjectName('pressure_icon')
        self.humidity_icon.setGeometry(QtCore.QRect(5, 5, 20, 20))
        self.humidity_icon.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "image: url(../assets/icons/humidity.png);\n"
        )

        font.setPointSize(12)

        self.humidity_label = QtWidgets.QLabel(self.humidity_body)
        self.humidity_label.setObjectName('humidity_label')
        self.humidity_label.setGeometry(QtCore.QRect(26, 4, 75, 20))
        self.humidity_label.setFont(font)
        self.humidity_label.setText('HUMIDITY')
        self.humidity_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(175, 175, 175);"
        )

        self.humidity_bar = QtWidgets.QProgressBar(self.humidity_body)
        self.humidity_bar.setObjectName('humidity_bar')
        self.humidity_bar.setGeometry(QtCore.QRect(7, 63, 115, 5))
        self.humidity_bar.setMinimum(0)
        self.humidity_bar.setMaximum(100)
        self.humidity_bar.setTextVisible(False)
        self.humidity_bar.setStyleSheet(
            "#humidity_bar {\n"
            "border-radius: 2px;\n"
            "background-color: rgb(10, 10, 10);\n"
            "}\n"
            "#humidity_bar:chunk {\n"
            "border-radius: 2px;\n"
            "background-color: rgb(200, 200, 200);\n"
            "}"
        )
        self.humidity_bar.close()

        font.setPointSize(15)

        self.humidity_object = QtWidgets.QLabel(self.humidity_body)
        self.humidity_object.setObjectName('humidity_object')
        self.humidity_object.setGeometry(QtCore.QRect(5, 38, 115, 30))
        self.humidity_object.setAlignment(QtCore.Qt.AlignHCenter)
        self.humidity_object.setFont(font)
        self.humidity_object.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.humidity_object.close()


        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)


        self.other_info_body = QtWidgets.QWidget(self.data_body)
        self.other_info_body.setObjectName('other_info_body')
        self.other_info_body.setGeometry(QtCore.QRect(10, 240, 320, 140))
        self.other_info_body.setStyleSheet(
            "background-color: rgb(17, 17, 17);\n"
            "border-radius: 10px;"
        )

        self.other_info_icon = QtWidgets.QWidget(self.other_info_body)
        self.other_info_icon.setObjectName('other_info_icon')
        self.other_info_icon.setGeometry(QtCore.QRect(9, 6, 18, 18))
        self.other_info_icon.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "image: url(../assets/icons/info.png);\n"
        )

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setPointSize(12)

        self.other_info_label = QtWidgets.QLabel(self.other_info_body)
        self.other_info_label.setObjectName('other_info_label')
        self.other_info_label.setGeometry(QtCore.QRect(32, 4, 100, 20))
        self.other_info_label.setFont(font)
        self.other_info_label.setText('INFORMATION')
        self.other_info_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(175, 175, 175);"
        )

        self.info_lines = []
        for i in range(4):
            self.info_line = QtWidgets.QFrame(self.other_info_body)
            self.info_line.setObjectName("info_line")
            self.info_line.setGeometry(QtCore.QRect(10, 30 + (33 * i), 300, 1))
            self.info_line.setStyleSheet("background-color: rgb(100, 100, 100);")
            self.info_line.setFrameShape(QtWidgets.QFrame.HLine)
            self.info_line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.info_line.close()
            self.info_lines.append(self.info_line)

        font.setPointSize(14)

        self.feels_like_label = QtWidgets.QLabel(self.other_info_body)
        self.feels_like_label.setObjectName('feels_like_label')
        self.feels_like_label.setGeometry(QtCore.QRect(10, 35, 100, 20))
        self.feels_like_label.setFont(font)
        self.feels_like_label.setAlignment(QtCore.Qt.AlignLeft)
        self.feels_like_label.setText('FEELS LIKE')
        self.feels_like_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.feels_like_label.close()

        self.feels_like_object = QtWidgets.QLabel(self.other_info_body)
        self.feels_like_object.setObjectName('feels_like_object')
        self.feels_like_object.setGeometry(QtCore.QRect(260, 35, 50, 20))
        self.feels_like_object.setAlignment(QtCore.Qt.AlignRight)
        self.feels_like_object.setFont(font)
        self.feels_like_object.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.feels_like_object.close()

        self.visibility_label = QtWidgets.QLabel(self.other_info_body)
        self.visibility_label.setObjectName('visibility_label')
        self.visibility_label.setGeometry(QtCore.QRect(11, 68, 100, 20))
        self.visibility_label.setFont(font)
        self.visibility_label.setAlignment(QtCore.Qt.AlignLeft)
        self.visibility_label.setText('VISIBILITY')
        self.visibility_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.visibility_label.close()

        self.visibility_object = QtWidgets.QLabel(self.other_info_body)
        self.visibility_object.setObjectName('visibility_object')
        self.visibility_object.setGeometry(QtCore.QRect(239, 68, 70, 20))
        self.visibility_object.setAlignment(QtCore.Qt.AlignRight)
        self.visibility_object.setFont(font)
        self.visibility_object.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.visibility_object.close()

        self.wind_label = QtWidgets.QLabel(self.other_info_body)
        self.wind_label.setObjectName('wind_label')
        self.wind_label.setGeometry(QtCore.QRect(11, 101, 100, 20))
        self.wind_label.setFont(font)
        self.wind_label.setAlignment(QtCore.Qt.AlignLeft)
        self.wind_label.setText('WIND')
        self.wind_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.wind_label.close()

        self.wind_object = QtWidgets.QLabel(self.other_info_body)
        self.wind_object.setObjectName('wind_speed')
        self.wind_object.setGeometry(QtCore.QRect(239, 101, 70, 20))
        self.wind_object.setAlignment(QtCore.Qt.AlignRight)
        self.wind_object.setFont(font)
        self.wind_object.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(215, 215, 215);"
        )
        self.wind_object.close()


        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)

        self.city_enter_field = QtWidgets.QLineEdit(self.main_body)
        self.city_enter_field.setObjectName("city_enter_field")
        self.city_enter_field.setGeometry(QtCore.QRect(20, 20, 320, 30))
        self.city_enter_field.setFont(font)
        self.city_enter_field.setStyleSheet(
            "background-color: rgb(10, 10, 10);\n"
            "color: rgb(215, 215, 215);\n"
            "padding: 0 30px 0 40px;\n"
            "border-radius: 15px;"
            "border: solid;\n"
            "border-width: 1px;\n"
            "border-color: rgb(175, 175, 175);"
        )

        self.search_button = QtWidgets.QPushButton(self.main_body)
        self.search_button.setObjectName('search_button')
        self.search_button.setGeometry(QtCore.QRect(310, 22, 25, 25))
        self.search_button.setStyleSheet(
            "#search_button {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "image: url(../assets/icons/search_static.png);\n"
            "}\n"
            "#search_button:hover {\n"
            "image: url(../assets/icons/search_hover.png);\n"
            "}\n"
            "#search_button:pressed {\n"
            "image: url(../assets/icons/search_pressed.png);\n"
            "}"
        )

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.city_label = QtWidgets.QLabel(self.main_body)
        self.city_label.setObjectName("city_label")
        self.city_label.setGeometry(QtCore.QRect(30, 25, 40, 20))
        self.city_label.setFont(font)
        self.city_label.setText('City')
        self.city_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(235, 235, 235);"
        )

        self.add_functions()

    def add_functions(self):
        self.close_app_button.clicked.connect(
            lambda x: Functions(obj=self.main_window).close_app()
        )
        self.hide_app_button.clicked.connect(
            lambda x: Functions(obj=self.main_window).hide_app()
        )
        self.search_button.clicked.connect(
            lambda x: Functions(
                self.city_enter_field.text(),
                self.current_weather_image,
                self.current_temp_label,
                self.ranges_temp_label,
                self.weather_label,
                self.pressure_bar,
                self.pressure_object,
                self.humidity_bar,
                self.humidity_object,
                self.feels_like_label,
                self.feels_like_object,
                self.visibility_label,
                self.visibility_object,
                self.wind_label,
                self.wind_object,
                self.info_lines
            ).get_weather()
        )


class WindowFrame(QtWidgets.QWidget, MainWindow):
    def __init__(self, parent=None):
        super(WindowFrame, self).__init__(parent)
        self.ui_setup(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            on_height = self.geometry().y()+25
            cursor = QtGui.QCursor.pos().y()

            if cursor < on_height:
                self.old_pos = event.pos()
            else:
                self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None


    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None


    def mouseMoveEvent(self, event):
        try:
            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)
        except AttributeError:
            pass


app = QtWidgets.QApplication(sys.argv)
ui = WindowFrame()
ui.show()

sys.exit(app.exec_())
