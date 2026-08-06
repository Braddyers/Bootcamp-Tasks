# Total cost for hotel stay
def hotel_cost(num_nights):               
    hotel_per_night = 750                                                                                                # Cost per night at hotel
    return num_nights * hotel_per_night                                                                                  # Multipy nights by price per night


# Total cost for the flight
def plane_cost(city_flight):                                                                                             # our options as cities, listed with corresponding flight prices
    if city_flight == "Paris":
        return 1000
    elif city_flight == "China":
        return 1750
    elif city_flight == "Sydney":
        return 1300
    elif city_flight == "Tokyo":
        return 2000
    else:
        print("City is not listed as a distination.")                                                                   # To check if the input is valid.
        return 0


# Total cost for car rental
def car_rental(rental_days):
    daily_rental_cost = 250                                                                                             # Cost per per day for car rental
    return rental_days * daily_rental_cost                                                                              # Multiply days by price per day


# Total holiday cost function
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    return total_hotel_cost + total_plane_cost + total_car_rental_cost



# Main program to get user inputs and calculate holday cost
print("This is a holiday cost calculator. Please answer the following questions: \n")
    

# Valid city options
valid_cities = ["Paris", "China", "Sydney", "Tokyo"]

# Ask user to enter a city and validate their input
while True:
    city_flight = input("Which city do you want to fly to (Paris, China, Sydney, or Tokyo)? ").strip().capitalize()   # Capitalise and strip excess characters
    if city_flight in valid_cities:                                                                                   # Check if it is a valid city
        break
    else:
        print("Invalid city.")                                                                                        


# Ask the user for the number of nights they will be staying in a hotel
num_nights = (input("How many nights will you stay at a hotel? "))

# Validation check to make sure input is a positive integer
while not (num_nights.isdigit() and int(num_nights) > 0):                                                            # Check if input is a number and positive
    print("Invalid input. Please enter a positive integer.")
    num_nights = input("How many nights will you stay at a hotel? ")
num_nights = int(num_nights)                                                                                         # Convert into an integer


# Ask user for the number of days they will rent a car for
rental_days = (input("How many days will you hire a car for? "))

# Validation check to make sure input is a positive integer
while not (rental_days.isdigit() and int(rental_days) > 0):                                                          # Check if input is a number and positive
    print("Invalid input. Please enter a positive integer.")
    rental_days = input("How many days will you hire a car for? ")
rental_days = int(rental_days)                                                                                       # Convert to an integer
    

# Calculate the total cost
total_cost = holiday_cost(num_nights, city_flight, rental_days)
    

# Cost breakdown simplified with f-strings
print(f"\n--- Holiday cost breakdown for {city_flight} ---")
print(f"Hotel cost for {num_nights} nights: R{hotel_cost(num_nights)}.")
print(f"Flight cost to {city_flight}: R{plane_cost(city_flight)}")
print(f"Car rental cost for {rental_days} days: R{car_rental(rental_days)}")
print(f"The total cost of your holiday: R{total_cost}.")



