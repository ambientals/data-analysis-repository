"""Code that performs a SSH connection from a Windows or Linux machine on a remote Windows server using Python's WinRM module, then runs the Windows update service. This code has educational purposes; no copyright infringement is intended."""

import winrm 
from winrm.protocol import Protocol

p = Protocol(
    endpoint='https://IP_ADDRESS:PORT/wsman',
    transport='basic',
    username=r'USERNAME',
    password='PASSWORD',
    server_cert_validation='ignore')
# *Commonly the PORT might be setted to 22 by default

shell_id1 = p.open_shell()
command_id1 = p.run_command(shell_id1, 'net', ['stop','wuauserv'])
std_out1, std_err1, status_code1 = p.get_command_output(shell_id1, command_id1)
p.cleanup_command(shell_id1, command_id1)
p.close_shell(shell_id1)
print(std_out1) 

shell_id2 = p.open_shell()
command_id2 = p.run_command(shell_id2, 'net', ['start','wuauserv'])
std_out2, std_err2, status_code2 = p.get_command_output(shell_id2, command_id2)
p.cleanup_command(shell_id2, command_id2)
p.close_shell(shell_id2)
print(std_out2)
