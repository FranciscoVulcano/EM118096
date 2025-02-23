from enum import Enum

class Commands(Enum):
    VOLTAGE = "100"
    CURRENT = "102"
    ACTIVE_POWER = "104"
    APPARENT_POWER = "106"
    REACTIVE_POWER = "108"
    FREQUENCY = "10A"
    POWER_FACTOR = "10B"
    POWER_FACTOR_CL = "10B"
    TOTAL_FORWARD_ACTIVE_ENERGY = "10E"
    T1_FORWARD_ACTIVE_ENERGY = "110"
    T2_FORWARD_ACTIVE_ENERGY = "112"
    T3_FORWARD_ACTIVE_ENERGY = "114"
    T4_FORWARD_ACTIVE_ENERGY = "116"
    TOTAL_REVERSE_ACTIVE_ENERGY = "118"
    T1_REVERSE_ACTIVE_ENERGY = "11A"
    T2_REVERSE_ACTIVE_ENERGY = "11C"
    T3_REVERSE_ACTIVE_ENERGY = "11E"
    T4_REVERSE_ACTIVE_ENERGY = "120"
    ACTIVE_TOTAL_POWER = "122"
    T1_TOTAL_ACTIVE_ENERGY = "124"
    T2_TOTAL_ACTIVE_ENERGY = "126"
    T3_TOTAL_ACTIVE_ENERGY = "128"
    T4_TOTAL_ACTIVE_ENERGY = "12A"
    TOTAL_FORWARD_REACTIVE_ENERGY = "12C"
    T1_FORWARD_REACTIVE_ENERGY = "12E"
    T2_FORWARD_REACTIVE_ENERGY = "130"
    T3_FORWARD_REACTIVE_ENERGY = "132"
    T4_FORWARD_REACTIVE_ENERGY = "134"
    TOTAL_REVERSE_REACTIVE_ENERGY = "136"
    T1_REVERSE_REACTIVE_ENERGY = "138"
    T2_REVERSE_REACTIVE_ENERGY = "13A"
    T3_REVERSE_REACTIVE_ENERGY = "13C"
    T4_REVERSE_REACTIVE_ENERGY = "13E"
    TOTAL_REACTIVE_ENERGY = "140"
    T1_REACTIVE_ENERGY = "142"
    T2_REACTIVE_ENERGY = "144"
    T3_REACTIVE_ENERGY = "146"
    T4_REACTIVE_ENERGY = "148"
    TOTAL_FIRST_QUADRANT_REACTIVE_ENERGY = "14A"
    T1_FIRST_QUADRANT_REACTIVE_ENERGY = "14C"
    T2_FIRST_QUADRANT_REACTIVE_ENERGY = "14E"
    T3_FIRST_QUADRANT_REACTIVE_ENERGY = "150"
    T4_FIRST_QUADRANT_REACTIVE_ENERGY = "152"
    TOTAL_SECOND_QUADRANT_REACTIVE_ENERGY = "154"
    T1_SECOND_QUADRANT_REACTIVE_ENERGY = "156"
    T2_SECOND_QUADRANT_REACTIVE_ENERGY = "158"
    T3_SECOND_QUADRANT_REACTIVE_ENERGY = "15A"
    T4_SECOND_QUADRANT_REACTIVE_ENERGY = "15C"
    TOTAL_THIRD_QUADRANT_REACTIVE_ENERGY = "15E"
    T1_THIRD_QUADRANT_REACTIVE_ENERGY = "160"
    T2_THIRD_QUADRANT_REACTIVE_ENERGY = "162"
    T3_THIRD_QUADRANT_REACTIVE_ENERGY = "164"
    T4_THIRD_QUADRANT_REACTIVE_ENERGY = "166"
    TOTAL_FOURTH_QUADRANT_REACTIVE_ENERGY = "168"
    T1_FOURTH_QUADRANT_REACTIVE_ENERGY = "16A"
    T2_FOURTH_QUADRANT_REACTIVE_ENERGY = "16C"
    T3_FOURTH_QUADRANT_REACTIVE_ENERGY = "16E"
    T4_FOURTH_QUADRANT_REACTIVE_ENERGY = "170"
    RESETTABLE_ACTIVE_TOTAL_POWER = "172"
    RESETTABLE_TOTAL_REACTIVE_ENERGY = "174"
    POSITIVE_ACTIVE_DEMAND = "176"
    FORWARD_MAX_ACTIVE_DEMAND = "178"
    REVERSE_ACTIVE_DEMAND = "17A"
    REVERSE_MAX_ACTIVE_DEMAND = "17C"
    FORWARD_REACTIVE_DEMAND = "17E"
    FORWARD_MAX_ACTIVE_REACTIVE_DEMAND = "180"
    REVERSE_REACTIVE_ENERGY_DEMAND = "182"
    REVERSE_MAX_ACTIVE_REACTIVE_DEMAND = "184"
    SERIAL_NUMBER = "1000"
    MODBUS_ID = "1003"
    SOFTWARE_VERSION = "1004"
    HARDWARE_VERSION = "1005"
    FIRMWARE_CHECKSUM = "1006"
    TIME = "1007"
    ROTATION_TIME = "100B"
    BAUD_RATE = "100C"
    CHECK_DIGIT = "100D"
    STOP_BIT = "100E"
    COMBINED_CODE = "100F"
    DEMAND_MODE = "1010"
    DEMAND_CYCLE = "1011"
    AUTOMATIC_ROTATION_CONTENT = "1012"
    LCD_BUTTON_DISPLAY_SETTING_PASSWORD = "1016"
    METER_RUNNING_TIME = "1018"
    SET_TIMING_CURRENT_VALUE = "101A"
    METER_RUNNING_STATUS_WORD_1 = "2002"
    METER_RUNNING_STATUS_WORD_2 = "4000502"
    METER_RUNNING_STATUS_WORD_3 = "4000503"
    METER_RUNNING_STATUS_WORD_4 = "4000504"
    METER_RUNNING_STATUS_WORD_5 = "4000505"
    METER_RUNNING_STATUS_WORD_6 = "4000506"
    METER_RUNNING_STATUS_WORD_7 = "4000507"
    METER_RUNNING_STATUS_WORD_BLOCK = "040005FF"
    CLEAR_ELECTRICITY = "C_1A"
    CLEAR_MAX_DEMAND = "C_19"
    TIMETABLE_1 = "1700"
    TIMETABLE_2 = "170C"
    TIMETABLE_3 = "1718"
    TIMETABLE_4 = "1724"
    TIMETABLE_5 = "1730"
    TIMETABLE_6 = "173C"
    TIMETABLE_7 = "1748"
    TIMETABLE_8 = "1754"
    TIME_ZONE_TABLE = "1760"
    HOLIDAY_TABLE = "176C"

