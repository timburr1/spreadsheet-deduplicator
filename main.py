master_dict = {}

# Last Name,First Name,Grade Level,Teacher
with open('All Students.csv') as fp:
    for line in fp:
        print(line)
        # todo read master list into map("first,last": data)

# Last Name,First Name
with open('Club Students.csv') as fp:
    for line in fp:
        print(line)
        # todo: create key like first,last
        thisKey = "f,l"
        master_dict.pop(thisKey)

for key in master_dict:
    # todo: write to file instead
    print(master_dict[key])
