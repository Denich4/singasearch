import datetime

def get_now():
    return datetime.datetime.now().strftime("%d/%m - %H:%M")