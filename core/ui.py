from core.prettier import COLOURS
import core.prettier as prettier
from core.instaf1nder import VERSION
from instagrapi import types
import time
import os
import art

ASCII_ART = rf"""
{COLOURS.red} ___ {COLOURS.green}     {COLOURS.yellow}    {COLOURS.blue} _  {COLOURS.white}     {COLOURS.magenta} _____{COLOURS.red} _ {COLOURS.blue}      {COLOURS.magenta}    _ {COLOURS.green}     {COLOURS.white}     
{COLOURS.red}|_ _|{COLOURS.green}_ __ {COLOURS.yellow} ___{COLOURS.blue}| |_{COLOURS.white} __ _{COLOURS.magenta}|  ___{COLOURS.red}/ |{COLOURS.blue}_ __  {COLOURS.magenta} __| |{COLOURS.green} ___ {COLOURS.white}_ __ 
{COLOURS.red} | ||{COLOURS.green} '_ \{COLOURS.yellow}/ __{COLOURS.blue}| __{COLOURS.white}/ _` {COLOURS.magenta}| |_  {COLOURS.red}| |{COLOURS.blue} '_ \ {COLOURS.magenta}/ _` |{COLOURS.green}/ _ \{COLOURS.white} '__|
{COLOURS.red} | ||{COLOURS.green} | | {COLOURS.yellow}\__ {COLOURS.blue}\ ||{COLOURS.white} (_| {COLOURS.magenta}|  _| {COLOURS.red}| |{COLOURS.blue} | | |{COLOURS.magenta} (_| |{COLOURS.green}  __/{COLOURS.white} |   
{COLOURS.red}|___|{COLOURS.green}_| |_{COLOURS.yellow}|___/{COLOURS.blue}\__{COLOURS.white}\__,_{COLOURS.magenta}|_|   {COLOURS.red}|_|{COLOURS.blue}_| |_|{COLOURS.magenta}\__,_|{COLOURS.green}\___|{COLOURS.white}_| {COLOURS.blue}v{VERSION}
{COLOURS.blue_blink}--------------------------------------------------------{COLOURS.reset}{COLOURS.default}"""


def print_first() -> str:
    '''Print first screen'''
    prettier.printy(ASCII_ART)
    prettier.printy("WELCOME TO ", end="\r", time=0.25)
    time.sleep(0.75)
    prettier.printy("INSTAF1NDER!", color_code=COLOURS.blue, end="\r", time=0.5)
    time.sleep(0.75)

def print_info(username: str):
    '''Print info'''
    prettier.printy(ASCII_ART)
    print(COLOURS.red)
    art.tprint(username, font="tarty4")
    print(COLOURS.default)

def print_target_generals(user_data: types.User, is_dump: bool = False, dump_file_path: str = "", overwrite: bool = False):
    '''Print target general informations'''
    if not is_dump:
        delay_to_show_info = 0.25
        print()
        prettier.printy("GENERAL:")
        prettier.printy("------")
        prettier.printy(fr"Username                     : {str(user_data.username)}", time=delay_to_show_info)
        prettier.printy(fr"Full Name                    : {str(user_data.full_name)}", time=delay_to_show_info)
        prettier.printy(fr"Account Type                 : {str(user_data.account_type)}", time=delay_to_show_info)
        prettier.printy(fr"Followers Count              : {str(user_data.follower_count)}", time=delay_to_show_info)
        prettier.printy(fr"Following Count              : {str(user_data.following_count)}", time=delay_to_show_info)
        prettier.printy(fr"Media Count                  : {str(user_data.media_count)}", time=delay_to_show_info)
        prettier.printy(fr"Private?                     : {'Yes' if user_data.is_private else 'No'}", time=delay_to_show_info)
        prettier.printy(fr"Verified                     : {'Yes' if user_data.is_verified else 'No'}", time=delay_to_show_info)
        prettier.printy(fr"Address Street               : {str(user_data.address_street)}", time=delay_to_show_info)
        prettier.printy(fr"City ID                      : {str(user_data.city_id)}", time=delay_to_show_info)
        prettier.printy(fr"City Name                    : {str(user_data.city_name)}", time=delay_to_show_info)
        prettier.printy(fr"Business Account?            : {'Yes' if user_data.is_business else 'No'}", time=delay_to_show_info)
        prettier.printy(fr"Business Category Name       : {str(user_data.business_category_name)}", time=delay_to_show_info)
    else:
        with open(dump_file_path, "w" if overwrite else "a+") as f:
            f.write(f"\nGENERAL:\n------\nUsername                     : {str(user_data.username)}\nFull Name                    : {str(user_data.full_name)}\nAccount Type                 : {str(user_data.account_type)}\nFollowers Count              : {str(user_data.follower_count)}\nFollowing Count              : {str(user_data.following_count)}\nMedia Count                  : {str(user_data.media_count)}\nPrivate?                     : {'Yes' if user_data.is_private else 'No'}\nVerified                     : {'Yes' if user_data.is_verified else 'No'}\nAddress Street               : {str(user_data.address_street)}\nCity ID                      : {str(user_data.city_id)}\nCity Name                    : {str(user_data.city_name)}\nBusiness Account?            : {'Yes' if user_data.is_business else 'No'}\nBusiness Category Name       : {str(user_data.business_category_name)}\n")
            

