from datetime import datetime
from logger import logger


class ScheduleManager():

    def __init__(self, scheduled_times):
        self.times = scheduled_times
        logger.debug('Schedule times')
        logger.debug(self.times)

    def get_actual_time(self):
        now = datetime.now()
        return "%02d:%02d" % (now.hour, now.minute)

    def its_time(self):
        return self.get_actual_time() in self.times
