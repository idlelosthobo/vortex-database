from ..settings import DEBUG, ADVANCED_PROCESSING, ASSUMPTIVE_UNDERSTANDING, TIME_ITERATION, APP_VERSION, \
    APP_NAME
import time


def debug():
    return DEBUG


def advanced():
    return ADVANCED_PROCESSING


def assumptive():
    return ASSUMPTIVE_UNDERSTANDING


def time_iteration():
    return TIME_ITERATION


def time_now():
    if time_iteration() == 'second':
        return round(time.time())
    elif time_iteration() == 'minute':
        return round(time.time() / 60)
    elif time_iteration() == 'hour':
        return round(time.time() / 60 / 60)
    elif time_iteration() == 'day':
        return round(time.time() / 60 / 60 / 24)


def file_header():
    header = 'application: ' + APP_NAME + ' version: ' + APP_VERSION + ' time: ' + TIME_ITERATION
    return header

