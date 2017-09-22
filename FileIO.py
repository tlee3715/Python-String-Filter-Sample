import StringFilter #Module for filtering and formatting string


def ReadFile(filename):
    try:
        with open(filename,'r') as file:
            for names in file:
                name = names.split(',')
                StringFilter.GetName(name)
            file.close()
    except IOError:
        print('Error reading file !',IOError)
        
        
def WriteInvalidNames(filename,mode):
    try:
         with open(filename,mode) as file:
             file.write(str(StringFilter.InvalidNames))
             file.close()
    except IOError:
        print('Error writing invalid names to file !',IOError)
        
    
def WriteCleanNames(filename,mode):
    try:
         with open(filename,mode) as file:
             file.write(str(StringFilter.CleanNames))
             file.close()
    except IOError:
        print('Error writing clean names to file !',IOError)

