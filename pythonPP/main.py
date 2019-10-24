"""
Molecular dynamics internship program
Created by: Andre
"""
print("Hello, Which program are we running today?")
from MDFile import File

ACTIVE = True
while ACTIVE:
    user_input = input("1. Input and output of position and velocity in (.dat) file\n"
                       "2. Graph positions and velocities in (.dat) file\n"
                       "3. Open (.dat) file in a particle visualizer\n"
                       "4. Simulation of a 2D fluid using (.dat) file\n"
                       "5. Calculate particle clusters using (.dat) file\n"
                       "6. Quit\n")
    if user_input.lower().strip() == "quit":
        break
    elif int(user_input.strip('.')) == 6:
        break
    elif int(user_input.strip('.')) == 1:

        dat_file_in = input("Write file direction\n")
        File dat_file(dat_file_in)
        print(f"You have selected {dat_file_in} file")
        user_input = input("Select an option:\n"
                           "1. Only read (results on the screen)\n"
                           "2. Only write (results in the output file)\n"
                           "3. Both\n")
        if int(user_input.strip('.')) == 1:
            dat_file.read()
            user_input = ""
        elif int(user_input.strip('.')) == 2:
            file_name = input("Write a name for generated output file\n")
            dat_file.write(file_name)
            user_input = ""
        elif int(user_input.strip('.')) == 3:
            file_name = input("Write a name for generated output file\n")
            dat_file.read()
            dat_file.write(file_name)
            user_input = ""