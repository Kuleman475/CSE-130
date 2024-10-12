import math

print("Welcome to monopoly!")

allOneColor = input("Do you have all the green properties? y/n ")


if allOneColor.lower() == "y":
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
                    if houseToBuild == 0:
                         print("There are not enough houses available for purchase at this time.")
                    if hotelToBuild == 0:
                        print("There are not enough hotels available for purchase at this time.")
            swap = input("would you like to swap? y/n ")
            if swap == "y":
                swapNC = input("would you like to swap NC? y/n ")
                if swapNC == "y":
                    print(f"Swap North Carolina's hotel with Pennsylvania's 4 houses.")
                    exit()
                swapPC = input("Would you like to swap with Pacific? y/n ")
                if swapPC == "y":
                    print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
                    exit()
            else:     
                money = int(input("how much $ do you have? $"))
                if money >= 200:
                    buildingHouses = int(input("how many houses"
                    " would you like to build? "))
                    buildingHotels = int(input("how many hotels"
                    " would you like to build? "))
                    if buildingHouses > houseToBuild:
                        print(" There are not enough houses available for purchase at this time.")
                        exit()
                    elif buildingHotels > hotelToBuild:
                        print("There are not enough hotel available for purchase at this time.")
                        exit()
                    else:
                        newPAhouses = int(input("how many houses would you like to put on Pennyslvania Ave? "))
                        newPacifichouses = int(input("how many houses would you like to put on Pacific Ave? "))
                        newNChouses = int(input("how many houses would you like to put on North Carolina Ave? "))
                        if buildingHotels > 0:
                            PAhotel = input("would you like to put hotel on Pennyslvania Ave? y/n ")
                            Pacifichotel = input("would you like to put hotel on Pacific Ave? y/n ")
                            NChotel = input("would you like to put hotel on North Carolina Ave? y/n ")
                    if PAhouses == 5:
                        print("You cannot purchase a hotel if the property already has one. ")
                        exit()
                        
                        if PAhotel == "y":
                            PAhouses = Hotel
                        if Pacifichotel == "y":
                            Pacifichouses = Hotel
                        if NChotel == "y":
                            NChouses = Hotel
                    HouseCost = buildingHouses * 200
                    hotelCost = buildingHotels * 200
                    print(f"Total Cost $", hotelCost + HouseCost)
                    print(f"you purchased {buildingHotels} hotels and {buildingHouses} houses")
                else:
                    print("You do not have sufficient funds to purchase anything at this time.") 
else: 
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
