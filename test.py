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


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []


    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minstack.append(x)
        else:
            self.stack.append(x)
            if x > self.minstack[-1]:
                self.minstack.append(self.minstack[-1])
            else:
                self.minstack.append(x)



    # @return nothing
    def pop(self):


    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minstack[-1]