'''
File Handling - managing files
file - container in which we contain or store some data
by using extension we can identify what kind of data is in it

Before handling any file, taking permission is very much important

open(): 
    open('filename.ext'/'absolute_path', mode)

close():
    var_name.close()

** here total 3 different modes are present,
    1. write(w),
    2. read(r),
    3. append(a),

write mode:
    1. only write (w)
    2. write + read (w+)
    3. write binary(wb)
    4. write & read binary (wb+)

read mode:
    1. Only read (r)
    2. read + write (r+)
    3. read binary (rb)
    4. read & write binary (rb+)

append mode:
    1. only append (a)
    2. append+read (a+)
    3. append bunary (ab)
    4. append and read binary (ab+)
'''

'''
for write operation we mainly use 2 different functions - 
write(str_data) : single line of data 
writelines(iterable_collection) : write([line1,line2,line3,...,lineN]) - for multiple line of data
'''
file=open('temp.txt','w')
# file.write("This is the first line")
file.write("This is the new data\n") #write overwrites
file.writelines(['This is line 1\n','This is line 2\n','This is line 3\n'])
file.close()
#if the file is not present and you use write mode, it will still execute and just create a new file 
#if the file is already present then it will overwrite prev data with the new one

file2=open('temp2.txt','w')
file2.write ("This file is create through write command")
file2.close()

#Reading file
'''
1. read()
2. readline()
3. readlines()
'''
file=open('temp.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

#write plus read mode
file=open('temp.txt','w+')
# file.write("This is the first line")
file.write("This is the new data\n") #write overwrites
file.writelines(['This is line 1\n','This is line 2\n','This is line 3\n'])
file.seek(0)
print(file.read())
file.close()

#append function - never overwrites previous data , appends at the end 
file=open('file1.txt','a+')
file.write("Python is the best programming language\n")
file.write("Python is very simple language")
file.seek(0)
print(file.read())
file.close()

