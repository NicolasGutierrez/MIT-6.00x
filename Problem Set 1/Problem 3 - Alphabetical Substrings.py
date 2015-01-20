# begin counting time until calculation ends
import time
start_time = time.clock()
# given variables
s = 'lkcifyktfhquabcdefghijknnnnnnnc'
# defined variables
current_s=''
new_s = ''
longest = ''
for i in range(len(s)):                 
    if i != len(s)-1:
        if  s[i] <= s[i+1]:             
            new_s += s[i]               # current letter is added to New string
        elif s[i] >= s[i-1]:
            new_s += s[i]               # current letter is added to New string
            current_s = new_s   
            new_s = ''                  
    elif s[i] >= s[i-1]:                # this works when i == len(s)
            new_s = new_s + s[i]    
    if len(current_s) > len(longest):   # updates longest value
        longest = current_s
    if len(new_s) > len(longest):       # updates longest value
        longest = new_s    
    print 'Run number: ' + str(i+1) 
    print 'Current string is: ' + current_s
    print 'New string is: ' + new_s
    print 'Longest string is: ' + longest
    print ''
print time.clock() - start_time