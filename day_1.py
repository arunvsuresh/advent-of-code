import pandas as pd 
import re

# create two pointers - one for first digit and one for last digit
# check to see if each calibration string has just one digit, if so sum that digit twice
def sum_calibration_values(input_txt):

    df = pd.read_csv(input_txt, header=None, sep=" ")
    calibration_values = df[0].tolist()
    # first_digit = 0
    # last_digit = -1
    outer_sum = 0
    for calibration_value in calibration_values:
        inner_sum = 0
        # for char in calibration_value:
        res = re.split(r'[a-z]*', calibration_value)
        res = [chr for chr in res if len(chr) == 1]
        inner_sum += int(res[0]) + int(res[-1])
        outer_sum += inner_sum
    return outer_sum

print(sum_calibration_values("input.txt"))