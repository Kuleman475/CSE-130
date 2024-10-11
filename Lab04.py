import math

print("Welcome to monopoly!")

allOneColor = input("Do you have all the green properties? y/n ")


if allOneColor.lower() == "y":
        money = int(input("how much $ do you have? $"))
        if money >= 200:
            print("how many houses are on each propetry")
            print("if hotel put '5'")
            Hotel = 5
            NChouses = int(input("how many houses are on your North Carolina property? "))
            PAhouses = int(input("how many houses are on your Pennysilvania property? "))
            Pacifichouses = int(input("how many houses are on your Pacific property? "))
            check1 = (math.isclose(Pacifichouses, PAhouses, abs_tol = 1))
            check2 = (math.isclose(PAhouses, NChouses, abs_tol = 1))
            check3 = (math.isclose(Pacifichouses, NChouses, abs_tol = 1))
            if NChouses == Hotel and PAhouses == Hotel and Pacifichouses == Hotel:
                print("Congratulations you have all of your properties are maxed out!")
            elif NChouses > Hotel or PAhouses > Hotel or Pacifichouses > Hotel:
                print("You can only have one hotel on each property")
            else:
                if check1 == True and check2 == True and check3 == True:
                    houseToBuild = int(input("how many houses are available? "))
                    hotelToBuild = int(input("how many hotels are available? "))
                    buildingHouses = int(input("how many houses"
                    " would you like to build? "))
                    buildingHotels = int(input("how many hotels"
                    " would you like to build? "))
                    if buildingHouses > houseToBuild:
                        print(" There are not enough houses available for purchase at this time.")
                    elif buildingHotels > hotelToBuild:
                        print("There are not enough hotel available for purchase at this time.")
                    else:
                        numHouses = Pacifichouses + NChouses + PAhouses
                        totalHouses = numHouses - buildingHouses
                        print(totalHouses, "houses")


                        # HouseCost = buildingHouses * 200
                        # if NChouses == 4 or PAhouses == 4 or Pacifichouses == 4:
                        #     hotelCost = buildingHotels * 200

                else: print("the houses and hotels need to be distributed evenly.")
        else:
            print("You do not have sufficient funds to purchase a hotel at this time.")
    # how many hotels/ houses are there to build?
    # do you want to build a hotel/house?    

    
else: 
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
