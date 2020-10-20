"""Code that prints all installed packages and a desired package's directories. This code is intended to be used as a GNU General Public Licensed source"""

import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

# Printing all the installed python packages names:
for i in installed_packages:
    print(i)
print("\n")

# # Printing all the directory names inside a package:

# import PACKAGE
# directory_list = dir(PACKAGE)
# for d in directory_list:
#     print(d)

# Example:
import wget
directory_list = dir(wget)
for d in directory_list:
    print(d)
