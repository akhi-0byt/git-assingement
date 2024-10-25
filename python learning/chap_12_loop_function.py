# monthly_saving = float(input("enter your monthly saving  "))
# number_of_years = float(input("enter your saving years  "))
# tatal_saving = monthly_saving*12*number_of_years
# print(float(tatal_saving))


# there are two types of loop 
# first is while Loop 

x = 0
while x<5:
    print(x)
    x=x+1

# second is for loop 

for x in range(10,20):
    print(x)

#arrays means data set 
days = ("mon","tue","wedn","thur","fri","sat","sun")

for d in days:
    # if d == "sat": break # stop the loop
      if d == "wedn":continue # skip the loop
      print(d)