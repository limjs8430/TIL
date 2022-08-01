# https://www.acmicpc.net/problem/1076

from sys import stdin

color = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange': 3, 'yellow' : 4, 'green' : 5,
            'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}

first = stdin.readline().strip()
second= stdin.readline().strip()
third = stdin.readline().strip()

print((color[first]*10 + color[second]) * (10 ** color[third]))