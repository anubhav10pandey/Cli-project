from datetime import datetime

def update_file(text,file_name="db.text"):
    date_str=datetime.now()
    file = open(file_name, 'a')
    file.write(f"{date_str}=>{text}\n")
    file.close()

    

def find_entery(query,file_name="db.text"):
    file = open(file_name, 'r')

    for entery in file.readlines():
         if query.lower() in entery.lower():
             print(entery)
    file.close()



option_1 = input("1: New Entery\n2: Search Entery\n-> ")

if option_1 =='1':

    new_entery=input("Plz Enate Your Entery\n-> ")
    update_file(new_entery)
elif option_1 =='2':
    search_query=input("Plz Enater matching string\n-> ")
    find_entery(search_query)

    

else:
    print("Not A Valid Option.")






