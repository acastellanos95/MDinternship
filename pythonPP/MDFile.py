import csv
from typing import List, Any


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self, print_statement=True):
        r_pos = []
        v_vel = []
        data_in_file = []

        # Open file with csv reader
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
            for row in reader:
                data_in_file.append(row)
        f.close()

        # convert data from string to float numbers
        data_in_file_float = list()
        for row in data_in_file:
            data_in_file_float.append([float(i) for i in row])
        num_pos = data_in_file_float[0][0]

        # Assign positions and velocities
        for i in range(2, len(data_in_file_float)):
            r_pos.append(data_in_file_float[i][1:4])
            v_vel.append(data_in_file_float[i][4:7])

        # Calculate Kinectic Energy K
        kin_energy = 0
        for j in v_vel:
            kin_energy += (1 / 2) * (j[0]) ** 2 + (j[1]) ** 2 + (j[2]) ** 2
        # Calculate Potential Energy U
        u_energy = 0
        for j in r_pos:
            u_energy += (1 / 2) * (j[0]) ** 2 + (j[1]) ** 2 + (j[2]) ** 2
            if print_statement:
                print(f"Your file has {int(num_pos)} of positions and velocities")
                print(f"Kinetic Energy = {kin_energy} and Potential Energy = {u_energy}.\n"
                      f"The total energy is {kin_energy + u_energy}")
        return num_pos, kin_energy, u_energy, r_pos, v_vel

    def write(self, new_file_name):
        # Passing variables of read method
        num_pos, kin_energy, u_energy, r_pos, v_vel = self.read(print_statement=False)
        # new attribute
        self.new_file_name = new_file_name
        # Write in file
        with open(self.new_file_name, 'w') as new_file:
            new_file.write(f"Your file has {int(num_pos)} of positions and velocities\n")
            new_file.write(f"Kinetic Energy = {kin_energy} and Potential Energy = {u_energy}.\n"
                           f"The total energy is {kin_energy + u_energy}")
            for u, v in zip(r_pos, v_vel):
                str1 = ','.join(str(x) for x in u)
                str2 = ','.join(str(y) for y in v)
                new_file.writelines(f"{str1},{str2}\n")

    def graph(self):
        from matplotlib import pyplot
        from mpl_toolkits.mplot3d import Axes3D
        num_pos, kin_energy, u_energy, r_pos, v_vel = self.read(print_statement=False)
