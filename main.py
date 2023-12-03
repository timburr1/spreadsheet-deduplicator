master_dict = {}
last_names = {"FAKE_NAME"}

# Last Name,First Name,Grade Level,Teacher
with open('All Students.csv') as fp:
    for line in fp:
        # print(line)
        line = line.strip()
        pieces = line.split(",")
        key = pieces[1].casefold() + pieces[0].casefold()
        master_dict[key] = line
        last_names.add(pieces[0].casefold())

# Last Name,First Name
with open('Club Students.csv') as fp:
    for line in fp:
        #print(line)
        line = line.strip()
        pieces = line.split(",")
        thisKey = pieces[1].casefold() + pieces[0].casefold()
        if thisKey in master_dict:
            master_dict.pop(thisKey)
        elif pieces[0].casefold() in last_names:
            print(pieces[0])

file = open("result.csv", "a")

for key in master_dict:
    # print(master_dict[key])
    file.write(master_dict[key] + "\n")

file.close()