"""Little utility for calculating how long it will take, without buffs, to get to a target number of cookies."""

import datetime

# fill in your current CPS.
cps = 1
cps_units = 'thousand'

# fill in the current number of cookies you have.
current_cookies = 1
current_units = 'thousand'

# fill in the number of cookies you want.
target_cookies = 1
target_units = 'thousand'

scales = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion",
          "sextillion", "septillion", "octillion"]

def calculate_value(number, units):
	idx = scales.index(units) + 1
	outp_value = number * 1000 ** idx
	return outp_value

calculated_cps = calculate_value(cps, cps_units)
calculated_current = calculate_value(current_cookies, current_units)
calculated_target = calculate_value(target_cookies, target_units)

time_in_seconds = (calculated_target - calculated_current) / calculated_cps
converted_time = str(datetime.timedelta(seconds=time_in_seconds))

print("time until target cookies: {}".format(converted_time))