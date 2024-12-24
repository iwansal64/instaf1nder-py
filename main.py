from core.instaf1nder import InstaF1nder
import core.ui as ui
import core.prettier as prettier
import os
from core.prettier import COLOURS
import time

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
        target_information = instaf1nder.get_user_info(target)
        
        change_target = False
        user_option = "1"
        while True:
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
                change_target = True
                break
            
            ui.print_options()
            prettier.printy("> ", end=" ")
            user_option = input() 

        if change_target:
            continue
        
        break
    

if __name__ == "__main__":
    main()
    print(prettier.COLOURS.reset)