from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Functions:
    def __init__(self, obj, *args):
        self.obj = obj
        self.args = args

    def close_app(self):
        self.obj.close()

    def hide_app(self):
        self.obj.showMinimized()

    def get_weather(self):
        city = self.obj

        key = '29038bc3e7bc8ae3f7ff21622c9cf43e'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'appid': key, 'q': city, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()

        if 'message' in weather.keys():
            pass
        else:
            self.parse_frame(weather)

    def parse_frame(self, weather):
        key = weather['weather'][0]['description']
        if 'thunderstorm' in key:
            key = 'thunderstorm'

        about = ''
        for i in key: about += i.capitalize()
        for i in self.args[:-1]: i.show()
        for i in self.args[14]: i.show()

        try:
            visibility = f'{'%.1f' % (weather['visibility']/1000)} km'
        except KeyError:
            visibility = 'None'

        self.args[0].setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            f"image: url(../assets/weather_types/{key}.png);\n"
        )
        self.args[1].setText(f'{'%.1f' % weather['main']['temp']}°')
        self.args[2].setText(f'🠕{'%.1f' % weather['main']['temp_max']}°  🠗{'%.1f' % weather['main']['temp_min']}°')
        self.args[3].setText(about)
        self.args[4].setValue(weather['main']['pressure'])
        self.args[5].setText(f'{weather['main']['pressure']} hPa')
        self.args[6].setValue(weather['main']['humidity'])
        self.args[7].setText(f'{weather['main']['humidity']} %')
        self.args[9].setText(f'{'%.0f' % weather['main']['feels_like']}°')
        self.args[11].setText(visibility)
        self.args[13].setText(f'{'%.1f' % weather['wind']['speed']} m/s')

