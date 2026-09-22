print("Spiderman mission control")
print("=========================")
print("systems online")
print("Wlecome spiderman")
a="Hero: spiderman"
b="City: new york"
c=("Health:" ,100)
d=("Energy:",100)
e={
    "Mission name":"Stop bank robbery",
    "Location":"Manhatten",
    "Difficulty":"Medium",
    "Status":"Incomplete"
}
m={
   "Mission name":"Stop scorpean",
   "Location":"Brooklyn",
   "Difficulty":"Hard",
   "Status":"Incomplete"
}
p={
   "Mission name":"Stop a theif",
   "Location":"Queens",
   "Difficulty":"Easy",
   "Status":"Incomplete"
}
l=[e,m,p]
print("What you want")
print("View hero info")
print("View missions")
print("Add missions")
print("Search four missions")
print("Complete a mission")
print("Filter by difficulty")
print("Exit")
while True:
 n=int(input("enter option:"))
 if n==1:
    print(a)
    print(b)
    print(c)
    print(d)
 elif n==2:
    print("===Missions===")
    print(l)
 elif n==3:
    mis=input("Enter mission:")
    loc=input("Enter location:")
    diff=input("Enter difficulty:")
    dict={
       "Mision name":mis,
       "Location":loc,
       "Difficulty":diff,
       "Status":"Incomplete"
    }
    l.append(dict)
    print("new mission list is",l)
 elif n==4:
    search=input("Enter the mission you want to search:")
    for missions in l:
       if search==missions["Mission name"]:
          print("This mission is available")
          break
    else:
          print("This mission is not available")
 elif n == 5:
    comp_search = input("Enter the mission you finished: ")
    
    for mission in l:
        if mission["Mission name"] == comp_search:
            mission["Status"] = "Complete"
            print("Status updated to Complete!")
            break  # Stops the loop immediately because we found it
 elif n == 6:
    target_diff = input("Enter difficulty (Easy, Medium, Hard): ")
    
    for mission in l:
        if mission["Difficulty"] == target_diff:
            # Prints the name and where it is
            print("Mission found:", mission["Mission name"], "at", mission["Location"])        
 else:
    print("--EXITING--")
    break


