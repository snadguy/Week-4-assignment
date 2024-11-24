try:
    filename = input("Enter the filename to read:")
    with open(filename, 'r') as file:
        # read the file content
        content = file.read()
    
    # modify the content (add a line at the end)
    modified_content = content + "\n This line was added by the program"

    # create a new file for the modified content
    new_filename = "modified_" + filename

    # write the modified content to a new file
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

        print(f"The modified content has been written to  {new_filename} ")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist")
except IOError:
    print(f"Error: unable to read the file name '{filename}'.")