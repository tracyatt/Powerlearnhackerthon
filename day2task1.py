books = int(input("enter the number of books that you have purchased this month : "))

if books == 0 :
    print("you have earned 0 points")
elif books == 1 :
    print("you have earned 6 points")
elif books == 2 :
    print("you have earned 16 points")
elif books == 3:
    print("you have earned 32 points")
elif books >= 4:
  print("you have earned 60 points")   
