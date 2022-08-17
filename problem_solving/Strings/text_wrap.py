#Problem: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    counter = (len(string) // max_width) + 1

    list1 = []
    list1[:0] = string

    for i in range(counter):
        list1.insert((max_width + 1) * i, "\n")

    list1.pop(0)
    result = "".join(list1)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

