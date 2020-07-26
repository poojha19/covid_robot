def is_num_valid(value):
#this function checks if the input is an integer
    try:
        val = int(value)
        return True
    except ValueError:
        return False

def is_num_float(temperature):
#this function checks if imput is a float
    try:
        temp = float(temperature)
        return True
    except ValueError:
        return False
    
def input_age():
#this function checks if the age is valid
    age = input("What is your age (Enter a number between 0 and 100): ")
    while True:
        if is_num_valid(age) == False:
            age = input("Please enter a valid number: ")
        if is_num_valid(age) == True and int(age) >= 0 and int(age) <= 100:
            return age
        else:
            age = input("Please enter a valid number: ")
            
def input_temperature():
#this function checks if the body temperature entered is reasonable
    temperature = input("What is your current body temperature (in degrees C): ")
    while True:
        if is_num_float(temperature) == False:
            temperature = input("Please enter a valid number: ")
        if is_num_float(temperature) == True and float(temperature) >= 0 and float(temperature) <= 50:
            return temperature
        else:
            temperature = input("Please a valid number: ")

def input_coughs():
#this function checks for a valid number of coughing episodes
    coughs = input("How many coughing episodes have you had in the last 24 hours: ")
    while True:
        if is_num_valid(coughs) == False:
            coughs = input("Please enter a valid number: ")
        if is_num_valid(coughs) == True and int(coughs) >= 0 and int(coughs) <= 50:
        #variable range
            return coughs
        else:
            coughs = input("Please enter a valid number: ")
            

    
def difficulty_breathing():
#function to check how difficult it is to breathe
    difficulty_breathing = input("On a scale of 1 to 10, how difficult is it to breathe: ")
    while True:
        if is_num_valid(difficulty_breathing) == False:
            difficulty_breathing = input("Please enter a valid number: ")
        if is_num_valid(difficulty_breathing) == True and int(difficulty_breathing) >= 0 and int(difficulty_breathing) <= 10:
            return difficulty_breathing
        else:
            difficulty_breathing = input("Please enter a valid number: ")

def congestion():
#function to check ho congested they feel
    congestion = input("On a scale of 1 to 10, how congested do your lungs feel: ")
    while True:
        if is_num_valid(congestion) == False:
            congestion = input("Please enter a valid number: ")
        if is_num_valid(congestion) == True and int(congestion) >= 0 and int(congestion) <= 10:
            return congestion
        else:
            congestion = input("Please enter a valid number: ")

def vomiting():
#function to check the number of times they vomitted.
    vomiting = input("How many times have you vomited in the last 24 hours: ")
    while True:
        if is_num_valid(vomiting) == False:
            vomiting = input("Please enter a valid number: ")
        if is_num_valid(vomiting) == True and int(vomiting) >= 0 and int(vomiting) <= 10:
            return vomiting
        else:
            vomiting = input("Please enter a valid number: ")

def duration():
#function to check how long sympotoms lasted
    duration = input("How long (days) have your symptoms lasted: ")
    while True:
        if is_num_valid(duration) == False:
            duration = input("Please enter a valid number: ")
        if is_num_valid(duration) == True and int(duration) >= 0 and int(duration) <= 10:
            return duration
        else:
            duration = input("Please enter a valid number: ")


age = input_age()
body_temperature = input_temperature()
no_of_coughing_episodes = input_coughs()
scale_of_breathing = difficulty_breathing()
scale_of_congestion = congestion()
no_of_vomiting = vomiting()
no_of_days = duration()

print("Age is: ", age)
print("Body Temperature is: ", body_temperature, " degrees C")
print("Number of coughing episodes is: ", no_of_coughing_episodes)
print("Difficulty breathing is: ", scale_of_breathing)
print("Level of congestion is: ", scale_of_congestion)
print("They vomitted ", no_of_vomiting, " times.")
print("Symptoms lasted: ", no_of_days, " days.")

##code to implement by Austin
##def austin_function(age, body_temperature, no_of_coughing_episodes, scale_of_breathing, scale_of_congestion, no_of_vomiting, no_of_days):
    



