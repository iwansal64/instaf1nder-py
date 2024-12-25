from core.instaf1nder import InstaF1nder
import core.ui as ui
import core.prettier as prettier
import os
from core.prettier import COLOURS
import time
from instagrapi.exceptions import UserNotFound
import webbrowser

def main():
    os.system("clear")
    current_directory = "/".join(__file__.split("/")[:-1])

    creds = {}

    try:
        with open(current_directory+"/creds.txt", "r+") as f:
            contents = f.read().split(",")
            creds["username"] = contents[0]
            creds["password"] = contents[1]

    except FileNotFoundError as e:
        print("creds.txt doesn't exist!")
        exit(1)

    instaf1nder = InstaF1nder()

    ui.print_first()

    prettier.printy("Logging in...", time=0.25, end="\r")
    instaf1nder.login(creds)
    prettier.printy("Successfully Login!", time=0.75)
    time.sleep(0.5)

    while True:
        prettier.printy("Who will be the target this time: ", time=0.5, end="")
        target = input(COLOURS.red)
        
        prettier.printy(f"Gathering {target} Information..", time=0.5)
        try:
            target_information = instaf1nder.get_user_info(target)
        except UserNotFound:
            prettier.printy(f"User not found...")
            time.sleep(2)
            prettier.printy(ui.ASCII_ART)
            continue
        
        change_target = False
        last_user_option = "1"
        user_option = "1"
        while True:
            os.system("clear")
            ui.print_info(target_information.username)
            if user_option == "q":
                break
            elif user_option == "1":
                ui.print_target_generals(target_information)
            elif user_option == "2":
                ui.print_target_bio(target_information)
            elif user_option == "3":
                ui.print_target_contacts(target_information)
            elif user_option == "4":
                ui.print_target_links(target_information)
            elif user_option == "5":
                ui.print_target_generals(target_information)
                ui.print_target_bio(target_information)
                ui.print_target_contacts(target_information)
                ui.print_target_links(target_information)
            elif user_option == "6":
                prettier.printy("Where should I put the dump file sir?", COLOURS.blue, time=0.5)
                prettier.printy("> ", end=" ")
                dump_file_path = input()
                overwrite = False
                if os.path.exists(dump_file_path):
                    prettier.printy("File exists!")
                    prettier.printy("Do you want to overwrite it?")
                    overwrite = input() == "y"

                prettier.printy("Saving...", COLOURS.blue, time=0.25)
                if last_user_option == "1":
                    ui.print_target_generals(target_information, True, dump_file_path, overwrite)
                elif last_user_option == "2":
                    ui.print_target_bio(target_information, True, dump_file_path, overwrite)
                elif last_user_option == "3":
                    ui.print_target_contacts(target_information, True, dump_file_path, overwrite)
                elif last_user_option == "4":
                    ui.print_target_links(target_information, True, dump_file_path, overwrite)
                elif last_user_option == "5":
                    ui.print_target_generals(target_information, True, dump_file_path, overwrite)
                    ui.print_target_bio(target_information, True, dump_file_path)
                    ui.print_target_contacts(target_information, True, dump_file_path)
                    ui.print_target_links(target_information, True, dump_file_path)

                prettier.printy("DONE!", COLOURS.blue, time=0.1)
                input("(press enter)")

            elif user_option == "7":
                if last_user_option == "1":
                    if target_information.address_street:
                        webbrowser.open("https://www.google.com/maps/search/"+target_information.address_street)
                    else:
                        prettier.printy("Address Street is not available. (The user doesn't include his/her address to the instagram profile) :(")
                        input("(press enter)")
                elif last_user_option == "3":
                    if target_information.public_email:
                        prettier.printy("What will be the subject? ")
                        subject = input("> ")
                        prettier.printy("What will be the body? ")
                        body = input("> ")
                        res = "mailto:"+target_information.public_email+"?subject="+subject+"&body="+body
                        prettier.printy(res)
                        webbrowser.open(res)
                    else:
                        prettier.printy("Address Street is not available. (The user doesn't include his/her address to the instagram profile) :(")
                        input("(press enter)")
                    
                    
                    
            elif user_option == "c":
                change_target = True
                break
            
            ui.print_options(user_option)
            prettier.printy("> ", end=" ")
            last_user_option = user_option
            user_option = input() 

        if change_target:
            continue
        
        break
    

if __name__ == "__main__":
    main()
    print(prettier.COLOURS.reset)