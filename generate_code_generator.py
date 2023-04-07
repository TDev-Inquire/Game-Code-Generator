import random
import time
import os
import string

# define the character set for the steam codes
char_set = string.ascii_uppercase + string.digits

# define the format for the steam codes
code_format = "{}{}{}{}{}-{}{}{}{}{}-{}{}{}{}{}-{}{}{}{}{}-{}{}{}{}{}"

# create a directory to store the generated codes
folder_name = str(len(os.listdir(".")) + 1)
os.mkdir(folder_name)

# prompt the user for the number of files to generate
num_files = int(input("How many files do you want to generate? "))

# prompt the user for the number of codes per file
codes_per_file = 50

# generate the codes and save them to files
start_time = time.time()
codes = set()
for i in range(num_files):
    file_name = f"steam_codes_{i+1}.txt"
    with open(os.path.join(folder_name, file_name), "w") as f:
        for j in range(codes_per_file):
            while True:
                code = code_format.format(*random.choices(char_set, k=25))
                if code not in codes:
                    codes.add(code)
                    break
            f.write(code + "\n")
            print(code)
end_time = time.time()
total_time = end_time - start_time
print(f"Generated {num_files * codes_per_file} steam codes in {total_time:.2f} seconds.")
