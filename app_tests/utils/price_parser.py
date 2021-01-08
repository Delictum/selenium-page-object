import re


def get_price_from_str(s: str):
    nums = re.findall(r'\d*[.,]\d+|\d+', s)
    return float(nums[0].replace(',', '.'))