class CommandLenght(Enum):
    VOLTAGE = 2
    CURRENT = 2
    ACTIVE_POWER = 2
    APPARENT_POWER = 2
    REACTIVE_POWER = 2
    FREQUENCY = 1
    POWER_FACTOR = 1
    POSITIVE_TOTAL_ACTIVE_ENERGY = 2
    T1_TOTAL_FORWARD_ACTIVE_ENERGY = 2
    T2_TOTAL_FORWARD_ACTIVE_ENERGY = 2
    T3_TOTAL_FORWARD_ACTIVE_ENERGY = 2
    T4_TOTAL_FORWARD_ACTIVE_ENERGY = 2
    TOTAL_REVERSE_ACTIVE_ENERGY = 2
    T1_TOTAL_REVERSE_ACTIVE_ENERGY = 2
    T2_TOTAL_REVERSE_ACTIVE_ENERGY = 2
    T3_TOTAL_REVERSE_ACTIVE_ENERGY = 2
    T4_TOTAL_REVERSE_ACTIVE_ENERGY = 2
    ACTIVE_TOTAL_POWER = 2
    T1_TOTAL_ACTIVE_ENERGY = 2
    T2_TOTAL_ACTIVE_ENERGY = 2
    T3_TOTAL_ACTIVE_ENERGY = 2
    T4_TOTAL_ACTIVE_ENERGY = 2
    TOTAL_FORWARD_REACTIVE_ENERGY = 2
    T1_TOTAL_FORWARD_REACTIVE_ENERGY = 2
    T2_TOTAL_FORWARD_REACTIVE_ENERGY = 2
    T3_TOTAL_FORWARD_REACTIVE_ENERGY = 2
    T4_TOTAL_FORWARD_REACTIVE_ENERGY = 2
    TOTAL_REVERSE_REACTIVE_ENERGY = 2
    T1_TOTAL_REVERSE_REACTIVE_ENERGY = 2
    T2_TOTAL_REVERSE_REACTIVE_ENERGY = 2
    T3_TOTAL_REVERSE_REACTIVE_ENERGY = 2
    T4_TOTAL_REVERSE_REACTIVE_ENERGY = 2
    TOTAL_REACTIVE_ENERGY = 2
    T1_TOTAL_REACTIVE_ENERGY = 2
    T2_TOTAL_REACTIVE_ENERGY = 2
    T3_TOTAL_REACTIVE_ENERGY = 2
    T4_TOTAL_REACTIVE_ENERGY = 2
    TOTAL_REACTIVE_ENERGY_FIRST_QUADRANT = 2
    T1_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T2_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T3_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T4_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    TOTAL_REACTIVE_ENERGY_SECOND_QUADRANT = 2
    T1_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T2_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T3_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T4_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    TOTAL_REACTIVE_ENERGY_THIRD_QUADRANT = 2
    T1_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T2_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T3_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T4_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    TOTAL_REACTIVE_ENERGY_FOURTH_QUADRANT = 2
    T1_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T2_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T3_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    T4_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = 2
    RESETTABLE_ACTIVE_TOTAL_POWER = 2
    RESETTABLE_TOTAL_REACTIVE_ENERGY = 2
    POSITIVE_ACTIVE_DEMAND = 3
    FORWARD_MAXIMUM_ACTIVE_DEMAND = 3
    REVERSE_ACTIVE_DEMAND = 3
    REVERSE_MAXIMUM_ACTIVE_DEMAND = 3
    FORWARD_REACTIVE_DEMAND = 3
    FORWARD_MAXIMUM_ACTIVE_AND_REACTIVE_ENERGY_DEMAND = 3
    REVERSE_REACTIVE_ENERGY_DEMAND = 3
    REVERSE_MAXIMUM_ACTIVE_AND_REACTIVE_ENERGY_DEMAND = 3
    ITEM = 6
    MODBUS_ID = 1
    SOFTWARE_VERSION_NUMBER = 1
    HARDWARE_VERSION_NUMBER = 1
    FIRMWARE_CHECKSUM = 1
    TIME = 4
    ROTATION_TIME = 1
    BAUD_RATE_485 = 1
    CHECK_DIGIT_485 = 1
    STOP_BIT_485 = 1
    COMBINED_CODE = 1
    DEMAND_MODE = 1
    DEMAND_CYCLE = 1
    AUTOMATIC_ROTATION_CONTENT = 4
    LCD_BUTTON_DISPLAY_SETTING_PASSWORD = 1
    METER_RUNNING_TIME = 2
    SET_TIMING_CURRENT_VALUE = 2
    TIMETABLE_1 = 12
    TIMETABLE_2 = 12
    TIMETABLE_3 = 12
    TIMETABLE_4 = 12
    TIMETABLE_5 = 12
    TIMETABLE_6 = 12
    TIMETABLE_7 = 12
    TIMETABLE_8 = 12
    TIME_ZONE_TABLE = 12
    HOLIDAY_TABLE = 21


