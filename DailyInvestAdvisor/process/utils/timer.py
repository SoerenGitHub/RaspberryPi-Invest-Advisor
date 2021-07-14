import datetime, time

class Timer:

    def set_timer(self, h, m):
        today = datetime.datetime.now()

        sleep = (datetime.datetime(today.year, today.month, today.day, h-1, m, 0) - today).seconds
        print('Timer is waiting until {h}:{m} o\'clock.'.format(h=h, m=m))
        time.sleep(sleep)