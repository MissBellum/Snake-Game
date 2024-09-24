from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('crimson')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        rand_x = randint(-230, 230)
        rand_y = randint(-230, 230)
        self.goto(x=rand_x, y=rand_y)

# alls = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# #print(alls[3:4])
# from random import randint
# alld = ['1', '2', '3', '4', '5', '6', '7'] #input().split() 
# new = [int(item) * int(item) for item in alld if int(item) % 2 == 0]
# print(new)
# with open('list1', 'r') as one:
#     uno = [item.strip() for item in one.readlines()]
#     print(uno)
# with open('list2', 'r') as too:
#     duo = [item.strip() for item in too.readlines()]
#     print(duo)
# new = [key for key in uno if key in duo]
# print(new)
# dits = {key: randint(0, 9) for key in alld if key in duo}
# print(dits)
# nw = {dits[key]: randint(90, 110) for key in dits}
# print(nw)
# #sent = eval(input())
# #nw = {key: len(key) for key in sent.split()}
# #print(sent)
# def foo(a, b=True, c=3):
#     print(a, b, c)
# foo(1, False)
# def foo(*args):
#     return args
# nw = foo(2, 5, 7, '9', 'g', 'sk1', {2: 'r'})
# print(nw[::-1])
# class Sutn():
#     def __init__(self, **kwargs) -> None:
#         self.jump = kwargs.get('jump')
#         self.move = kwargs.get('move')
#         self.help = kwargs.get('help')
#         self.times(100, 3, 65)

#     def times(self, b, n, p):
#         self.jump = b
#         self.move = n
#         self.help = p
#         return b * n + p
    
# sn = Sutn()
# print(sn.help)
# print(sn.times(100, 3, 65))

# try:
#     with open
