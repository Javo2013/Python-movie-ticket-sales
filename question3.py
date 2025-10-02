# question3.py

#input 
pet_type = input("enter pet type (dog/cat/bird/hamster):")
human_age = int(input("enter your pet's age in human years:"))

#conversion
if pet_type == 'dog:' or pet_type == 'cat':
  if human_age <=2:
     pet_age = human_age * 12  
  else:
   pet_age = 24 + (human_age - 2) * 4
elif pet_type == "bird":
  pet_age = human_age * 9
elif pet_type == "hamster":
    pet_age = human_age * 25
  
else:
   print("sorry, unsupported pet type.")
   pet_age = 0

#print result
print("\n===Pet Age Conversion ===")
print(f"pet Type: {pet_type.capitalize}")
print(f"human age:{human_age} years")
print(f"pet age: {pet_age} pet years")
print(f"/n A fun fact: your {pet_type} is like a {pet_age}-year-old human!")
