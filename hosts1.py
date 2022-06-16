file1 = open('./temp/hosts8')
new = []
for line in file1:
    if len(line)>5:
        new.append(line)
file1.close()
file2=open('./temp/haproxy')
hproxy = file2.readline()
file2.close()
f3 = open("./hosts", "w")
f3.close()
f = open("./hosts", "w")

f.write("[haproxy]\n")
f.write(hproxy)
f.write("\n")

f.write("[webservers]")
f.write("\n")
for line in new:
    linesplit = line.split(" ")
    if len(linesplit[1])>7:
        #print(linesplit[1][-7:])
        if (linesplit[1][-7:]) != 'haproxy' and (linesplit[1][-7:]) != 'bastion':
            f.write(linesplit[1])
            #print(linesplit[1])
            f.write("\n")
    else:
        f.write(linesplit[1])
        f.write("\n")
f.write("\n")
f.write("[all:vars]\n")
f.write("ansible_user=ubuntu")
f.close()
