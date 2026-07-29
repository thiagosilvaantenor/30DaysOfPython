# 2) Use a defaultdict to store a count for each character 
# that appears in a given string. 
# Print the most common character in this dictionary.

from collections import defaultdict

chars = defaultdict(int)

words = {1: 'paralelepipedo', 2: 'lalelilelu'}

for value in words.values():
    for key in value:
        chars[key] += 1

most_value = max(chars,key=lambda key: chars[key])
print(f"most commom character: '{most_value}', it appers {chars.get(most_value)} times on the set")

# for key,value in chars.items():
#     if value == most_value:
#         print(f"most commom character: '{key}', it appers {value} times on the set")
#         break
