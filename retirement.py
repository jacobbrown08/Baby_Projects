#How much money does the person already have, how tall is their "pile"
pile = int(input("How much money do you already have saved? "))

#How much money will they have allotted per year
spend = int(input("How much money will you spend per year? "))

#How old is the user currently
age = int(input("How old are you right now? "))

#Age the user plans to retire
retire = int(input("At what age do you expect to retire? "))

#How many years do they expect to live
death = int(input("At what age do you expect to pass away? "))

#print how much money they need to save in order to achieve this retirement savings goal
print("You will need to save $", ((((death - retire) * spend) - pile) / (retire-age)), " per year in order to achieve this goal.")