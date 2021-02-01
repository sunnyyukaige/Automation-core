# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 11:04 AM
# @Author  : Sunny.Yu
# @FileName: Logging.py.py
# @Software: PyCharm

from functools import wraps
import logging


def general_log_decorator(func):
    """
    输出日志的装饰器
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args):
        try:
            result = func(*args)
        except Exception as e:
            logging.error(func.__name__ + ' run failed')
            raise e
        return result

    return wrapper


def find_log_decorator(func):
    """
        输出Exception的装饰器
        :param func:
        :return:
        """

    @wraps(func)
    def wrapper(*args):
        try:
            result = func(*args)
        except Exception as e:
            logging.error(func.__name__ + ' run failed')
            raise Exception("Cannot find element by [%s]:under:\n %s \n" % (args[1], args[2]))
        return result

    return wrapper
