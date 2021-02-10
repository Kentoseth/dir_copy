import os

# https://stackoverflow.com/a/40347279
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

'''
Say that you put this script in the directory:
/home/user/crypto/

But you only want to copy subfolders from:
/home/user/crypto/bitcoin/

You will make list_dir look like so:
list_dir = fast_scandir("bitcoin/")

If you wanted to copy subfolders from:
/home/user/crypto/bitcoin/exchanges/

You will make list_dir look like so:
list_dir = fast_scandir("bitcoin/exchanges/")
'''
list_dir = fast_scandir("**ENTER_CUSTOM_PATH_HERE**")

# writing to file, all code below is from:
# https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/

with open('dir_list.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in list_dir)
