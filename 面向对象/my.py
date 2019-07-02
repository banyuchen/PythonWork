
# # 单例模式
# class A:
#     __instance = False
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance:
#             return cls.__instance
#         cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#
# a = A('12', 2)
# a.cloth = '小花袄'
# a1 = A('32', 4)
# print(a.name)
# print(a1.name)
# print(a1.cloth)


# from collections import namedtuple
# from random import choice
#
# Card = namedtuple("Card", ["rank", "suit"])
#
#
# class FranchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list("JQKA")
#     suits = ["红心", "方块", "梅花", "黑桃"]
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for rank in FranchDeck.ranks
#                                         for suit in FranchDeck.suits]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return self._cards[item]
#
#
# deck = FranchDeck()
# print(deck[0])
# print(choice(deck))
# print(choice(deck))
