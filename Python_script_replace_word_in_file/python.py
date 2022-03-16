#!/usr/bin/python

def replace(filename,current_string,replace_string):
    replace_file = ""
    file = open(filename, "r")
    for line in file:
        line = line.replace(current_string,replace_string)
        replace_file = replace_file + line
    file.close()

    output_file = open(filename, "w")
    output_file.write(replace_file)
    output_file.close()

filename = input("Please enter the filename with full location: ")
current_string = input("Please enter the string/word which you want to replace: ")
replace_string = input("Please enter the replacing string: ")

replace(filename,current_string,replace_string)