# SSH-Shodan-Botnet
Self explanatory:

Before you use this script make sure to install the pip packages:
1. Paramiko
2. shodan

And make sure to setup a shodan account to use your shodan API

once you are done doing that, open the py file and go to ```API_KEY``` variable and insert your key within the quotes
Then use your own password and user file(I was planning on making a big user and password file for you all but eh)
and insert the path into the ```user_file``` and ```pass_file```

And that's basically it, now a few things to remember is make sure your password list is longer than the IP list because I have everything relying on the IP for loop
So if your password list gets done before the IP list iteration is over then IndexError will occur and it will stop everything, you can modify whatever you want about the code because I personally know that it's not well polished and I was too lazy to polish it up even more

There will also be an output of errors relating to the exception: paramiko.ssh_exception.SSHException
but it will basically get ignored by the exception handling and it will skip over an IP that caused it and same thing for the paramiko.ssh_exception.NoValidConnectionsError Exception.

Long story short:
The program works as intended but the output may look messy, you'll still be told when you successfully gained access to a ssh server

Purpose of this tool: 
It will scan Shodan and it will attempt to brute force every IP found(at the end of the code you should probably use ```sys``` or ```os``` module and have it execute itself again so it can repeatedly search or put the shodan search function within a loop(if you know what you are doing)
And once the attack is successful it will tell you the password and such, and then you can handle the rest using metasploit.
