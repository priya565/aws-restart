txt = """ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//"""

import  re
file1 = open(r"/home/ec2-user/environment/preproinsulin-seq.txt","r")
lines =file1.readlines()#returns list of lines
lines = "".join(lines)#we wiil get txt
res = re.findall("[a-z]",lines)
res="".join(res)
file1.close()
print(res,len(res))
print(res[0:24])
print(res[24:54])
print(res[54:89])
print(res[89:110])

#checked re with txt
result = re.findall("[a-z]",txt)
result="".join(result)
#print(result)
#save contents to different file in preproinsulin-seq-clean.txt
file2 = open(r"/home/ec2-user/environment/preproinsulin-seq-clean.txt","w+")
file2.write(result)
file2.close()
#lsinsulin-seq-clean.txt(1-24)
file3 = open(r"/home/ec2-user/environment/lsinsulin-seq-clean.txt","w+")
file3.write(res[0:24])
file3.close()
#binsulin-seq-clean.txt(25-54)
file4 = open(r"/home/ec2-user/environment/binsulin-seq-clean.txt","w+")
file4.write(res[24:54])
file4.close()
#cinsulin-seq-clean.txt(55-89)
file5 = open(r"/home/ec2-user/environment/cinsulin-seq-clean.txt","w+")
file5.write(res[54:89])
file5.close()
# ainsulin-seq-clean.txt(90-110)
file6 = open(r"/home/ec2-user/environment/ainsulin-seq-clean.txt","w+")
file6.write(res[89:110])
file6.close()