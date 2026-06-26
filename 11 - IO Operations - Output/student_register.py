#Initialize variables
loop_counter = input("How many students are registering? ")

#Input check as positive integer
while not loop_counter.isdigit() or int(loop_counter) <= 0:       #Check if input not a digit or input not <= 0
    print("Oops. Please enter a positive integer.")
    loop_counter = input("How many students are registering? ")   #Re-ask if input invalid.
       

#Creation of text file + formatting + close text file
with open("reg_form.txt", "w") as reg_form:
    reg_form.write("Student ID:" + "\n")


#Loop for the number of students registering (number of students == loops)
for i in range(int(loop_counter)):
    
    #Ask fir Student ID
    student_id = input("Student ID: ")                            
    
    #Open text file + add student ID with formatting + close text file
    with open('reg_form.txt', 'a') as reg_form:
        reg_form.write("\n" + student_id + "\n" + "------------------------" + "\n")



    