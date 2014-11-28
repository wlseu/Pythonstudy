from logging import exception
from Tools.Scripts.treesync import raw_input


__author__ = 'wl'
# from string import Template
# from math import pi
# format = "Pi with three decimals: %.3f"
# print(format % pi)
# seq = ['1' '2' '3' '4' '5']
# sep = '/'
# print(sep.join(seq))
# '1+2+3+4+5+60'.split('+')
# people ={
#         'wl':
#             {
#                 'phone': '18795899021',
#                 'address': 'shangtangyuan'
#             },
#         'zjr':
#             {
#                 'phone': '18795899013',
#                 'adress': 'shenyuan'
#             },
#
#         }
# labels = {
#           'phone': 'phone num',
#           'address': 'address'
#         }
# request = raw_input('phone num(p) or address(a)?')

#leetcode minstack

# memory exceed


# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minstack = []
#
#
#     # @param x, an integer
#     # @return an integer
#     def push(self, x):
#         if len(self.stack) == 0:
#             self.stack.append(x)
#             self.minstack.append(x)
#         else:
#             self.stack.append(x)
#             if x > self.minstack[-1]:
#                 y = self.minstack[-1]
#                 self.minstack.append(y)
#             else:
#                 self.minstack.append(x)
#
#
#
#     # @return nothing
#     def pop(self):
#         if len(self.stack) == 0:
#             raise exception ("stack is empty")
#         else:
#             self.minstack.pop()
#             self.stack.pop()
#
#
#
#
#     # @return an integer
#     def top(self):
#         return self.stack[-1]
#
#     # @return an integer
#     def getMin(self):
#         return self.minstack[-1]


### AC

#--*-- coding:utf-8 --*--
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []
#     # @param x, an integer
#     # @return an integer
#     def push(self, x):
#         self.stack.append(x)
#         if len(self.minStack) == 0 or x < self.minStack[-1][0]: #小于最小值
#             self.minStack.append((x, 1))
#         elif x == self.minStack[-1][0]: #等于最小值
#             self.minStack[-1] = (x, self.minStack[-1][1] + 1)
#     # @return nothing
#     def pop(self):
#         if self.top() == self.getMin(): #pop的值为最小值
#             if self.minStack[-1][1] > 1:
#                 self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
#             else:
#                 self.minStack.pop()
#         self.stack.pop()
#     # @return an integer
#     def top(self):
#         return self.stack[-1]
#     # @return an integer
#     def getMin(self):
#         return self.minStack[-1][0]


#https://oj.leetcode.com/problems/merge-intervals/

# class Interval:
#
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
# class Solution:
#
#     # @param intervals, a list of Interval
#     # @return a list of Interval
#     def merge(self, intervals):
#
#         if len(intervals) <= 1:
#             return intervals
#
#         intervals.sort(lambda x, y: cmp(x.start, y.start))
#         new_intervals = [ ]
#         last_interval = intervals[0]
#         for i in range(1, len(intervals)):
#             if intervals[i].start >= last_interval.start and intervals[i].start <= last_interval.end:
#                 if intervals[i].end >= last_interval.start and intervals[i].end <= last_interval.end:
#                     pass
#                 else:
#                     last_interval.end = intervals[i].end
#             else:
#                 new_intervals.append(last_interval)
#                 last_interval = intervals[i]
#         new_intervals.append(last_interval)
#
#         return new_intervals