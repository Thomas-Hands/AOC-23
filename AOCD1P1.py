f = open('words.txt', 'r')
name = "fred"
lines = f.readlines()
total = 0
worddigits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
def checkforwords(line, pos):
    length = len(line)-1 - pos
    if line[pos] == 'o' and length >= 3:
        if line[pos+1] == 'n':
            if line[pos + 2] == 'e':
                return '1'
    elif line[pos] == 't':
        if line[pos + 1] == 'w'and length >= 3:
            if line[pos+2] == 'o':
                return '2'
        elif line[pos+1] == 'h'and length >= 5:
            if line[pos+2] == 'r':
                if line[pos + 3] == 'e':
                    if line[pos+4] == 'e':
                        return '3'
    elif line[pos] == 'f'and length >= 4:
        if line[pos+1] == 'o':
            if line[pos+2] == 'u':
                if line[pos + 3] == 'r':
                    return '4'
        elif line[pos+1] == 'i':
            if line[pos+2] == 'v':
                if line[pos+3] == 'e':
                    return '5'
    elif line[pos] == 's':
        if line[pos + 1] == 'i' and length >= 3:
            if line[pos + 2] == 'x':
                return '6'
        elif line[pos+1] == 'e'and length >= 5:
            if line[pos+2] == 'v':
                if line[pos+3] == 'e':
                    if line[pos+4] == 'n':
                        return '7'
    elif line[pos] == 'e'and length >= 5:
        if line[pos+1] == 'i':
            if line[pos+2] == 'g':
                if line[pos+3] == 'h':
                    if line[pos+4] == 't':
                        return '8'
    elif line[pos] == 'n'and length >= 4:
        if line[pos+1] == 'i':
            if line[pos+2] == 'n':
                if line[pos+3] == 'e':
                    return '9'
    return "none"
    
def findfirst(line):
    i = 0
    found = False
    while found == False:
        a = line[i]
        if a.isdigit():
            found = True
        else:
            if a == 'o' or a == 't' or a == 'f' or a == 's' or a == 'e' or a == 'n':
                b = checkforwords(line,i)
                if b.isdigit():
                    a = b
                    found = True
        i= i + 1
    return a


def findlast(line):
    found = False
    i = len(line)-1
    while found == False:
        a = line[i]
        if a.isdigit():
            found = True
        else:
            if a == 'o' or a == 't' or a == 'f' or a == 's' or a == 'e' or a == 'n':
                b = checkforwords(line,i)
                if b.isdigit():
                    a = b
                    found = True
        i= i - 1
    return a

#main code
for line in lines:
    pair = ""
    #find first num
    print(line)
    pair = pair + findfirst(line)
    #find last num
    pair = pair + findlast(line)
    print(pair)
    #cast
    try:
      pair = int(pair)
    except:
      print("cant cast to int")
    total = total + pair
print(total)
