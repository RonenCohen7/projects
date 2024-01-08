sim_password.py
import os
import faker
from faker import Faker
import colorama
from colorama import Fore, Back, Style
import datetime
import sys
import hashlib
import json
import glob
import shutil
import uuid
import time
import pyodbc

f = Faker(["en_US"])
now = datetime.datetime.now()


def manu():
    print(Fore.LIGHTRED_EX + '''


        ███████╗██╗   ██╗██████╗ ███╗   ███╗ █████╗ ██████╗ ██╗███╗   ██╗███████╗███████╗    ██╗███╗   ██╗    ████████╗██╗  ██╗███████╗    
        ██╔════╝██║   ██║██╔══██╗████╗ ████║██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔════╝    ██║████╗  ██║    ╚══██╔══╝██║  ██║██╔════╝    
        ███████╗██║   ██║██████╔╝██╔████╔██║███████║██████╔╝██║██╔██╗ ██║█████╗  ███████╗    ██║██╔██╗ ██║       ██║   ███████║█████╗      
        ╚════██║██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║██╔══██╗██║██║╚██╗██║██╔══╝  ╚════██║    ██║██║╚██╗██║       ██║   ██╔══██║██╔══╝      
        ███████║╚██████╔╝██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║██║██║ ╚████║███████╗███████║    ██║██║ ╚████║       ██║   ██║  ██║███████╗    
        ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝    ╚═╝╚═╝  ╚═══╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    

                                    ██████╗ ███████╗███████╗███████╗██████╗ ████████╗                                                      
                                    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝                                                      
                                    ██║  ██║█████╗  ███████╗█████╗  ██████╔╝   ██║                                                         
                                    ██║  ██║██╔══╝  ╚════██║██╔══╝  ██╔══██╗   ██║                                                         
                                    ██████╔╝███████╗███████║███████╗██║  ██║   ██║                                                         
                                    ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝                                                         
    ''', '\n', end="\r", flush=True)
    current_date = datetime.date.today()  # year - mount - dat
    time = now.strftime("%H:%M:%S")
    cnt = 0
    path = r"C:\Python\sim_pass"
    for file in glob.glob(path + '\*.json'):
        if file.endswith('.json'):
            shutil.copy(file, r"C:\temp\sim_password\Customers")
            os.remove(file)
            print(Fore.RED + str('[+] The system performs updates files have been moved to secure mode\n'.title()) + Fore.RESET)

    path = r"C:\\temp\\sim_password\\Customers\\"
    for _ in glob.glob(path + '*.json'):
        os.listdir(path)
        cnt += 1
    print(Fore.LIGHTMAGENTA_EX + str(f'[+] total json file in path: {cnt},  {current_date},  {time}\n'.title()) + Fore.RESET)

    print(Fore.BLUE + str('[+] in this program we create Submarines in the desert = FAKER file\n'
                          '[+] hashing the password\n'
                          '[+] In addition we save the parameters on CSV file\n'.title()) + Fore.RESET)

    print(Fore.BLUE + str(current_date) + '\t' + '\t' + str(time) + '\t' + '\t' +Fore.RED + Style.DIM +('Creted By Ronen Cohen'.title()) +Style.NORMAL + Back.RESET + Fore.RESET)
    get_in = input(Fore.LIGHTMAGENTA_EX + str('[+] hello, if you exists in the system please click on x key\n'.title()) + Fore.RESET)
    if get_in == 'X' or get_in == 'x':
        ans = input(Fore.LIGHTCYAN_EX + str('[+] Enter your password'.title() + Fore.RESET))
        print(Fore.LIGHTRED_EX + str('[+] check if you in sys...'.title() + Fore.RESET))
        str_password = hashlib.sha3_256(ans.encode('utf-8')).hexdigest()
        path = r"C:\\temp\sim_password\Customers\\"
        for file in glob.glob(path + '*.json'):
            print(Fore.LIGHTRED_EX + str('[+] steel check if you in sys...'.title() + Fore.RESET))
            with open(file, "r") as json_file:
                json_object = json.load(json_file)
                password = json_object["password"]
                if str_password in json_object["password"]:
                    print(Fore.CYAN + str(f'[+] welcome to the system {json_object["first_name"]}'.title()) + Fore.RESET)
                    Q = input(Fore.CYAN + str(f'[+] do you want to upgrade your data?, press Y/N'.title()) + Fore.RESET)
                    if Q == 'y' or Q == 'Y':
                        print(Fore.LIGHTYELLOW_EX + str(f'[+] moving to upgrade modul, do you know the Data you want\n'
                                                        f'[+] to upgrade. i present to you all the data file'.title() + Fore.RESET))
                        #print(file)
                        with open(file, "r") as json_file:
                            data = json_file.read()
                            print(data)
                            con = input(Fore.LIGHTYELLOW_EX + str(f'[+] do you want to continue press on C or exit press Q'.title()) + Fore.RESET)
                            if con == 'c' or con == 'C':
                                print(Fore.LIGHTYELLOW_EX + str(
                                    f'[+] i present the data from the file for you\n'
                                    f'[+] if you wants to upgrade your email click on E\n'
                                    f'[+] if you wants to upgrade your mobile click on M'.title() + Fore.RESET))
                                with open(file, "r") as json_file:
                                    data = json.load(json_file)
                                print(data)
                                ans = input(Fore.CYAN + str('[+] what a field you wants to upgrade? if its email click on E or if its mobile click on M'.title())+ Fore.RESET)
                                if ans == 'e' or ans == 'E':
                                    new_mail = input(Fore.CYAN + str('[+] please add your new email'.title()) + Fore.RESET)
                                    data['email'] = str(new_mail)
                                    with open(file, "w") as json_file:
                                        json.dump(data, json_file, indent=4)
                                    print(Fore.BLUE + str('[+] upgrade success'.title()) + Fore.RESET)
                                    print(Fore.LIGHTYELLOW_EX + str('[+] tank you'.title()) + Fore.RESET)
                                elif ans == 'm' or ans == 'M':
                                    mobile_number = input(Fore.CYAN + str('[+] please add your new mobile'.title()) + Fore.RESET)
                                    data['mobile_number'] = str(mobile_number)
                                    with open(file, "w") as json_file:
                                        json.dump(data, json_file, indent=4)
                                    print(Fore.BLUE + str('[+] upgrade success'.title()) + Fore.RESET)
                                    print(Fore.LIGHTYELLOW_EX + str('[+] tank you'.title()) + Fore.RESET)
                                    manu()
                            else:
                                if con == 'Q' or con == 'q':
                                    manu()
                    else:
                        manu()
                else:
                    print(Fore.LIGHTMAGENTA_EX + str('[+] your pass not valid, lets create to you a new login count...'.title() + Fore.RESET))
                    manu()
    else:
        ans = input(Fore.MAGENTA + str('[+] add your pass'.title() + Fore.RESET))
        str_password = hashlib.sha3_256(ans.encode('utf-8')).hexdigest()
        path = r"C:\\temp\sim_password\Customers\\"
        for file in glob.glob(path + '*.json'):
            with open(file, "r") as json_file:
                json_object = json.load(json_file)
                password = json_object["password"]
                if str_password in json_object["password"]:
                    print((Fore.LIGHTMAGENTA_EX + str('[+] hello, you exists in the system'.title()) + Fore.RESET))
                    manu()

        id_number = input(Fore.LIGHTYELLOW_EX + str(
            '[+] please enter your id number or,  if you click on k i create an id for you'.title()) + Fore.RESET)
        if id_number == 'k' or id_number == 'K':
            len(id_number) != 11
            id_number = f.ssn()
            print(Fore.LIGHTCYAN_EX + f'[+] ok i create id number -{id_number} for you, lets continue.'.title() + Fore.RESET)
        elif len(id_number) != 9:
            print(Fore.RED + str('[+] id number must be correct - 9 number only'.title()) + Fore.RESET)
            manu()
        path = r"C:\temp\sim_password\\Customers\\"
        for file in glob.glob(path + '*.json'):
            with open(file, 'r', encoding='utf-8') as json_file:
                json_object = json.load(json_file)
                if id_number in json_object["id_number"]:
                    print(Fore.RED + f'[+]{id_number} is already Exists'.title() + Fore.RESET)
                    manu()

        fn = input(Fore.LIGHTYELLOW_EX + str(
            '[+] please enter your first name, if you click on k i create id for you'.title()) + Fore.RESET)
        if fn == 'k' or id_number == 'K':
            fn = f.first_name()
            print(Fore.LIGHTCYAN_EX + f'[+] ok i create a first name-{fn} for you, lets continue.'.title() + Fore.RESET)

        ln = input(Fore.LIGHTYELLOW_EX + str(
            '[+] please enter your last name, if you click on k i create id for you'.title()) + Fore.RESET)
        if ln == 'k' or id_number == 'K':
            ln = f.last_name()
            print(Fore.LIGHTCYAN_EX + f'[+] ok i create a last name-{ln} for you, lets continue.'.title() + Fore.RESET)

        mobile_number = input(Fore.LIGHTYELLOW_EX + str(
            '[+] please enter your mobile number, if you click on k i create a number for you'.title()) + Fore.RESET)
        if mobile_number == 'k' or id_number == 'K':
            mobile_number = f.phone_number()
            print(Fore.LIGHTCYAN_EX + str(
                f'[+] ok i created, from now your mobile number is: {mobile_number}, lets continue.'.title()) + Fore.RESET)
        pasword1 = ans  # input(Fore.LIGHTGREEN_EX + str('[+] please enter your password'.title()) + Fore.RESET)
        pasword2 = input(Fore.LIGHTGREEN_EX + str('[+] please renter your password'.title()) + Fore.RESET)
        if ans != pasword2:
            print(Fore.RED + str('[+][+] You must Enter Precise password Please Try again [+][+]'.title()))
            manu()
        str_password = hashlib.sha3_256(pasword1.encode('utf-8')).hexdigest()

        email = input(Fore.LIGHTYELLOW_EX + str(
            '[+] please enter your email, if you click on k i create email for you'.title()) + Fore.RESET)
        if email == 'k' or id_number == 'K':
            email = f.email()
            print(Fore.LIGHTCYAN_EX + str(
                f'[+] ok i create a new email: {email} for you, lets continue.'.title()) + Fore.RESET)

        print(Fore.CYAN + str('[+] The system performs updates and collect mor Details...'.title()) + Fore.RESET)

        ipv4_privet = f.ipv4_private()
        ipv4_public = f.ipv4_public()
        port_number = f.port_number()
        user_name = f.user_name()
        f_path = f.file_path(depth=5)
        domain_name = f.domain_name()
        macaddress = f.hexify(text="MAC: ^^:^^:^^:^^:^^:^^".upper())
        event_id = uuid.uuid4()
        print(Fore.CYAN + str('[+] The system performs updates and collect mor Details...'.title()) + Fore.RESET)


        print(Fore.CYAN + str('[+] The system collect Details like IP, Ports, Users, MACADDRESS..'.title()) + Fore.RESET)
        dictionary = {
            "time": str(time),
            "date": str(current_date),
            "event_id": str(event_id),
            "id_number": str(id_number),
            "first_name": str(fn),
            "last_name": str(ln),
            "mobile_number": str(mobile_number),
            "password": str(str_password),
            "email": str(email),
            "ipv4_privet": str(ipv4_privet),
            "ipv4_public": str(ipv4_public),
            "port_number": str(port_number),
            "user_name": str(user_name),
            "domain_name": str(domain_name),
            "macaddress": str(macaddress),
            "path": str(f_path)
        }
        path = "C:\\Temp\\sim_password\\"
        fn = fn + '.json'
        for file in glob.glob(path + '*'):
            ext = os.path.split(file)[-1].lower()
            if ext == fn:
                print(f'[+] file name {fn} is in path try new one', fn)
                manu()
            else:
                with open(fn, "w") as outfile:
                    json.dump(dictionary, outfile, indent=4)
        print(Fore.LIGHTBLUE_EX + str('[+] new file create - welcome Submarines in the desert'.title()) + Fore.RESET)

        mdb = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=.;'
                             'Database=SubmarinesInTheDesert;'
                             'Trusted_Connection=yes;')
        mc = mdb.cursor()
        mdb.autocommit = True

        time = dictionary['time']
        current_date = dictionary['date']
        event_id = dictionary['event_id']
        id_number = dictionary['id_number']
        first_name = dictionary['first_name']
        last_name = dictionary['last_name']
        mobile_number = dictionary['mobile_number']
        password = dictionary['password']
        email = dictionary['email']
        ipv4_privet = dictionary['ipv4_privet']
        ipv4_public = dictionary['ipv4_public']
        port_number = dictionary['port_number']
        user_name = dictionary['user_name']
        domain_name = dictionary['domain_name']
        path = dictionary['path']
        macaddress = dictionary['macaddress']

        mc_query = f"EXEC sp_load_fakr_customers " \
                   f"@time = '{time}'," \
                   f"@date = '{current_date}'," \
                   f"@event_id = '{event_id}'," \
                   f"@id_number = '{id_number}'," \
                   f"@first_name = '{first_name}'," \
                   f"@last_name = '{last_name}'," \
                   f"@mobile_number = '{mobile_number}'," \
                   f"@password = '{password}'," \
                   f"@email = '{email}'," \
                   f"@ipv4_privet = '{ipv4_privet}'," \
                   f"@ipv4_public = '{ipv4_public}'," \
                   f"@port_number = '{port_number}'," \
                   f"@user_name = '{user_name}'," \
                   f"@domain_name = '{domain_name}'," \
                   f"@path = '{path}'," \
                   f"@macaddress = '{macaddress}'"
        mc = mc.execute(mc_query)
        mc.close()
        mdb.close()

        cnt = 0
        path = r"C:\\temp\sim_password\Customers\\"
        for _ in glob.glob(path + '*.json'):
            os.listdir(path)
            cnt += 1
        print(Fore.MAGENTA + str(f'[+] total json file in path: {cnt},  {current_date},  {time}'.title()) + Fore.RESET)

        manu()
manu()