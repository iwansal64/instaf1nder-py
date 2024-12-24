from core.prettier import COLOURS
import core.prettier as prettier
from instagrapi import types
import time
import os
import art

ASCII_ART = rf"""
{COLOURS.red} ___ {COLOURS.green}     {COLOURS.yellow}    {COLOURS.blue} _  {COLOURS.white}     {COLOURS.magenta} _____{COLOURS.red} _ {COLOURS.blue}      {COLOURS.magenta}    _ {COLOURS.green}     {COLOURS.white}     
{COLOURS.red}|_ _|{COLOURS.green}_ __ {COLOURS.yellow} ___{COLOURS.blue}| |_{COLOURS.white} __ _{COLOURS.magenta}|  ___{COLOURS.red}/ |{COLOURS.blue}_ __  {COLOURS.magenta} __| |{COLOURS.green} ___ {COLOURS.white}_ __ 
{COLOURS.red} | ||{COLOURS.green} '_ \{COLOURS.yellow}/ __{COLOURS.blue}| __{COLOURS.white}/ _` {COLOURS.magenta}| |_  {COLOURS.red}| |{COLOURS.blue} '_ \ {COLOURS.magenta}/ _` |{COLOURS.green}/ _ \{COLOURS.white} '__|
{COLOURS.red} | ||{COLOURS.green} | | {COLOURS.yellow}\__ {COLOURS.blue}\ ||{COLOURS.white} (_| {COLOURS.magenta}|  _| {COLOURS.red}| |{COLOURS.blue} | | |{COLOURS.magenta} (_| |{COLOURS.green}  __/{COLOURS.white} |   
{COLOURS.red}|___|{COLOURS.green}_| |_{COLOURS.yellow}|___/{COLOURS.blue}\__{COLOURS.white}\__,_{COLOURS.magenta}|_|   {COLOURS.red}|_|{COLOURS.blue}_| |_|{COLOURS.magenta}\__,_|{COLOURS.green}\___|{COLOURS.white}_| {COLOURS.blue}v1.0
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
    os.system("clear")
    prettier.printy(ASCII_ART)
    print(COLOURS.red)
    art.tprint(username, font="tarty4")
    print(COLOURS.default)

def print_target_generals(user_data: types.User):
    '''Print target general informations'''
    print_info(user_data.username)
    delay_to_show_info = 0.5
    print()
    prettier.printy("GENERAL:")
    prettier.printy("------")
    prettier.printy(fr"Username                     : {str(user_data.username)}", time=delay_to_show_info)
    prettier.printy(fr"Full Name                    : {str(user_data.full_name)}", time=delay_to_show_info)
    prettier.printy(fr"Private?                     : {str(user_data.is_private)}", time=delay_to_show_info)
    prettier.printy(fr"Address Street               : {str(user_data.address_street)}", time=delay_to_show_info)

def print_target_links(user_data: types.User):
    '''Print target link informations'''
    print_info(user_data.username)
    print()
    prettier.printy("LINKS:")
    prettier.printy("------")
    prettier.printy(fr"Profile Pict URL             : ", time=0.5, end="")
    prettier.printy(fr"{str(user_data.profile_pic_url.__str__())}")
    prettier.printy(fr"External URL                 : ", time=0.5, end="")
    prettier.printy(fr"{str(user_data.external_url.__str__())}")

def print_target_bio(user_data: types.User):
    '''Print target bio'''
    print_info(user_data.username)
    print()
    prettier.printy("BIO:")
    prettier.printy("-------")
    prettier.printy(fr"{str(user_data.biography)}")
    
def print_target_contacts(user_data: types.User):
    '''Print target contact informations'''
    print_info(user_data.username)
    print()
    delay_to_show_info = 0.5
    prettier.printy("CONTACT:")
    prettier.printy("---------")
    prettier.printy(fr"Contact Phone Number         : {str(user_data.contact_phone_number)}", time=delay_to_show_info)
    prettier.printy(fr"Public Email                 : {str(user_data.public_email)}", time=delay_to_show_info)

def print_options():
    '''Print options to do'''
    print()
    prettier.printy("********************* INFORMATION *********************", COLOURS.green)
    prettier.printy("1. General .......... General information about the user", COLOURS.blue)
    prettier.printy("2. Biography ........ Take a look at her/his bio!", COLOURS.blue)
    prettier.printy("3. Contacts ......... You want to try to contact her/him?", COLOURS.blue)
    prettier.printy("4. Links ............ Links that related to her/his insta", COLOURS.blue)
    prettier.printy("************************ OTHER ************************", COLOURS.green)
    prettier.printy("5. Change ........... You have another target to search?", COLOURS.blue)
    prettier.printy("q. Quit ............. Are you done bro?", COLOURS.blue)

    
    
    