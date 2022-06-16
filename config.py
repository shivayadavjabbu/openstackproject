file1 = open('./temp/hosts2')
new = []
for line in file1:
    new.append(line)
file1.close()
file2=open('./temp/publickeyfile')
pkeyfile = file2.readline()
file2.close()
file4=open('./temp/config')
op_file = file4.readline()
file4.close()
f = open(f"./{op_file}".replace("\n",""), "w")
f.write("PasswordAuthentication no\n")
f.write("StrictHostKeyChecking no\n\n")
for i in new:
    if len(i) > 5:
        new_line = i.split(" ")
        if len(new_line[1]) > 7:
            #print(new_line[1][-7:])
            if (new_line[1][-7:]) == 'bastion':
                bast_ip = new_line[1]
                #print(bast_ip)
for line in new:
    if len(line)>5:
        linesplit = line.split(" ")
        f.write("host ")
        f.write(linesplit[1])
        f.write("\n")
        ip = linesplit[4]
        ip = ip.strip("[',]}")
        f.write("port 22\n")
        f.write("user ubuntu\n")
       # f.write(f"UserKnownHostsFile=~/dev/null\n")
        f.write(f"IdentityFile {pkeyfile}") # changes as per user
        f.write("hostname ")
        #print(new_line[1][-7:])
        if (linesplit[1])== bast_ip:
            new_ip = linesplit[5].strip("[',]}")
            f.write(new_ip)
        else:
            f.write(ip)
        f.write("\n")
        if linesplit[1] != bast_ip:
            f.write(f"proxyjump {bast_ip}\n")
        if linesplit[1] == bast_ip:
            f.write(f"UserKnownHostsFile=~/dev/null\n")
    f.write("\n")
       
f.close()
