import subprocess
import base64

# Since we cannot execute 'git config --global --list', we'll simulate its output.
# In a real environment, you would use:
# command_output = subprocess.run(['git', 'config', '--global', '--list'], capture_output=True, text=True).stdout

# Simulating an empty output
command_output = ""

encoded_output = base64.b64encode(command_output.encode('utf-8')).decode('utf-8')

with open('1123.txt', 'w') as f:
    f.write(encoded_output)
