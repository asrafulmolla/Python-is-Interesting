from food_item import FoodItem
from menu import Menu
from user import Customer, Admin, CustomerNew
from restaurent import Restaurant
from orders import Order


mamar_res=Restaurant('Mamar Restaurent')
def customer_menu():
    name=input('\nEnter Your Username: ')
    if Restaurant.find_customer(mamar_res,name) is not None:
        email=input('Enter Your email: ')
        address=input('Enter Your Address: ')
        
        customer=Customer(name=name, email=email, address=address)
        
        while True:
            print (f'\nWelcome {customer.name} !!')
            print ('1. View Manu')
            print ('2. Add item to card')
            print ('3. View Card')
            print ('4. Pay Bill')
            print ('5. Add Blance in Your Wallet')
            print ('6. View Current Blance in your Wallet')
            print ('7. View List of Past Orders')
            print ('8. Exit')
            
            choice=int (input('Enter Your Choice: '))
            if choice == 1:
                customer.view_menu(mamar_res)
            elif choice ==2:
                item_name=input('Enter Item Name: ')
                item_quantity=int (input('Enter Item Quantity: '))
                customer.add_to_cart(mamar_res, item_name,item_quantity)
            elif choice ==3:
                customer.view_cart()
            elif choice==4:
                customer.pay_bill()
            elif choice ==5:
                amount=int (input('Enter Blance added in your wallet: '))
                customer.add_blance(amount)
            elif choice ==6:
                print (f'Current Blance in Your Wallet: {customer.wallet}\n')
            elif choice ==7:
                customer.view_past_order()
            elif choice==8:
                break
            else:
                print('Invalid Choice...Please Try Again\n')
                
    else:
        print (f'{name} invalid username\n')
        
def admin_menu():
    name=input('\nEnter Your Username: ')
    if name=='Admin':  #admin user name
        email=input('Enter Your email: ')
        address=input('Enter Your Address: ')
        
        admin=Admin(name=name, email=email, address=address)
        
        while True:
            print (f'\nWelcome {admin.name} !!')
            
            print ('1. Add New Customer')
            print ('2. Delet Customer')
            print ('3. View Customers')
            print ('4. Add New Item')
            print ('5. Delet Item')
            print ('6. View Items Details')
            print ('7. Update  Item Price')
            print ('8. Exit')
            
            choice=int (input('Enter Your Choice: '))
            if choice == 1:
                name=input('Enter Customer Name: ')
                email=input('Enter Customer Email: ')
                address=input('Enter Customer Address: ')
                Customer=CustomerNew(name, email, address)
                admin.add_customer(mamar_res, Customer)
            elif choice ==2:
                customer_name=input('Enter Delete Customer Name: ')
                admin.remove_customer(mamar_res,customer_name)
            elif choice ==3:
                admin.view_customer(mamar_res)
            elif choice==4:
                item_name=input('Enter Item Name: ')
                item_price=input('Enter Item Price: ')
                item_quantity=input('Enter Item Quantity: ')
                item=FoodItem(item_name,item_price,item_quantity)
                admin.add_new_item(mamar_res,item)
            elif choice==5:
                item_name=input('Enter Delete Item Name: ')
                admin.remove_item(mamar_res,item_name)
            elif choice==6:
                admin.view_menu(mamar_res)
            elif choice==7:
                item_name=input('Enter Update Price Item Name: ')
                update_rate=input('Enter Update Price Item Name: ')
                admin.update_price(mamar_res,item_name,update_rate)
            elif choice==8:
                break
            else:
                print('Invalid Choice...Please Try Again')
            
    else:
        print (f'{name} user name Invalid... Admin user name is Admin')
        
while True:
    print ('\n**********Welcome***********')
    print ('1. Admin Login')
    print ('2. Customer Login')
    print ('3. Exit')
    
    choice=int(input('Enter Your Choice: '))
    
    if choice==1:
        admin_menu()
    elif  choice==2:
        customer_menu()
    elif choice==3:
        break
    else:
        print ('Invalid Choice. Please Try Again........')