import os
import json
import colorama

from time import sleep
from colorama import Fore
from currency_converter import CurrencyConverter
from weight_converter.convert import Kilograms, Pounds

c = CurrencyConverter()

def menu():  
    print(f"""{colorama.Fore.RED}
                     ████████╗███╗   ███╗ ██████╗               ██╗   ██╗████████╗██╗     ███████╗
                     ╚══██╔══╝████╗ ████║██╔════╝               ██║   ██║╚══██╔══╝██║     ██╔════╝
                        ██║   ██╔████╔██║██║  ███╗    █████╗    ██║   ██║   ██║   ██║     ███████╗
                        ██║   ██║╚██╔╝██║██║   ██║    ╚════╝    ██║   ██║   ██║   ██║     ╚════██║
                        ██║   ██║ ╚═╝ ██║╚██████╔╝              ╚██████╔╝   ██║   ███████╗███████║
                        ╚═╝   ╚═╝     ╚═╝ ╚═════╝                ╚═════╝    ╚═╝   ╚══════╝╚══════╝
                                                    

                                                Made by {colorama.Fore.RESET}WolvTMG#0001 {colorama.Fore.RED}

                            [1] Money        | [2] Weight       | [3] Distance     | [4] Coming soon
                            [5] Coming soon  | [6] Coming soon  | [7] Coming soon  | [8] Coming soon
                            [9] Coming soon  | [10] Update Log  | [11] Coming soon | [12] Exit

""")

def lau():
    print(f"""{colorama.Fore.RED}
                     ████████╗███╗   ███╗ ██████╗               ██╗   ██╗████████╗██╗     ███████╗
                     ╚══██╔══╝████╗ ████║██╔════╝               ██║   ██║╚══██╔══╝██║     ██╔════╝
                        ██║   ██╔████╔██║██║  ███╗    █████╗    ██║   ██║   ██║   ██║     ███████╗
                        ██║   ██║╚██╔╝██║██║   ██║    ╚════╝    ██║   ██║   ██║   ██║     ╚════██║
                        ██║   ██║ ╚═╝ ██║╚██████╔╝              ╚██████╔╝   ██║   ███████╗███████║
                        ╚═╝   ╚═╝     ╚═╝ ╚═════╝                ╚═════╝    ╚═╝   ╚══════╝╚══════╝

                                            Made by {colorama.Fore.RESET}WolvTMG#0001
                                                        
""")

def main():

    print("Booting TMG UTLS")
    sleep(0.5)
    print("Made by WolvTMG")
    sleep(0.5)
    os.system('cls')
    print("Loading ...")
    sleep(0.25)
    os.system('cls')

    while True:

        menu()
        select = int(input("                                                      Choice: "))

        if select == 1:
            os.system('cls')
            lau()
            go = input("What currency are you converting from? ").upper()
            to = input("What currency are you converting to? ").upper()
            ammount = float(input("How much are you converting? "))
            result = c.convert(ammount, go, to)
            input(f"\n{result}")

        elif select == 2:
            os.system('cls')
            lau()
            go = input("What weight are you converting from? ").lower()
            ammount = float(input("How much are you converting? "))

            if go == 'kg':
                x = 'KG'
                y = 'LBS'
                kilograms = Kilograms(value=ammount)
                result = kilograms.to_pounds()
            elif go == 'lbs':
                x = 'LBS'
                y = 'KG'
                pounds = Pounds(value=ammount)
                result = pounds.to_kilograms()

            input(f"\n{ammount} {x} is {result} {y}")

        elif select == 10:
            os.system('cls')
            lau()
            input("\n[Update] Changelog 4/4/2022, nothing yet\n\n[Enter] to return")

        elif select == 12:
            os._exit(1)

        else:
            input("Invalid input")

        os.system('cls')

if __name__ == '__main__':
    main()
