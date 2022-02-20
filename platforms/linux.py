import subprocess
import colorama
import shlex
import json

class Ubuntu():
    def __init__(self):
        self.successful_policies_added = 0
        self.error_policies = 0

    def mount_policy_file(self, policy_file_path):
        if len(policy_file_path) < 1:
            raise ValueError("No policy file has been specified.")
        
        #read file and load the json file
        with open(policy_file_path, "r") as read_file:
            self.imported_policy_file = json.load(read_file)
    
    def set_policies(self):
        for policy_category in self.imported_policy_file:
            print('[{0}{1}{2}]'.format(colorama.Fore.RED, policy_category, colorama.Style.RESET_ALL))
            for policy in self.imported_policy_file[policy_category]:
                #use shlex library to handle splitting of the bash command and routing it to the subprocess library to execute it seamlessy
                bash_command = shlex.split(policy)
                
                process = subprocess.Popen(bash_command, stdout=subprocess.PIPE)
                output, error = process.communicate()
                print('{0}[✓] {1}{2}\n{3}'.format(colorama.Fore.GREEN ,colorama.Style.RESET_ALL , ' '.join(bash_command), output.decode('utf-8')))
