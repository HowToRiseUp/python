CURRENT_YEAR = 2023 #constant varialbe
CURRENT_TO_FEET = 3.281

first_name = input("Firsr Name :")
last_name = input("Last Name :")
year_born = input("Year Born: ")
height_metter = input("Your height (meter): ")

year_born = int(year_born)
age = CURRENT_YEAR - year_born
height_metter = float(height_metter)
height_feet = height_metter * CURRENT_TO_FEET
height_feet = round(height_feet,1)

print("\n--------")
print("The {0} {1} {2} is {3} years old and {4} feet tall".format(CURRENT_YEAR, last_name, first_name, age, height_feet))


