#https://www.hackerrank.com/challenges/incorrect-regex/problem?h_r=internal-search
import re
for _ in range(int(input())):
    try:
        re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
