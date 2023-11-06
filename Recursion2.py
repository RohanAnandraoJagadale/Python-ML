import sys

print(sys.getrecursionlimit())   # 1000 stack frame

sys.setrecursionlimit(3001)      # limit change keli // ass karu naye

print(sys.getrecursionlimit())
