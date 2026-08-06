dob_file = ""

#Open the DOB.text file and read the lines
with open('DOB.txt', 'r+') as dob_file:
    lines = dob_file.readlines()

    #Initialise two lists for names and birth dates
    name_list = []
    birthdate_list = []

    #Splitting
    for line in lines:
        
    #Split each line into parts (name and birth dates)
                 
        #Splitting each line
        parts = line.rsplit(' ', 3)                  #Split the words in each line into parts keeping the first names and surnames together
        raw_name = parts[0]                          #The first part is the full name
        raw_birthdate = ' '.join(parts[1:4])         #Joins the last 3 parts to form the birthdates

        #Checks for above values
        #print(parts)                            
        #print(raw_name)
        #print(raw_birthdate)

        #Append results to respective lists
        name_list.append(raw_name)
        birthdate_list.append(raw_birthdate.replace("\n", ""))

    #Print "Name" and respective list 
    print("Name")
    print("\n".join(name_list))
    print("\n")                                       #Formatting

    #Print "Birthdate" and respective list
    print("Birthdate")
    print("\n".join(birthdate_list))