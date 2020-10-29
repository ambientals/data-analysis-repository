"""Code that performs a SSH connection from a Windows or Linux machine on a remote Linux server using Python's Paramiko module, then executes the "ls" linux-bash-based command. This code has educational purposes; no copyright infringement is intended."""

import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('IP_ADDRESS', port=PORT, username='USERNAME', password='PASSWORD')
# *Commonly the PORT might be setted to 22 by default

stdin, stdout, stderr = ssh.exec_command('ls')

output=stdout.readlines()
AA = type(output)
print(AA)
print(output)
