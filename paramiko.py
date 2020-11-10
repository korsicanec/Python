import paramiko

# обнуляю список виртуальних машин name.txt

f = open('name.txt', 'w')
f.write('')
f.close()

# обнуляю список виртуальних машин name.txt

f = open('name.txt', 'w')
f.write('')
f.close()

# ssh авторизация и выполнение команды на хосте

def connect(ip='',
            username='',
            port=,
            password='',
            cmd="""vim-cmd vmsvc/getallvms | grep -v Vmid | awk "{print \$2}" | sed 's/^/"/;s/$/", /'"""):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    vmname = ''.join(outlines)
