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

# Записываем в файл результат выполнения команды

    f = open('name', 'a')
    f.write(**name)
    f.close()

connect(ip='')

# ssh авторизация и выполнение команды на хосте

def connect_6(ip='',
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

# Записываем в файл результат выполнения команды

    f = open('name', 'a')
    f.write(**name)
    f.close()

connect_6(ip='', password='')
