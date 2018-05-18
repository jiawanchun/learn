#coding=utf-8
'''
import os
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException,InvalidElementStateException

def fail_on_screenshot(function):
    def get_snapshot_directory():
        if not os.path.exists(settings.SNAPSHOT_DIRECTORY):
            os.mkdir(settings.SNAPSHOT_DIRECTORY)
            return settings.SNAPSHOT_DIRECTORY
    def get_current_time_str():
        return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f")

    def wrapper(*args, **kwargs):
		instance, selector = args[0], args[1]
		try:
            return function(*args, **kwargs)
        except (TimeoutException, NoSuchElementException, InvalidElementStateException) as ex:
            logger.error("Could not find the selector: [{}].".format(selector))
            filename = "{}.png".format(get_current_time_str())
            screenshot_path = os.path.join(get_snapshot_directory(), filename)
            logger.debug(instance.selenium.page_source)
            instance.selenium.save_screenshot(screenshot_path)
            raise ex
    return wrapper
'''
class Page(object):
    """
    页面对象的基本页面类
    """
    def __init__(self, selenium_driver):
        self.dr = selenium_driver