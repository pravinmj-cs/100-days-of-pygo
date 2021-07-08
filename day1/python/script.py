#1. create a greeting for your program
print("********** Welcome **********")

#2. Ask the user for city that they grew up in
city = input("Enter the name of the city you grew up in: ")

#3. Ask the user for the name of the pet
pet = input("Enter the name of your favourite pet: ")

#4. Combine the name of their city and pet and show them their band name
band_name = city + " " + pet

#5. Make sure the input cursor shows on new line
print("\n The name of your band is  ", band_name)


#one liner
print(f"\n The name of your band is {input('Enter the name of the city you grew up in: ')} \n {input('Enter the name of your favourite pet: ')}")