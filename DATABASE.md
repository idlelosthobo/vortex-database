# Data File Header
    Postioned at byte 0 and is 64 bytes long 
# Seek Structure
    The seek file directly references a 4 character set in the locale language.
        Example  : "a" would be at byte 64, "ac" would be at byte 192
        
    This structure is static and generate when the file is created.
     
    Data is postioned every 64 bytes
        0 to 31  : start location of all items related to character set in data file.
        32 to 63 : the amount of data items in the data file for that character set.
# Data Structure
    Positioned based on settings variable "DATA_SIZE" in bytes
        0 to DATA_SIZE : Contains the data set inserted in this specific location.