def print_target_links(user_data: types.User, is_dump: bool = False, dump_file_path: str = "", overwrite: bool = False):
    '''Print target link informations'''
    if not is_dump:
        delay_to_show_info = 0.5
        print()
        prettier.printy("LINKS:")
        prettier.printy("------")
        prettier.printy(fr"Profile Pict URL             : ", time=delay_to_show_info, end="")
        prettier.printy(fr"{str(user_data.profile_pic_url.__str__())}")
        prettier.printy(fr"Profile Pict URL (HD)        : ", time=delay_to_show_info, end="")
        prettier.printy(fr"{str(user_data.profile_pic_url_hd.__str__())}")
        prettier.printy(fr"External URL                 : ", time=delay_to_show_info, end="")
        prettier.printy(fr"{str(user_data.external_url.__str__())}")
    else:
        with open(dump_file_path, "w" if overwrite else "a+") as f:
            f.write(f"\nLINKS:\n------\nProfile Pict URL             : \n{str(user_data.profile_pic_url.__str__())}\nProfile Pict URL (HD)        : \n{str(user_data.profile_pic_url_hd.__str__())}\nExternal URL                 : \n{str(user_data.external_url.__str__())}\n")
        

def print_target_bio(user_data: types.User, is_dump: bool = False, dump_file_path: str = "", overwrite: bool = False):
    '''Print target bio'''
    if not is_dump:
        print()
        prettier.printy("BIO:")
        prettier.printy("-------")
        prettier.printy(fr"{str(user_data.biography)}")
    else:
        with open(dump_file_path, "w" if overwrite else "a+") as f:
            f.write(f"\nBIO:\n-------\n{str(user_data.biography)}\n")
        
    
def print_target_contacts(user_data: types.User, is_dump: bool = False, dump_file_path: str = "", overwrite: bool = False):
    '''Print target contact informations'''
    if not is_dump:
        delay_to_show_info = 0.25
        print()
        prettier.printy("CONTACT:")
        prettier.printy("---------")
        prettier.printy(fr"Contact Phone Number         : {str(user_data.contact_phone_number)}", time=delay_to_show_info)
        prettier.printy(fr"Public Phone Number          : {str(user_data.public_phone_number)}", time=delay_to_show_info)
        prettier.printy(fr"Public Phone Country Code    : {str(user_data.public_phone_country_code)}", time=delay_to_show_info)
        prettier.printy(fr"Public Email                 : {str(user_data.public_email)}", time=delay_to_show_info)
        prettier.printy(fr"Business Contact Method      : {str(user_data.business_contact_method)}", time=delay_to_show_info)
    else:
        with open(dump_file_path, "w" if overwrite else "a+") as f:
            f.write(f"\nCONTACT:\n---------\nContact Phone Number         : {str(user_data.contact_phone_number)}\nPublic Phone Number          : {str(user_data.public_phone_number)}\nPublic Phone Country Code    : {str(user_data.public_phone_country_code)}\nPublic Email                 : {str(user_data.public_email)}\nBusiness Contact Method      : {str(user_data.business_contact_method)}\n")

def print_options(last_option: str = "-1"):
    '''Print options to do'''
    print()
    prettier.printy("********************* INFORMATION *********************", COLOURS.green, time=0.2)
    prettier.printy("1. General .......... General information about the user", COLOURS.blue, time=0.2)
    prettier.printy("2. Biography ........ Take a look at her/his bio!", COLOURS.blue, time=0.2)
    prettier.printy("3. Contacts ......... You want to try to contact her/him?", COLOURS.blue, time=0.2)
    prettier.printy("4. Links ............ Links that related to her/his insta", COLOURS.blue, time=0.2)
    prettier.printy("5. All .............. Shows all of the informations", COLOURS.blue, time=0.2)
    if last_option == "1":
        prettier.printy("******************** DATA PROCESS *********************")
        prettier.printy("6. Dump ............. Save it for later research?", COLOURS.blue, time=0.2)
        prettier.printy("7. Map .............. Search adress street in map?", COLOURS.blue, time=0.2)
    elif last_option == "2":
        prettier.printy("******************** DATA PROCESS *********************")
        prettier.printy("6. Dump ............. Save it for later research?", COLOURS.blue, time=0.2)
    elif last_option == "3":
        prettier.printy("******************** DATA PROCESS *********************")
        prettier.printy("6. Dump ............. Save it for later research?", COLOURS.blue, time=0.2)
        prettier.printy("7. Email ............ Send an email to target's email", COLOURS.blue, time=0.2)
        prettier.printy("8. Chat ............. Send a message to target's phone number", COLOURS.blue, time=0.2)
    elif last_option == "4":
        prettier.printy("******************** DATA PROCESS *********************")
        prettier.printy("6. Dump ............. Save it for later research?", COLOURS.blue, time=0.2)
        prettier.printy("7. Downloads ........ Downloads available media", COLOURS.blue, time=0.2)
    elif last_option == "5":
        prettier.printy("******************** DATA PROCESS *********************")
        prettier.printy("6. Dump ............. Save it for later research?", COLOURS.blue, time=0.2)
        
    prettier.printy("************************ OTHER ************************", COLOURS.green)
    prettier.printy("c. Change ........... You have another target to search?", COLOURS.blue)
    prettier.printy("q. Quit ............. Are you done bro?", COLOURS.blue)

    
    
    