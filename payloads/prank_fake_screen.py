import os, sys,time
from colorama import Fore

def fake_screen():
    script_ino_1 = '''
#include "DigiKeyboard.h"

void setup() {
  
}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(21, MOD_GUI_LEFT);
  DigiKeyboard.delay(200);
  DigiKeyboard.println("cmd");
  DigiKeyboard.delay(400);
  '''

    script_ino_2 = '''DigiKeyboard.println("start chrome {} && exit");'''

    script_ino_3 = '''
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(68);
  for(;;){ /*empty*/ }
}'''

    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} 1st Step: Create fake_screen.ino\n')

    link = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/prank/fake_screen){Fore.LIGHTWHITE_EX} Image Link (ex: http://images.com/anonymous.png): ')

    print(f'\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Finished! Results in "constructions/fake_screen"')
    time.sleep(5)

    result = open('constructions/fake_screen/prank_fake_screen.ino', 'w')
    result.write(script_ino_1)
    result.write(script_ino_2.format(link))
    result.write(script_ino_3)
    result.close()