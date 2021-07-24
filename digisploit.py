#!/usr/bin/env python3
import os, sys, platform
from colorama import Fore
import payloads.reverse_shell_tcp as r_shell_tcp
import payloads.reverse_shell_tcp_disable_wd as r_shell_tcp_d_wd
import payloads.wifi_grabber_mail as wifi_grabber_mail
import payloads.wifi_grabber as wifi_grabber
import payloads.prank_fake_screen as prank_fake_screen


def main():
    if platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
    def banner():
        print('''
                      ▒███████████████████████████▓▓▓▓▓
                      ▒█████████▓█▓▓▓▓▓▓▓▓▓█▓███▓▓▒▒ ▓▒
                      ▒████████████▓█▓█▓█▓████████▒▓▓▓▓
     ▓██████████████████████████▓█▓▓▓█▓█▓█▓█▓█████▒▓▓▓▓
     ▓██████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▒ ▓▓
     ▓█▓ ▒ ▒▒▒▒▒▒▒▒▒ ▓██████████▓███████████▓█████▒▓██▓
     ▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████████████████▓▓▓▒▓▓
     ▓██████████████████████████████████████████▓▓▓▓▒▓▓
     ▓███▓▒▒▒▒▒▒▒▒▒▒▒▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓█████▒▓██▓
     ▓████████████████████ ▒██▓█▓█▓█▓█▓███▓▓▓███▓▓▓▓ ▓▓
     ▓███▓▒▒▒▒▒▒▒▒▒▒▒▓████▒▒███▓█▓█▓█▓████████████▓▓▓▓▓
     ▓████████████████████▒▒██▓█▓███▓██▓▓█████████▒▓█▓▓
     ▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▒▒███▓█▓█▓█▓▓█████████▓▓▓▒ ▓▓
     ▓█▓ ▒▒▒▒▒▒▒▒▒▒▒ ▓████▒▒▓█▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒█████▒▓█▓▓
     ▓████████████████████████████████████████████▓▓▓▓▓
     ▓██████████████████████████████████████████▓▓▒▒ ▒▒
                      ▒███▓▓▓▓▓▓▓▓▓▓▓▒▓▓██████████▓▓▓▓▓
                      ▒██▓▓▒ ▓█▓ ▒▓█▓ ▒▓▒██████████████
                      ▒██▓▓▒▒▓▓▓▒▒▓▓▓▒▒▓▓██████████████
''')

    banner()
    print(f'''
{Fore.LIGHTYELLOW_EX}[!]{Fore.LIGHTWHITE_EX} IMPORTANT!!!

This Tool was created with the intention of making it
easier to create a script for digispark. This tool
only works on "ABNT2 keyboards", if your victim
does not have this keyboard the script will not work

[01] Show Payloads
[02] Payload Infos

[99] Exit
''')


    def payloads():
        if platform == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        banner()
        print(f'''
{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Select Payload:

[01] windows/shell/reverse_tcp
[02] windows/disable_windows_defender/shell/reverse_tcp
[03] windows/wifi/grabber
[04] windows/wifi/grabber_mail
[05] windows/prank/fake_screen

[99] Back
''')

    def payload_infos():
        if platform == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
            
        banner()
        print(f'''
{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} PAYLOAD INFOS:

windows/shell/reverse_tcp                                 Normal          Reverse shell on a machine
windows/disable_windows_defender/shell/reverse_tcp        Good            Reverse shell on a machine and disable WD
windows/wifi/grabber                                      Normal          Save all wifi passwords in a folder on the victim's machine
windows/wifi/grabber_mail                                 Excellent       Send all wifi passwords to the attacker's gmail
windows/prank/fake_screen                                 Good            Opens an image in the chrome browser and leaves it in full screen

[99] Back
''')


    
    terminal_main = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}~{Fore.LIGHTWHITE_EX}$ ')
    while True:
        if terminal_main == '1':
            payloads()
            terminal_payload = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}/payloads{Fore.LIGHTWHITE_EX}# ')
            
            if terminal_payload == '99':
                main()

        if terminal_main == '2':
            payload_infos()
            terminal_payload_infos = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}/payload_infos{Fore.LIGHTWHITE_EX}# ')
            
            if terminal_payload_infos == '99':
                main()

        if terminal_main == '99':
            break

        if terminal_payload == '1':
            r_shell_tcp.reverse_shell_tcp()
        if terminal_payload == '2':
            r_shell_tcp_d_wd.reverse_shell_tcp()
        if terminal_payload == '3':
            wifi_grabber.wifi_grabber()
        if terminal_payload == '4':
            wifi_grabber_mail.wifi_grabber_mail()
        if terminal_payload == '5':
            prank_fake_screen.fake_screen()
        if terminal_payload == '99':
            break
            
            
if __name__ == '__main__':
    main()
