# def gift(gift_1:int,gift_2:int,gift_3:int,gift_4:int,gift_5:int):

#     if (gift_1 > gift_2 and gift_1 > gift_3 and gift_1 > gift_4 and gift_1 > gift_5):
#         return print("1")
#     elif (gift_2 > gift_1 and gift_2 > gift_3 and gift_2 > gift_4 and gift_2 > gift_5):
#         return print("2")
#     elif (gift_3 > gift_1 and gift_3 > gift_2 and gift_3 > gift_4 and gift_3 > gift_5):
#         return print("3")
#     elif (gift_4 > gift_1 and gift_4 > gift_2 and gift_4 > gift_3 and gift_4 > gift_5):
#         return print("4")
#     elif (gift_5 > gift_1 and gift_5 > gift_2 and gift_5 > gift_4 and gift_5 > gift_3):
#         return print("5")


# gift_1 = int(input())
# gift_2 = int(input())
# gift_3 = int(input())
# gift_4 = int(input())
# gift_5 = int(input())
# gift(gift_1, gift_2, gift_3, gift_4, gift_5)

g1 = int(input())
g2 = int(input())
g3 = int(input())
g4 = int(input())
g5 = int(input())

gifts = [g1, g2, g3, g4, g5]

max_value = max(gifts)
print(gifts.index(max_value) + 1)