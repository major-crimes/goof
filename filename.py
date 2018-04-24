all_things = " "

for i in range(3):
    category = input("Enter a category: ")
    for j in range(3):
       thing = input("Enter something in that category: ")  
       all_things = all_things + " " + thing
    print str(category) + ": " + all_things
    all_things = " "


