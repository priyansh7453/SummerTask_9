  
#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess 
import cgi
import time



dataset = cgi.FieldStorage()

cmd = data.getvalue("command")

output = subprocess.getoutput("sudo " +cmd+ " --kubeconfig /root/kubews/admin.conf") 

print(output)
