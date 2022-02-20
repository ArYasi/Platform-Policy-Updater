from operator import le
from sys import platform
from platforms.linux import Ubuntu
import os
import sys
import colorama

def platform_linux(policy_file):
    platU = Ubuntu()

    platU.mount_policy_file(policy_file)
    platU.set_policies()

def platform_win32():
    #import code from powershell script later
    pass

try:
    #Return errors if not root or no policy file is specified
    if os.geteuid() != 0:
        raise ValueError("This script must be ran as root.")

    if len(sys.argv) < 2:
        raise ValueError("Please specify a policy file to run.\nExample: python3 main.py policy_file.json")

    #run function based off of platform of the computer
    {'linux': platform_linux(sys.argv[1]), 'win32': platform_win32() }.get(platform)

except ValueError as err:
    print('{0}[Error]{1} {2}'.format(colorama.Fore.RED ,colorama.Style.RESET_ALL ,err))

except (OSError, IOError) as err:
    print('{0}[Error]{1} Policy file has not been found.'.format(colorama.Fore.RED ,colorama.Style.RESET_ALL))