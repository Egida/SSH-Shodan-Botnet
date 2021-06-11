# SSH-Shodan-Botnet
Self explanatory:

This code extracts multiple IPs based on the "SSH" query and attempts to brute force each one, which once successful you can then use to establish your "botnet".

Before you use this script make sure to install the pip packages:
1. Paramiko
2. shodan

Tested on:
Ubuntu20+
Python version: 3.9+

# Steps

```git clone https://github.com/Ancurserv/SSH-Shodan-Botnet/```
```cd SSH-Shodan-Botnet```
Once you reach that then simply modify open/edit the py file and put your Shodan API key within the quotes of:
```API_KEY = ""```

As for installing process just do:
```pip install paramiko shodan```(or install both separately) and then do:
```python3 ssh-bot.py``` or ```python ssh-bot.py```

(Also when you add your own pass/users file you can either choose to rename them to user.txt or pass.txt(since default search)
```user_file = "user.txt"```
```pass_file = "pass.txt"```
(also it only extracts IPs within page 1(for the API) until you get premium for your account, you could however also put it in a loop since page 1 will eventually refresh with new IPs.


# Bugs
After longer testing periods, avoid using mixed character password files without declaring ```ISO-8859-1```:
```python
with open(pass_file, 'r', encoding="ISO-8859-1") as source2:
```
(There was also a bug relating to file size which I assumed was because of the way the data was handled but instead was caused because of the fast iteration)

# Update
You can now use files near the size of rockyou.txt original file size.
