# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
    for line in fh:
        print(line.upper().strip())
    fh.close()
except FileNotFoundError:
    print("File cannot be opened:", fname)
