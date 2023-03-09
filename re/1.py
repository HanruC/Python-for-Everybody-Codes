import re

def main():
    file = open('text.txt')
    numlist = list()
    for line in file:
        for word in line.split():
            number = re.findall('[0-9]+', word)
            urlnum = re.findall('^www.([0-9]+)?/', word)
            if len(number) != 1: continue 
            num = int(number[0])
            #numurl = int(urlnum[1])
            numlist.append(num)
            #numlist.append(numurl)
    print(urlnum)
    print((numlist))
    print('sum', sum(numlist))
    
        
main()
    
    
    
    
