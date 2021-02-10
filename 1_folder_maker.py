import os

# open file and read the content in a list
with open('dir_list.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:

        # remove linebreak which is the last character of the string
        current_place = line[:-1]
        
        # print(current_place)
        
        # https://stackoverflow.com/a/17890088
        os.makedirs(current_place)
