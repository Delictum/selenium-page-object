import re


def get_price_from_str(s: str):
    nums = re.findall(r'\d*\.\d+|\d+', s)
    num = nums[0] + "." + nums[1]
    return float(num)
