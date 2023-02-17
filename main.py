import os
#import customtkinter

#customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("dark-blue")

#root = customtkinter.CTk()
#root.geometry("1000x600")

#def login():
#    print("test")

#frame = customtkinter.CTkFrame(master=root)
#frame.pack(pady=20, padx=60, fill="both", expand=True)

#label = customtkinter.CTkLabel(master=frame, text="Enter the full path to your profile folder: ")
#label.pack(pady=12, padx=10)

#entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Path goes here")
#entry1.pack(pady=12, padx=10)

#button_path = customtkinter.CTkButton(master=frame, text="Continue", command=login)
#button_path.pack(pady=12, padx=10)

#root.mainloop()

# GRAPHICAL SETUP - IGNORE FOR NOW
 
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
# if it does not exist, download them from github

# Reading the file

# Defines the path to the file within the folder
path_css = rw_path + "/userChrome.css"
path_cfg = rw_path + "/csstomUI.txt"


# Check if the userChrome.css file exists, and then creates it if it does not
if os.path.exists(path_css):
    print("warning: userChrome.css already exists within the chrome folder")
else:
    with open(path_css, "w") as fp:
        fp.write("")
# Writes empty space in the file

# Check if the config file exists, and then creates it if it does not
if os.path.exists(path_cfg):
    print("warning: csstomUI config file already exists within the chrome folder")
else:
    with open(path_cfg, "w") as fp:
        fp.write("")
# Writes empty space in the file






# Library of settings
#   Matching true or false on each setting & displaying in in the GUI as such - config.py hosts the settings



# Variables for the changes that the user has made in the GUI

# Change the true or false statement so that it shows up in the GUI

# Writing the changes to the file (using the variables above)





