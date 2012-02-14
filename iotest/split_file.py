'''
Created on Feb 13, 2012

@author: josa
'''
import md5
md5sum = md5.new()

headers = ["File Name: DSC04001.JPG\n"]
source_filename = "DSC04001.JPG"
print "split of file: %s" % source_filename
source_f = open(source_filename, "rb") 
files = []
num_bytes = 1024 * 15
count = 0;
c = source_f.read(num_bytes)
while len(c) > 0:
    if len(c) > 0:
        name = "DSC04001_%s.part" % str(count)
        files = files + ["%s\n" % name]
        count = count + 1
        fwrite = open(name, "w")
        fwrite.write(c)
        fwrite.flush()
        fwrite.close()
        md5sum.update(c)
        print "  %s" % name
    c = source_f.read(num_bytes)    
source_f.flush()
source_f.close()   

header_f = open("DSC04001.JPG.headers", "w")
headers = headers + ["md5-sum: %s\n" % md5sum.hexdigest()]
headers = headers + files
header_f.writelines(headers)
header_f.flush()
header_f.close()  

print "file split OK, md5sum: %s" % md5sum.hexdigest()
