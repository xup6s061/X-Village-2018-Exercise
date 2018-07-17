import random
item_in_shop = {"soybean_sauce": 0, "milk": 4, "salt": 10, "soybean_milk": 3}
items = [item for item in item_in_shop.keys()]
cnt = 5

def buy(item):
    # TODO: 補上程式碼和完成邏輯
    # tips: 如果東西數量是 0 需要 raise Exception,否則就把物品的數量減 1 
    if item_in_shop[item]==0:
        raise ValueError("it's sold out")
    else:
        print("Mommy! I've bought {} for you!".format(item))
        item_in_shop[item]-=1
# 買五個隨機的東西
while cnt>0:
    
    index = random.randint(0,3)
    item = items[index]
    try:
        buy(item)
        cnt -= 1
    except ValueError:
        print("it's sold out")

# print(item_in_shop['milk'])