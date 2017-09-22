import re #Regular expression

InvalidNames = []
CleanNames = []

def GetName(names):
    for name in names:
        try:
            if(name.isnumeric() == False and name.isalpha() == True and name.isspace() == False):
                GetCleanNames(name) #get dirty names (without hyphen)
            elif(re.match('^([a-zA-Z]*-[a-zA-Z]*)+$',name)):
                GetHyphenNames(name) #get dirty names (with hyphen)
            elif(name.isalpha() == False or name.isspace() == True or name.isnumeric() == True):
                GetInvalidNames(name) #get invalid names
        except Exception as arg:
            print('Error filtering data !',arg)
                    
def GetInvalidNames(name):
    global InvalidNames
    try:
        InvalidNames.append(name)
    except Exception as arg:
        print('Error appending invalid data !', arg)

def GetCleanNames(name):
    global CleanNames
    try: #cleaned names without hyphen
        CleanNames.append(name[0].upper() + name[1:].lower())
    except Exception as arg:
        print('Error formatting data !', arg)

def GetHyphenNames(name):
    global CleanNames
    try:
        for i in range(0,len(name)):
            if(name[i] == '-'): #format names with hyphen
                CleanNames.append(name[0].upper() + name[1:i].lower() + '-' + name[i+1].upper() + name[(i+2):].lower())
    except Exception as arg:
        return
        #print('Error formatting name with hyphen !', arg)
