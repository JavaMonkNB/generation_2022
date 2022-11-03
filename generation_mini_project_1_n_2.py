products = ['Coke Zero', 'Pepsi', 'Sprite', 'Tango', 'Lemonade']    # initial product list 
# to add a product to the list use products.append('?')

user_menu_1_input = ''
def menu_1():
    print('[1] enter Product Menu')
    print('[0] Exit the Program')

user_menu_2_input = ''
def menu_2():
    print('[0] Return to Previous Menu ')
    print('[1] List of Available Products ')
    print('[2] Add New Product ')
    print('[3] Update Existing Product' )
    print('[4] Delete Current Product')

def menu_order():
    print('')
    print('[0] Return to Main Menu ')       # return to menu()_1
    print('[1] PRINTS order Dictionary')
    print('[2] Add New Product ')
    print('[3] Update Existing Product' )
    print('[4] Delete Current Product')

update_product_index = ''
update_product_name = ''
want_to_order = ''
make_order = ''
want_to_add_product = ''
new_added_product_name = ''

order_status_list = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]

order = [
{
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
},
{
    "customer_name": "Boris",
    "customer_address": "Unit 10, 10 Downing Street, LONDON, SW1 ",
    "customer_phone": "0789887334",
    "status": "Awaiting Pickup"
},
{
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "Out For Delivery"
},
{
    "customer_name": "Liz",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "Delivered"
}

]

menu_1()
user_menu_1_input = int(input('Enter your option please: '))
if user_menu_1_input == 1:
    print()
    print('Welcome to the Product Menu, Please Make Your Selection ')
    menu_2()
    user_menu_2_input = int(input('Enter your option please: '))
    if user_menu_2_input == 0:  # i need a function here
        print('welcome Back To The Main Menu, Please Make Your Selection')
        menu_1()
        user_menu_1_input = int(input('Enter your option please: '))
        print('Welcome to the Product Menu, Please Make Your Selection ')
        menu_2()
    elif user_menu_2_input == 1:
        print('These Are The Products Currently Available \n')
        for index, value in enumerate(products):
            print(index, value)
        print()
        want_to_order = input('Do you want to place an Order, enter 1 for yes and 0 for No ')
        menu_order()
        make_order = int(input('Enter the corresponding menu number '))
        if make_order == 0:
            menu_1
        elif make_order == 1:   # prints order dictionary 
            print('Prints Order Dictionary')
        elif make_order = 2:
            products.item(index, value )        




    #if user_menu_2_input == 0:   # int(input('Enter your option please: '))
    #print('Welcome to the Product Menu, Please Make Your Selection ')
    #menu_1()
    #elif user_menu_2_input != 0:
    #elif user_menu_2_input == 1:
    #    menu_2
    
    elif user_menu_2_input == 2:
        want_to_add_product = input(' Do you want to add a new product \n Enter 0 for No or Enter 1 for Yes ')
        if want_to_add_product == 1:
            new_added_product_name = input('What Is the Name of The New Product ')
            # new_added_product_index = int(input('What is The Index Number of The New Product'))
            products.append(new_added_product_name)
            # products.insert() 
            print('products')
        #if want_to_add_product == y:

        print(*products, sep=',')   # used to list items and remove square brackets and quotes


    elif user_menu_2_input == 3:    
        while True:
            new_product_name = input('Enter the Name of New Product  ') # remember append adds one item at a time
            products.append(new_product_name)
            #add_another_product = input('Do You Want To Add Another Product? (y / n): ')
            #if add_another_product.lower == 'n':
                #break

        for product in products:
            print('the current Products')
            print(product)
 
    elif user_menu_2_input == 3:
        for index, value in enumerate(products): # to print list index and values 
            print(index, value)
        # print(list(enumerate(products))) # this does the same thing too
        update_product_index = int(input('Enter the Number Index of Product to be Updated  '))
        update_product_name = input('What is the Name of The New Updated Product ')
        # products[upate_product_index] = [update_product_name]
        products[update_product_index, update_product_name]




            # catch a valueError exception 
        

    elif user_menu_2_input == 4:
        print('You have decieded to delete a product')
        # print(list(enumerate(products)))  # this also prints out the name and index of the list items
        for index, value in enumerate(products):
            print(index, value)
        user_product_delete = int(input('Enter the Index Number of the Product You Want To Delete '))
        del products[user_product_delete]           # slicing                           
        # products.remove([user_product_delete])    # this works for the product names
        print(list(enumerate(products)))    # catch a valueError exception

else:
    print('Please enter 0 0r 1 ')



















