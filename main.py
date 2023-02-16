import os

# Python program showing
# a use of input()
 
path_to_userprofile_folder = input("Enter the full path to your profile folder: ")
print(path_to_userprofile_folder)

# checking if the chrome folder exists 

# exist or not.
if not os.path.exists(path_to_userprofile_folder + "/chrome"):
    # if the chrome folder is not present 
    # then create it.
    os.makedirs(path_to_userprofile_folder + "/chrome")

rw_path = path_to_userprofile_folder + "/chrome"

# Check if the right files exist within the folder (rw_path) - i.e pictures etc.

# Reading the file

# Library of settings
#   Matching true or false on each setting & displaying in in the GUI as such

# Variables for the changes that the user has made in the GUI

# Change the true or false statement so that it shows up in the GUI

# Writing the changes to the file (using the variables above)





