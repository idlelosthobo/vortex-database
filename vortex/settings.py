import os

DEBUG = True

PACKAGE_NAME = 'vortex'

ADVANCED_PROCESSING = False

ASSUMPTIVE_UNDERSTANDING = False

# Determine what the storage iteration is year, month, day, hour, second
# Note that second and even hour can take up a lot of storage space.
DATE_ITERATION = 'hour'

LOCALE = 'english_canada'

INSTANCES_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instances')
