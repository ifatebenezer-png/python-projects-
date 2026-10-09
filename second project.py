# >>>>>>INTERACTIVE SHOPPING CART<<<<<<<
inventory={"tomato":80,"potato":60,"apple":200,"banana":80,"water":40};

shopping_cart=[] ## an empty list that holds the persons objects that he's gonna buy

while True:
    print(">>>>>>PLEASE CHOOSE WHAT TO DO<<<<<<")
    print()
    print("1, view the available items 🍅🍎🍏🍌🥔")
    print("2, add item to cart 🛒🛒🛒")
    print("3, remove from cart ")
    print("4, checkout ")
    print("5, exit program 👋👋👋")
    print()
    choice=int(input("chosse an option to perform: "))
    if choice not in range(1,7):
        print("ERROR: choice does't exist")

    if choice==1:
        print('>>>> AVAILABLE ITEMS <<<<')
        for item,price in inventory.items():
            print(f'{item}>>> costs{price}')
    elif choice==2:
        print('>>> ADD ITEM <<<')
        added_items=input("enter the name of the object you wanna buy: ")
        if added_items in inventory:
            shopping_cart.append(added_items)
            print("items has been added 👍👍👍")
        else:
            print("that item does't exist! 🚫🚫🚫")
    elif choice==3:
        print(">>> remove items <<<")
        if not shopping_cart:
            print(" your cart is empty ther's nothing to remove")
        else:
            items_to_remove=input("enter the items to remove from your cart: ")
            if items_to_remove in shopping_cart:
                shopping_cart.remove(items_to_remove)
                print(f'{items_to_remove} has been removed from your cart')
            else:
                print("item wasn't inyour cart")
    elif choice==4:
        print(">>> checking out <<<")
        total_price=sum(inventory[item] for item in shopping_cart)
        print(f' thanks for shopping with us your final total is {total_price} birr')
        print("we accept cash, credit card, mobile banking!!")
        break
    elif choice==5:
        break

                




    
    