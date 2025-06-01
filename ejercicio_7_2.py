# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Find the position of the number
    colon_pos = line.find(':')
    number_str = line[colon_pos + 1:].strip()
    try:
        number = float(number_str)
    except:
        print("Could not convert to float:", number_str)
        continue
    count += 1
    total += number
if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No lines with X-DSPAM-Confidence found")
fh.close()