# ......CONTACT BOOK.......#
  
import string as str

name=[]
email_id=[]
mobile_no=[]

count_sno=0

with open('contact.txt','a+') as std:
    std.write('S.NO: \t \t NAME: \t \t \t \t MAIL ID: \t \t \t \t \t \t \t \t PHONE NUMBER: \n')
    
    while True:
        Name=input('Enter Your Name: ')
        Email_id=input('Enter Your Email Id: ')
        Mobile_No=int(input('Enter Your Mobile Number: '))
        
        name.append(Name)
        email_id.append(Email_id)
        mobile_no.append(Mobile_No)
        
        std.write(f'{count_sno+1} \t \t {name[count_sno]} \t \t \t \t \t \t \t {email_id[count_sno]} \t \t \t \t \t {mobile_no[count_sno]} \n')
        
        count_sno +=1
        
        add_details=input('Enter any (alphabetic) character if you want to add more details: ')
        
        if add_details not in str.ascii_letters :
            break
                
            
std_info=('contact.txt')
print(std_info.read())
        
        
search_details = input('To check whether the given information is stored or not : ')
while True: 
    if search_details in name :
        enter_details = name.index(search_details)
        email_id = email_id[enter_details]
        mobile_no =mobile_no[enter_details]
            
        print(f'Name: {search_details}, Email-id: {email_id}, Mobile Number: {mobile_no}')
                
    else :
        print("Name Not Found")
            
    search_details=input('Enter any (alphabetic) character if you want to search more details: ')
        
    if search_details not in str.ascii_letters :
        break
                
                
        
