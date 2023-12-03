master_dict = {}

# Last Name,First Name,Grade Level,Teacher
with open('All Students.csv') as fp:
    for line in fp:
        # print(line)
        line = line.strip()
        pieces = line.split(",")
        key = pieces[1].casefold() + pieces[0].casefold()
        master_dict[key] = line

# Last Name,First Name
with open('Club Students.csv') as fp:
    for line in fp:
        #print(line)
        line = line.strip()
        pieces = line.split(",")
        thisKey = pieces[1].casefold() + pieces[0].casefold()
        if thisKey in master_dict:
            master_dict.pop(thisKey)

for key in master_dict:
    # todo: write to file instead
    print(master_dict[key])
    pass
