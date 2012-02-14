'''
Created on Feb 13, 2012

@author: josa
'''
import os
import md5

final_file = "DSC04001_final.JPG"
f = open("DSC04001.JPG.headers", "rb")
lines = f.readlines()
origin_name = lines[0].split(":")[1].strip()
md5sum = lines[1].split(":")[1].strip()
print "join files in: %s" % origin_name
print "md5sum: %s" % md5sum
new_f = open(final_file, "w")
for i in lines[2:]:
    file_name = i.strip()
    part_f = open(file_name)
    new_f.write(part_f.read())
    part_f.flush()
    part_f.close()
    os.remove(file_name)
    
new_f.flush()
new_f.close()
f.flush()
f.close()

md5sum_check = md5.new()
check_f = open(final_file, "rb")
num_of_bytes = 1024 * 15
c = check_f.read(num_of_bytes)
while len(c) > 0:
    md5sum_check.update(c)
    c = check_f.read(num_of_bytes)
 
check_f.flush()
check_f.close()   

print "File is OK" if md5sum_check.hexdigest() == md5sum else "File is NOT OK"
