import FileIO #Module for 

File10000 = "10000DirtyNames.csv"
File100000 = "100000DirtyNames.csv"
File10000000 = "10000000DirtyNames.csv"
CleanNames = "CleanNames.csv"
InvalidNames = "InvalidNames.csv"

#100000DirtyNames.csv
try: 
    FileIO.ReadFile(File100000) #read csv file
    FileIO.WriteInvalidNames(InvalidNames,'w') #write invalid names
    print('Successfully write InvalidNames.csv file to hardrive (100000DirtyNames.csv)')
except Exception as arg:
    print('Error transmitting data !',arg)

try: #write
    FileIO.ReadFile(File100000) #read csv file
    FileIO.WriteCleanNames(CleanNames,'w') #write clean names
    print('Successfully write CleanNames.csv file to hardrive (100000DirtyNames.csv)')
except Exception as arg:
    print('Error transmitting data !',arg)

print('\n')

#10000DirtyNames.csv
try: 
    FileIO.ReadFile(File10000) #read csv file
    FileIO.WriteInvalidNames(InvalidNames,'a') #write invalid names
    print('Successfully write InvalidNames.csv file to hardrive (10000DirtyNames.csv)')
except Exception as arg:
    print('Error transmitting data',arg)

try:
    FileIO.ReadFile(File10000) #read csv file
    FileIO.WriteCleanNames(CleanNames,'a') #write clean names
    print('Successfully write CleanNames.csv file to hardrive (10000DirtyNames.csv)')
except Exception as arg:
    print('Error transmitting data',arg)
    

#10000000DirtyNames.csv
#try: 
#    FileIO.ReadFile(File10000000) #read csv file
#    FileIO.WriteInvalidNames(InvalidNames,'a') #write invalid names
#    print('Successfully write InvalidNames.csv file to hardrive (10000000DirtyNames.csv)')
#except Exception as arg:
#    print('Error transmitting data',arg)

#try:
#    FileIO.ReadFile(File10000000) #read csv file
#    FileIO.WriteCleanNames(CleanNames,'a') #write clean names
#    print('Successfully write CleanNames.csv file to hardrive (10000000DirtyNames.csv)')
#except Exception as arg:
#    print('Error transmitting data',arg)
    





