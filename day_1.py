import pandas as pd 
import re
import time

# edge case: check to see if each calibration string has just one digit, if so sum that digit twice
def sum_calibration_values(input_txt):

    df = pd.read_csv(input_txt, header=None, sep=" ")
    calibration_values = df[0].tolist()    
    sum = 0
    for calibration_value in calibration_values:
        matches = list(re.finditer(r'\d', calibration_value))
        sum += int(matches[0].group() + matches[-1].group())
    return sum
start = time.time()
print(sum_calibration_values("input.txt"))
end = time.time()
print('time to run...', end - start)