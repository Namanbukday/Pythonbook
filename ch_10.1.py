# FILES AND EXCEPTION :

# READING FROM A FILE

# READING AN ENTIRE FILE

'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''

'''
with open('ENTER THE FILE PATH') as f_obj:
    contents = f_obj.read()
    print(contents)
'''

# Reading line by line from a file :

'''
filename = 'pi_digits.txt'

with open(filename) as f_obj:
    for i in f_obj:
        print(i.rstrip())
'''

# making a list of lines from a file :
# this will help when you have to access the file's content after the with block :
'''
filename = 'pi_digits.txt'

with open(filename) as f_obj:
    name = f_obj.readlines()

for i in name:
    print(i.strip())
    
'''

# Working with the file contents :

'''
filename = 'pi_digits.txt'

with open(filename) as f_obj:
    line = f_obj.readlines()

pi_string = ''
for i in line:
    pi_string += i.strip()

print(pi_string)
print(len(pi_string))
'''

filename = 'ch10_1.txt'

'''with open(filename) as f:
    contents = f.read()
    for i in range(1, 4):
        print(contents, "\n")
'''

'''with open(filename) as f:
    l = f.readlines()

for i in l:
    print(i.rstrip())
'''
with open(filename) as f:
    l = f.readlines()

l_st = ''
for i in l:
    l_st += i

l_st.replace('python', 'js')
print(l_st)