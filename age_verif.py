def age():
  while True:
    age=input ("Enter your age: ")
    try:
      user_age =int(age)
      if user_age >=21:
        print("Welcome in!")
        break
      else:
        print("Underage!")
        break
    except ValueError:
      print("Must be a number!")
  return user_age
age()
