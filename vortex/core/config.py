from ..settings import DEBUG, ADVANCED_PROCESSING, ASSUMPTIVE_UNDERSTANDING, DATE_ITERATION, APP_VERSION, DATA_SIZE,\
    APP_NAME


def debug():
    return DEBUG


def advanced():
    return ADVANCED_PROCESSING


def assumptive():
    return ASSUMPTIVE_UNDERSTANDING


def iteration():
    return DATE_ITERATION


def file_header():
    header = 'application: ' + APP_NAME + ' version: ' + APP_VERSION + ' data size: ' + str(DATA_SIZE)
    return header

