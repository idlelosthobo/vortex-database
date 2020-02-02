import os

APP_NAME = 'vortex'

# Note changing file versions should only be used after refactoring the data file.
APP_VERSION = '0.1a'

DEBUG = True

ADVANCED_PROCESSING = False

ASSUMPTIVE_UNDERSTANDING = False

# Determine what the storage iteration is day, hour, minute, second
# Note that minute, second and even hour can take up a lot of storage space.
# Once this is set you cannot change it as all timing in the system will stop working.
TIME_ITERATION = 'hour'

LOCALE = 'english_canada'

INSTANCES_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instances')
