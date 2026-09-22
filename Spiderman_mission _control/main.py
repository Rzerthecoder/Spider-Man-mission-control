class Hero:
   def __init__(self,name,city,health,energy):
      self.name=name
      self.city=city
      self.health=health
      self.energy=energy
   def display(self):
      print("Name:",self.name)
      print("City:",self.city)
      print("Health:",self.health)
      print("Energy:",self.energy)
print("Spiderman mission control")
print("=========================")
print("systems online")
print("Wlecome spiderman")
hero1=Hero("Spiderman","NYC",100,100)
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
choice=0
while choice!=7:
 choice=int(input("Enter choice:"))
 if choice==1:
   hero1.display()
 elif choice==2:
    print("===Missions===")
    print(l)
 elif choice==3:
    mis=input("Enter mission:")
    loc=input("Enter location:")
    diff=input("Enter difficulty:")
    new_mis={
       "Mision name":mis,
       "Location":loc,
       "Difficulty":diff,
       "Status":"Incomplete"
    }
    l.append(new_mis)
    print("new mission list is",l)
 elif choice==4:
    search=input("Enter the mission you want to search:")
    for missions in l:
       if search==missions["Mission name"]:
          print("This mission is available")
          break
    else:
          print("This mission is not available")
 elif choice == 5:
    comp_search = input("Enter the mission you finished: ")
    
    for mission in l:
        if mission["Mission name"] == comp_search:
            mission["Status"] = "Complete"
            print("Status updated to Complete!")
            break
 elif choice == 6:
    target_diff = input("Enter difficulty (Easy, Medium, Hard): ")
    for mission in l:
        if mission["Difficulty"] == target_diff:
            print("Mission found:", mission["Mission name"], "at", mission["Location"])        
 elif choice==7:
    print("--EXITING--")
    break
 else:
    print("incorrect choice")    

    
 


