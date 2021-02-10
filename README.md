# dir_copy - Copy folders/subfolders between 2 locations

dir_copy is a set of 2 dependency-free Python scripts to copy only folders/subfolders(some people use the words directories/subdirectories) between 2 locations.

These scripts were written to be able to recreate a folder/subfolder structure found in a container and the host OS.

If you are attempting to copy a set of folders/subfolders on your Unix OS directly, there are many commands that are just as easy to use.

The scripts only depend on Python3.

## Contents
 * [Requirements](#requirements)
 * [Installation](#installation)
 * [Usage](#usage)
 * [Modify](#modify)
 * [License](#license)
 * [Queries](#queries)

## Requirements

 * Python3

## Installation

`git clone https://github.com/Kentoseth/dir_copy.git`

or

Copy/Paste the scripts from GitHub into the desired folders as explained in the usage below.

## Usage

This section explains how these scripts work and also how to use them.

dir_copy has 2 scripts:

 1. 0_subfolder_list.py
 2. 1_folder_maker.py

The folders are named according to their usage(0_ then 1_).

Say you have a container that contains a folder/subfolder structure you want to replicate on your OS.

In your container, the path of the folder/subfolder structure you want to copy is located at:

`/mounted/container/crypto/`

Within your `crypto/` folder, you have various subfolders(and folders below them). What you do is the following:

`cd mounted/container/`
`touch 0_subfolder_list.py`

(You can also copy/paste the `0_subfolder_list.py` file into the `/container/` folder)

Go to the following line in the file:

`list_dir = fast_scandir("**ENTER_CUSTOM_PATH_HERE**")`

and change it to:

`list_dir = fast_scandir("crypto/")`

Run the file:

`python 0_subfolder_list.py`

This will create a file called: `dir_list.txt`.

Now navigate to the destination where you want to recreate the folder/subfolder structure:

`cd /home/user/crypto_backup/`

Copy `dir_list.txt` to this folder and add the second script to this folder:

`touch 1_folder_maker.py`

(You can also copy/paste the `1_folder_maker.py` file into the `/crypto_backup/` folder)

Now run the file:

`python 1_folder_maker.py`

The end result is that all folders/subfolders will be created in the path:

`home/user/crypto_backup/crypto/*`

## Modify

These scripts can also be modified to also copy over all files within various subfolders.

## License

This project is licensed under the open-source "MIT" license.

The full license text is available in the file LICENSE

## Queries

Open an Issue to discuss

-----

If you find this project interesting or useful, please star it and share it with colleagues and friends.