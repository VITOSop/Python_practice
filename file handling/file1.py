#create new file
with open("new_file.txt","w"):
    print("new file created")


# write into the file
message="""Hello .......this is file handling
           This is decomd line.
           Now im writing 3rd line."""

with open("new_file.txt","w") as fp:
    fp.write(message)
with open("new_file.txt","a") as fp:
    fp.write(message)

# read from the file

with open("new_file.txt","r") as fp:
    contents=fp.read()

print(contents)
