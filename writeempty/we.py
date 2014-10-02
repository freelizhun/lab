
message =' '
try:
    # This will create a new file or **overwrite an existing file**.
    f = open("file.txt", "w")
    try:
        f.write(message) # Write a string to a file
        #f.writelines(lines) # Write a sequence of strings to a file
    finally:
        f.close()
except IOError:
    pass
