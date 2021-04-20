regex_integer_in_range = r"^\d{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)(?:\d)(\1))"	# Do not delete 'r'.
# (\d)\d\1
# (?=(\d)\d\1)
# (\d)(?=(\d)\1)
# (\d)(?:\d)(\1)+
# (?=((\d)\d\2))
# (\d)(?=(?:\d)(\1))
# do not change the code below
import re
# P = input()
P='454867'

# print(bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P))<2)
print(re.findall(regex_alternating_repetitive_digit_pair,P))