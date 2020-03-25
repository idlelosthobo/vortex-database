from ..settings import DEBUG, ADVANCED_PROCESSING, ASSUMPTIVE_UNDERSTANDING, TIME_ITERATION, APP_VERSION, \
    APP_NAME, SEEK_CHARACTER_SIZE, INSTANCES_DIRECTORY
import time, os


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
    elif time_iteration() == 'week':
        return round(time.time() / 60 / 60 / 24 / 7)


def file_header():
    header = 'Application: ' + APP_NAME + ' Version: ' + APP_VERSION + ' Time Iteration: ' + TIME_ITERATION
    return str(header)


def check_file_header(file, location):
    file_header_size = len(file_header())
    if os.stat(location).st_size == 0:
        file.seek(0)
        file.write(file_header())
        file.seek(0)
        header_validated = True
    else:
        file.seek(0)
        header = file.read(file_header_size)
        if header == file_header():
            header_validated = True
        else:
            header_validated = False
    return header_validated


def seek_character_size():
    if 0 < SEEK_CHARACTER_SIZE <= 4:
        return SEEK_CHARACTER_SIZE
