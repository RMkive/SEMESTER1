# Useful for editing youtube's live transcript (to replace the time)

name_file_in = input("Enter file input : ")
name_file_out = input("Enter file output : ")

with open(name_file_in, "r") as file_text :
    with open(name_file_out, "w") as file_out :
        for line in file_text :
            file_split = line.split()
            for char in file_split :
                if(":" in char) :
                    line = line.replace(char, "")
            line_r = line.strip()
            print(line_r, end=" ",file=file_out)