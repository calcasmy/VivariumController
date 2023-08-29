import configparser


config = configparser.RawConfigParser()
config.read('ConfigFile.properties')


class DBCONFIG:
    vdbname = config.get('DBSection', 'database.vdbname')
    adbname = config.get('DBSection', 'database.adbname')
    dbhost = config.get('DBSection', 'database.host')
    dbuser = config.get('DBSection', 'database.user')
    dbpassword = config.get('DBSection', 'database.password')

class APPCONFIG:
    weatherAPI = config.get('AppSection', 'app.weatherapi')
