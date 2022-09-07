from datetime import datetime
from random import randrange, randint

temp = randrange(20, 40)

def get_time():
    time = datetime.now()
    return time.strftime("%Y/%m/%d %H:%M")


def generate_data():
    global temp
    if randint(0, 1):
        temp = temp + 1
    else:
        temp = temp - 1
    return temp


def avg_data(data):
    with open('avg_temp.txt', 'a') as f:
        f.write(str(get_time()) + " | " + str(round(sum(data) / len(data),2)) + " C\n")