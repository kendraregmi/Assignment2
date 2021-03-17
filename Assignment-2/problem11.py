# Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?


fileName = input("Enter a file name: ")
fileext = fileName.split('.')
file = repr(fileext[:-1])
file_wout_bracs = str(file[1:-1])
print(file_wout_bracs[1:-1])