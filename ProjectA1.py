#Get the list of all files from a specific folder
#print out how many files are in the folder
#print out all file names
#print out the length of each file name
import os

def my_files():
#Get list of file names from a folder
    my_file_list = os.listdir(r"<path>")
    
#Print the list of files from the specified directory    
    print(my_file_list)

#Get the current working directory
    var_saved_path = os.getcwd()

#Print the current working directory
    print("CURRENT WORKING DIRECTORY " + var_saved_path)
    
#Change the current working directory to the path listed
    os.chdir(r"<path>")

#Print out the newly changed current working directory
    print("NEW DIRECTORY " + os.getcwd())  
    print("")

#Count the number of files in the folder
    number_of_files = len(os.walk("<path>").next()[2])

#Print out the number of files
    print("Number of files: " + str(number_of_files))
    print("")
    
#For each file: print out the file name, print out the length of each file name
    for fileee_name in my_file_list:
        print("Name of File: "+ fileee_name)
        print("Length of " + "'" + fileee_name + "'" + ": " +str(len(fileee_name)))
        print("")
        
#Change the current working directory back to the original path       
    os.chdir(var_saved_path)

#Print out the current working directory
    print("DIRECTORY CHANGED BACK TO "+ os.getcwd())
      
my_files()
