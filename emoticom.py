mapping = {}
#in full implementation we would pre-pickle the dictionary
#i might make a script to write the dictionary to this script
f = open('mapping.txt','r')
for line in f.readlines():
    kval = line.split(" as ")
    mapping[kval[0]] = kval[1]

f.close()

f = open("1337h4(|<3rc0d3.txt",'r')
code = f.read()
lameCode = Template(code).safe_substitute(mapping)