class ResultFormat(Enum):
    VOLTAGE = "INT32_3_3"
    CURRENT = "INT32_2_3"
    ACTIVE_POWER = "INT32_5_0"
    APPARENT_POWER = "INT32_5_0"
    REACTIVE_POWER = "INT32_5_0"
    FREQUENCY = "INT16_2_1"
    POWER_FACTOR = "INT16_1_3"

    POSITIVE_TOTAL_ACTIVE_ENERGY = "INT32_6_2"
    T1_TOTAL_FORWARD_ACTIVE_ENERGY = "INT32_6_2"
    T2_TOTAL_FORWARD_ACTIVE_ENERGY = "INT32_6_2"
    T3_TOTAL_FORWARD_ACTIVE_ENERGY = "INT32_6_2"
    T4_TOTAL_FORWARD_ACTIVE_ENERGY = "INT32_6_2"
    TOTAL_REVERSE_ACTIVE_ENERGY = "INT32_6_2"
    T1_TOTAL_REVERSE_ACTIVE_ENERGY = "INT32_6_2"
    T2_TOTAL_REVERSE_ACTIVE_ENERGY = "INT32_6_2"
    T3_TOTAL_REVERSE_ACTIVE_ENERGY = "INT32_6_2"
    T4_TOTAL_REVERSE_ACTIVE_ENERGY = "INT32_6_2"
    ACTIVE_TOTAL_POWER = "INT32_6_2"
    T1_TOTAL_ACTIVE_ENERGY = "INT32_6_2"
    T2_TOTAL_ACTIVE_ENERGY = "INT32_6_2"
    T3_TOTAL_ACTIVE_ENERGY = "INT32_6_2"
    T4_TOTAL_ACTIVE_ENERGY = "INT32_6_2"
    TOTAL_FORWARD_REACTIVE_ENERGY = "INT32_6_2"
    T1_TOTAL_FORWARD_REACTIVE_ENERGY = "INT32_6_2"
    T2_TOTAL_FORWARD_REACTIVE_ENERGY = "INT32_6_2"
    T3_TOTAL_FORWARD_REACTIVE_ENERGY = "INT32_6_2"
    T4_TOTAL_FORWARD_REACTIVE_ENERGY = "INT32_6_2"
    TOTAL_REVERSE_REACTIVE_ENERGY = "INT32_6_2"
    T1_TOTAL_REVERSE_REACTIVE_ENERGY = "INT32_6_2"
    T2_TOTAL_REVERSE_REACTIVE_ENERGY = "INT32_6_2"
    T3_TOTAL_REVERSE_REACTIVE_ENERGY = "INT32_6_2"
    T4_TOTAL_REVERSE_REACTIVE_ENERGY = "INT32_6_2"
    TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T1_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T2_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T3_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T4_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    TOTAL_REACTIVE_ENERGY_FIRST_QUADRANT = "INT32_6_2"
    T1_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T2_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T3_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T4_FIRST_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    TOTAL_REACTIVE_ENERGY_SECOND_QUADRANT = "INT32_6_2"
    T1_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T2_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T3_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T4_SECOND_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    TOTAL_REACTIVE_ENERGY_THIRD_QUADRANT = "INT32_6_2"
    T1_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T2_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T3_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T4_THIRD_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    TOTAL_REACTIVE_ENERGY_FOURTH_QUADRANT = "INT32_6_2"
    T1_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T2_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T3_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    T4_FOURTH_QUADRANT_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    RESETTABLE_ACTIVE_TOTAL_POWER = "INT32_6_2"
    RESETTABLE_TOTAL_REACTIVE_ENERGY = "INT32_6_2"
    POSITIVE_ACTIVE_DEMAND = "INT32_6_1"
    FORWARD_MAXIMUM_ACTIVE_DEMAND = "INT32_6_1"
    REVERSE_ACTIVE_DEMAND = "INT32_6_1"
    REVERSE_MAXIMUM_ACTIVE_DEMAND = "INT32_6_1"
    FORWARD_REACTIVE_DEMAND = "INT32_6_1"
    FORWARD_MAXIMUM_ACTIVE_AND_REACTIVE_ENERGY_DEMAND = "INT32_6_1"
    REVERSE_REACTIVE_ENERGY_DEMAND = "INT32_6_1"
    REVERSE_MAXIMUM_ACTIVE_AND_REACTIVE_ENERGY_DEMAND = "INT32_6_1"

    ITEM = "NOT_SUPPORTED"
    MODBUS_ID = "NOT_SUPPORTED"
    SOFTWARE_VERSION_NUMBER = "NOT_SUPPORTED"
    HARDWARE_VERSION_NUMBER = "NOT_SUPPORTED"
    FIRMWARE_CHECKSUM = "NOT_SUPPORTED"
    TIME = "NOT_SUPPORTED"
    ROTATION_TIME = "NOT_SUPPORTED"
    BAUD_RATE_485 = "NOT_SUPPORTED"
    CHECK_DIGIT_485 = "NOT_SUPPORTED"
    STOP_BIT_485 = "NOT_SUPPORTED"
    COMBINED_CODE = "NOT_SUPPORTED"
    DEMAND_MODE = "NOT_SUPPORTED"
    DEMAND_CYCLE = "NOT_SUPPORTED"
    AUTOMATIC_ROTATION_CONTENT = "NOT_SUPPORTED"
    LCD_BUTTON_DISPLAY_SETTING_PASSWORD = "NOT_SUPPORTED"
    METER_RUNNING_TIME = "NOT_SUPPORTED"
    SET_TIMING_CURRENT_VALUE = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_1 = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_2 = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_3 = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_4 = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_5 = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_6 = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_7 = "NOT_SUPPORTED"
    METER_RUNNING_STATUS_WORD_BLOCK = "NOT_SUPPORTED"
    CLEAR_ELECTRICITY = "NOT_SUPPORTED"
    CLEAR_MAX_DEMAND = "NOT_SUPPORTED"

    TIMETABLE_1 = "NOT_SUPPORTED"
    TIMETABLE_2 = "NOT_SUPPORTED"
    TIMETABLE_3 = "NOT_SUPPORTED"
    TIMETABLE_4 = "NOT_SUPPORTED"
    TIMETABLE_5 = "NOT_SUPPORTED"
    TIMETABLE_6 = "NOT_SUPPORTED"
    TIMETABLE_7 = "NOT_SUPPORTED"
    TIMETABLE_8 = "NOT_SUPPORTED"
    TIME_ZONE_TABLE = "NOT_SUPPORTED"
    HOLIDAY_TABLE = "NOT_SUPPORTED"
