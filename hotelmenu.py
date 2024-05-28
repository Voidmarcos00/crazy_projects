menu = {'pizza':40, "pasta":50, "coffee":60, "salad":40, "ice-cream":80}

print("******** Welcome to RAHUL cafe **********\n")
print("pizza     :   $40.00\npasta     :   $50.00\ncoffee    :   $60.00\nsalad     :   $40.00\nice-cream :   $80.00\n")

order_total = 0
 
item_1 = input("enter your first order = \n")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order") 

else:
    print(f"ordered item {item_1} is not available")

while True:
 another_item = input("do you want to add another item ?(yes/no)")

 if another_item == "yes":
    item2 = input ("enter your next item = \n")
    if item2 in menu:
        order_total += menu[item2]
        print(f"your item {item2} has been added to your order")     
    else:
     print(f"ordered item {item2} is not available")
 if another_item == "no":    
    break    

print(f"the total amount of items is ${order_total}")     