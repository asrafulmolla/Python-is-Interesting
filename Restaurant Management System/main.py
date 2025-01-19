from food_item import FoodItem
from menu import Menu
from user import Customer, Admin, Employee
from restaurent import Restaurant
from orders import Order


mamar_res=Restaurant('Mamar Restaurent')
def customer_menu():
    name=input('Enter Your Name: ')
    email=input('Enter Your email: ')
    phone=input('Enter Your phone: ')
    address=input('Enter Your Address: ')
    
    customer=Customer(name=name, phone=phone, email=email, address=address)
    
    while True:
        print (f'Welcome {customer.name} !!')
        print ('1. View Manu')
        print ('2. Add item to card')
        print ('3. View Card')
        print ('4. Pay Bill')
        print ('5. Exit')
        
        choice=int (input('Enter Your Choice: '))
        if choice == 1:
            customer.view_menu(mamar_res)
        elif choice ==2:
            item_name=input('Enter Item Name: ')
            item_quantity=input('Enter Item Quantity: ')
            customer.add_to_cart(mamar_res, item_name,item_quantity)
            
        elif choice ==3:
            customer.view_cart()
            
        elif choice==4:
            customer.pay_bill()
            
        elif choice==5:
            break
        else:
            print('Invalid Choice...Please Try Again')
            
def admin_menu():
    name=input('Enter Your Name: ')
    email=input('Enter Your email: ')
    phone=input('Enter Your phone: ')
    address=input('Enter Your Address: ')
    
    admin=Admin(name=name, phone=phone, email=email, address=address)
    
    while True:
        print (f'Welcome {admin.name} !!')
        print ('1. Add New Item')
        print ('2. Add New Employee')
        print ('3. View Employee')
        print ('4. View Items')
        print ('5. Delet Items')
        print ('6. Exit')
        
        choice=int (input('Enter Your Choice: '))
        if choice == 1:
            item_name=input('Enter Item Name: ')
            item_price=input('Enter Item Price: ')
            item_quantity=input('Enter Item Quantity: ')
            item=FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_res,item)
        elif choice ==2:
            name=input('Enter Employee Name: ')
            phone=input('Enter Employee Phone: ')
            email=input('Enter Employee Email: ')
            designation=input('Enter Employee Designation: ')
            age=input('Enter Employee Age: ')
            salary=input('Enter Employee Salary: ')
            Address=input('Enter Employee Address: ')
            employee=Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(mamar_res, employee)
            
        elif choice ==3:
            admin.view_employee(mamar_res)
            
        elif choice==4:
            admin.view_menu(mamar_res)
            
        elif choice==5:
            item_name=input('Enter Delete Item Name: ')
            admin.remove_item(mamar_res,item_name)
        elif choice==6:
            break
        else:
            print('Invalid Choice...Please Try Again')
            
while True:
    print ('**********Welcome***********')
    print ('1. Customer')
    print ('2. Admin')
    print ('3. Exit')
    
    choice=int(input('Enter Your Choice: '))
    
    if choice==1:
        customer_menu()
    elif  choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print ('Invalid Choice. Please Try Again........')