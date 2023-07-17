# Lists: creating, deleting and updating
# Notice with a while loop we have to use and keyword if we want to add multiple conditions that we need to compare

#  test Sample
nameList = ["Max","John"]; surnameList = ["Steel","Cena"] ; genderList = ["Male","Male"] ; ageList = [26,33]      # we have created an empty list, just like in c++, in c++ we have arrays

def adder(names,surnames,ages,genders):     # Working, tested and tuned
    # Creating a for loop to keep the user in until they have entered enough names
    add = input("\nSelect A to Add a profile (q to quit): ")
    choices = ["a","A","q","Q"]
    while not add in choices:
        choices = input("\nInvalid Entry. Select A to add a profile (q to quit):" )
    quit = "n"
    while not quit == "q" and not quit == "Q":
        if add == "a" or add == "A":
                # an error I have been making is using colon : in the range bracket... NB, us a comma (start,end)...not (start:end))
                name = input("\nEnter the First Name: ");     # Note: this loop runs the exact amount times as the amount names that you wish to enter
                surname = input("Enter the Surname: ")
                age = int(input("Enter the Age: "))
                while age <  0 :
                    print("\nInvalid Age Entry. Age must be above 0: ")
                    age = int(input("Enter the Age: "))
                gender = input("Select Gender, M for Male / F for Female: ")
                choices = ["m","M","F","f"]
                while not gender in choices:
                    gender = input("\nInvalid Entry. Select M or F: ")
                if gender == "m" or gender == "M":
                    gender = "Male"
                else:
                    gender = "Female"
                names.append(name.capitalize())   # we appending the current name entered by the user to the list of names
                surnames.append(surname.capitalize()) # we doing the same with the surnames entered. By using append function we adding to the end of the list instead of overwriting
                ages.append(age)
                genders.append(gender)
                print("\n",name,surname + "'s Profile has been created")
                addProfile =input("\nWould you like to add another profile Y/N: ")
                choices = ['y','Y',"n","N"]
                while not addProfile in choices:
                    addProfile = input("\nInvalid Entry, Select Y to add a new profile or N to exit: ")
                if addProfile == "Y" or addProfile == "y":
                    continue
                else:
                    print("\nSaving all changes and exiting")
                    quit = "q"
        else:
            print("\nUndoing all changes and exiting")
            quit = "q"

# prints all the profiles
def printer(names,surnames,ages,genders):   # working
    print("\n")
    # we trying to use a for loop to print the names without showing brackets and '' NB: for loop did not work, while loop works best to getting the result I want
    length = len(names)      # incase you forgot, the len (), gives us the size/ amount of indexes a list has. so now we using the size/index count as our counter
    x = 0
    while x < length:   # so now we will print the full length of the list regardless of how many names we add
        print([x+1],names[x], surnames[x] + ", Age", ages[x],", Gender",genders[x])  # notice how we have written square bracket [x].
        # The x in the bracket is telling the ide that we want to access the specific index of the list. x is also the value of our counter
        # In short we saying at iteration 1, show index 1, at iteration 2 show index 2... but because indexes start on 0, we have to start our counter also on 0
        x = x + 1       # increments the size of x. This is a kill switch for the while loop. when x = numNames, loop breaks

# updating or Replacing the information  on the profiles 
def updater(names,surnames,ages,genders): # working
    printer(names,surnames,ages,genders)
    quit = "start"
    while not quit == "q" and not quit == "Q":
        print("\n\nTo update the information on a profile Select: N for Names, S for Surnames, A for Ages, G for Genders or R to Replace a Profile (q to quit):")
        update = input()
        choices = ["a","A","n","N","S","s","G","g","R","r","q","Q"]
        while not update in choices:
            print("\nInvalid Entry.")
            update = input("To update the information on a profile Select: N for Names, S for Surnames, A for Ages, G for Genders or R to replace a Profile (q to quit):\n")

        # updating the nameList # main algo for editing all the lits 
        if update == "n" or update == "N":  # works
            printer(names,surnames,ages,genders)
            index2update = int(input("\nSelect the number of the Profile you wish to update: ")) # index # of the name
            prevName = names[index2update - 1]    # Temp to hold the data of what is being edited
            prevSurname = surnames[index2update -1]
            print("\nDo you wish to edit:", prevName, prevSurname + "'s", "Profile")
            choice = input("Select Y/N: "); choices = ["Y","y","N","n"]
            while not choice in choices:
                choice = input("\nInvalid Entry. Select Y/N: ")
            if choice == "Y" or choice == "y":
                newName = input("\nEnter the new name: ").capitalize()
                names[index2update - 1] = newName
                print("\nYou have replaced the First Name", prevName, "with",newName)
                saveChoices = ["Y","y","N","n"] 
                save = input("Would you like to save the changes on this profile? Y/N: ")
                while not save in saveChoices:
                    save = input("Invalid Entry. Select Y/N: ")
                if save == "N" or save == "n":
                    names[index2update - 1] = prevName
                    print("\nUndoing changes on",prevName, prevSurname + "'s","Profile")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]    # quitting the main loop
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
                else:
                    print("\nSaved Successfully\n")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
            else:   # selected no to saving changes
                print("\nUndoing changes on",prevName, prevSurname + "'s","Profile\n")
                quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                while not quit in choices:
                    quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                if quit == "Y" or quit == "y":
                    quit = "start"
                else:
                    print("\nSaving all changes")
                    quit = "q"
            
        # updating surnameList
        elif update == "s" or update == "S":
            printer(names,surnames,ages,genders)
            index2update = int(input("\nSelect the number of the Profile you wish to update: ")) # index # of the name
            prevName = names[index2update - 1]    # Temp to hold the data of what is being edited
            prevSurname = surnames[index2update -1]
            print("\nDo you wish to edit:", prevName, prevSurname + "'s", "Profile")
            choice = input("Select Y/N: "); choices = ["Y","y","N","n"]
            while not choice in choices:
                choice = input("\nInvalid Entry. Select Y/N: ")
            if choice == "Y" or choice == "y":
                newSurname = input("\nEnter the new Surname: ").capitalize()
                surnames[index2update - 1] = newSurname
                print("\nYou have replaced the Surname", prevSurname, "with",newSurname)
                saveChoices = ["Y","y","N","n"] 
                save = input("Would you like to save the changes on this profile? Y/N: ")
                while not save in saveChoices:
                    save = input("Invalid Entry. Select Y/N: ")
                if save == "N" or save == "n":
                    surnames[index2update - 1] = prevSurname
                    print("\nUndoing changes on",prevName, prevSurname + "'s","Profile\n")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
                else:
                    print("\nSaved Successfully\n")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
            else:
                print("\nUndoing changes on",prevName, prevSurname + "'s","Profile\n")
                quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                while not quit in choices:
                    quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                if quit == "Y" or quit == "y":
                    quit = "start"
                else:
                    print("\nSaving all changes")
                    quit = "q"

        # updating Age list
        elif update == "a" or update == "A":
            printer(names,surnames,ages,genders)
            index2update = int(input("\nSelect the number of the Profile you wish to update: ")) # index # of the name
            prevAge = ages[index2update -1]  # temp to hold the current age on the profile
            prevAge = int(prevAge)  # Converting string entry to int
            print("\nDo you wish to edit the age on:", names[index2update - 1], surnames[index2update - 1] + "'s", "Profile")
            choice = input("Select Y/N: "); choices = ["Y","y","N","n"]
            while not choice in choices:
                choice = input("\nInvalid Entry. Select Y/N: ")
            if choice == "Y" or choice == "y":
                newAge = int(input("\nEnter the value of the new Age: "))
                while newAge < 1:
                    newAge = int(input("\nInvalid Entry. Age Must be above 0: "))
                ages[index2update - 1] = newAge      # access the index and updating its value
                print("\nYou have replaced the Age of", prevAge, "years with",newAge,"years")
                saveChoices = ["Y","y","N","n"]
                save = input("Would you like to save the changes on this profile? Y/N: ")
                while not save in saveChoices:
                    save = input("Invalid Entry. Select Y/N: ")
                if save == "N" or save == "n":
                    ages[index2update - 1] = prevAge     # restoring the original value back in the index to revert the changes made
                    print("\nUndoing changes on",names[index2update - 1], surnames[index2update - 1] + "'s","Profile\n")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
                else:
                    print("\nSaved Successfully\n")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
            else:
                print("\nUndoing changes on",names[index2update - 1], surnames[index2update - 1] + "'s","Profile\n")
                quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                while not quit in choices:
                    quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                if quit == "Y" or quit == "y":
                    quit = "start"
                else:
                    print("\nSaving all changes")
                    quit = "q"

            # updating the gender
        elif update == "g" or update == "G":
            printer(names,surnames,ages,genders)
            index2update = int(input("\nSelect the number of the Profile you wish to update: ")) # index # of the name
            prevGen = genders[index2update - 1]  # temp to hold the current age on the profile
            print("\nDo you wish to edit the gender on:", names[index2update - 1], surnames[index2update - 1] + "'s", "Profile")
            choice = input("Select Y/N: "); choices = ["Y","y","N","n"]
            while not choice in choices:
                choice = input("\nInvalid Entry. Select Y/N: ")
            if choice == "Y" or choice == "y":
                newGen = input("\nSelect the new gender M for Male / F for Female: ")
                genChoices = ["m","M","F","f"]
                while not newGen in genChoices:
                    newGen = input("\nInvalid Entry. Select M for Male / F for Female: ")
                if newGen == "M" or newGen == "m":
                    newGen = "Male"
                    genders[index2update - 1] = newGen      # access the index and updating its value through assignment
                    print("\nYou have replaced the gender of", prevGen, "with",newGen)
                    saveChoices = ["Y","y","N","n"]
                    save = input("Would you like to save the changes on this profile? Y/N: ")
                    while not save in saveChoices:
                        save = input("Invalid Entry. Select Y/N: ")
                    if save == "N" or save == "n":
                        genders[index2update - 1] = prevGen    # restoring the original value back in the index to revert the changes made
                        print("\nUndoing changes on",names[index2update - 1], surnames[index2update - 1] + "'s","Profile\n")
                        quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                        while not quit in choices:
                            quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                        if quit == "Y" or quit == "y":
                            quit = "start"
                        else:
                            print("\nSaving all changes")
                            quit = "q"
                    else:
                        print("\nSaved Successfully\n")
                        quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                        while not quit in choices:
                            quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                        if quit == "Y" or quit == "y":
                            quit = "start"
                        else:
                            print("\nSaving all changes")
                            quit = "q"
                else:
                    newGen = "Female"
                    genders[index2update - 1] = newGen      # access the index and updating its value through assignment
                    print("\nYou have replaced the gender of", prevGen, "with",newGen)
                    saveChoices = ["Y","y","N","n"]
                    save = input("Would you like to save the changes on this profile? Y/N: ")
                    while not save in saveChoices:
                        save = input("Invalid Entry. Select Y/N: ")
                    if save == "N" or save == "n":
                        genders[index2update - 1] = prevGen    # restoring the original value back in the index to revert the changes made
                        print("\nUndoing changes on",names[index2update - 1], surnames[index2update - 1] + "'s","Profile\n")
                        quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                        while not quit in choices:
                            quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                        if quit == "Y" or quit == "y":
                            quit = "start"
                        else:
                            print("\nSaving all changes")
                            quit = "q"
                    else:
                        print("\nSaved Successfully\n")
                        quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                        while not quit in choices:
                            quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                        if quit == "Y" or quit == "y":
                            quit = "start"
                        else:
                            print("\nSaving all changes")
                            quit = "q"
            else:
                print("\nUndoing changes on",names[index2update - 1], surnames[index2update - 1] + "'s","Profile\n")
                quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                while not quit in choices:
                    quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                if quit == "Y" or quit == "y":
                    quit = "start"
                else:
                    print("\nSaving all changes")
                    quit = "q"

        # replacing a Profile
        elif update == "R" or update == "r":
            printer(names,surnames,ages,genders)
            index2update = int(input("\nSelect the number of the Profile you wish to replace: ")) # index # of the name
            prevName = names[index2update - 1]    # Temp to hold the data of what is being edited
            prevSurname = surnames[index2update -1]
            prevAge = ages[index2update - 1]
            prevGen = genders[index2update - 1]
            print("\nDo you wish to replace:", prevName, prevSurname + "'s", "Profile")
            choice = input("Select Y/N: "); choices = ["Y","y","N","n"]
            while not choice in choices:
                choice = input("\nInvalid Entry. Select Y/N: ")
            if choice == "Y" or choice == "y":
                newName = input("\nEnter a new First Name: ").capitalize()
                names[index2update - 1] = newName
                newSurname = input("Enter a new Surname: ").capitalize()
                surnames[index2update - 1] = newSurname
                newAge = int(input("Enter a new Age: "))
                while newAge < 1:
                    newAge = input("\nInvalid Entry. Age must be above 0: ")
                ages[index2update - 1] = newAge
                newGen = input("Select the Gender (M for Male / F for Female): ")
                genChoices = ["M","m","F","f"]
                while not newGen in genChoices:
                    newGen = input("\nInvalid Entry. Select M for Male / F for Female: ")
                if newGen == "M" or newGen == "m":
                    newGen = "Male"
                    genders[index2update - 1] = newGen
                else:
                    newGen = "Female"
                    genders[index2update - 1] = newGen
                print("\nYou have replaced", prevName,prevSurname + "'s Profile", "with the",newName,newSurname +"'s Profile")
                print("\nOld Profile:",prevName, prevSurname,"Age",prevAge,"Gender",prevGen )
                print("New Profile:",newName, newSurname,"Age",newAge, "Gender", newGen)
                saveChoices = ["Y","y","N","n"]
                save = input("\nWould you like to save these changes? Y/N: ")
                while not save in saveChoices:
                    save = input("Invalid Entry. Select Y/N: ")
                if save == "N" or save == "n":
                    names[index2update - 1] = prevName
                    surnames[index2update - 1] = prevSurname
                    ages[index2update - 1] = prevAge
                    genders[index2update - 1] = prevGen
                    print("Undoing changes on",prevName, prevSurname + "'s","Profile\n")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
                else:
                    print("\nSaved Successfully\n")
                    quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                    while not quit in choices:
                        quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                    if quit == "Y" or quit == "y":
                        quit = "start"
                    else:
                        print("\nSaving all changes")
                        quit = "q"
            else:
                print("\nUndoing changes on",prevName, prevSurname + "'s","Profile\n")
                quit = input("\nDo you wish to edit another Profile Y/N: "); choices = ["Y","y","n","N"]
                while not quit in choices:
                    quit = input("\nInvalid Entry. \nY to edit another Profile (N to Exit): ")
                if quit == "Y" or quit == "y":
                    quit = "start"
                else:
                    print("\nSaving all changes")
                    quit = "q"

        # quitting the program
        else:
            print("\nUndoing all changes and exiting the program!")
            quit = "q"

# deleting Profiles
def deleter(names,surnames,ages,genders): # working
    # Replacing and editing
    quit = "n"
    while not quit == "Q" and not quit == "q":
        choice = input("\n\nSelect D to delete a Profile (q to quit): ")
        choices = ['d','D',"q","Q"]
        while not choice in choices:
            choice = input("\nInvalid Entry. Select D to delete or Q to quit: ")
        if choice == "D" or choice == "d":
            printer(names,surnames,ages,genders)
            index2update = int(input("\nSelect the number of the Profile you wish to delete: ")) # index # of the name
            prevName = names[index2update - 1]    # Temp to hold the data of what is being edited
            prevSurname = surnames[index2update -1]
            prevAge = ages[index2update - 1]
            prevGen = genders[index2update - 1]
            print("\nAre you certain you want to delete:", prevName, prevSurname + "'s", "Profile")
            choice = input("Select Y/N: "); choices = ["Y","y","N","n"]
            while not choice in choices:
                choice = input("\nInvalid Entry. Select Y/N: ")
            if choice == "Y" or choice == "y":
                del names[index2update - 1]      # we using the del keyword instead of .remove() because with the del keyword all we need to do is specify the index to delete from
                del surnames[index2update - 1]
                del ages[index2update - 1]
                del genders[index2update - 1]
                print("\n")
                print(prevName,prevSurname + "'s Profile has been deleted.")
                
                quit = input("\nDo you wish to delete another Profile Y/N: "); choices = ["Y","y","n","N"]
                while not quit in choices:
                    quit = input("\nInvalid Entry. \nY to delete another Profile (N to Exit): ")
                if quit == "Y" or quit == "y":
                    quit = "start"
                else:
                    print("\nSaving all changes")
                    quit = "q"
            else:
                print("\nUndoing changes on",prevName, prevSurname + "'s","Profile\n")
                quit = input("\nDo you wish to delete another Profile Y/N: "); choices = ["Y","y","n","N"]
                while not quit in choices:
                    quit = input("\nInvalid Entry. \nY to delete another Profile (N to Exit): ")
                if quit == "Y" or quit == "y":
                    quit = "start"
                else:
                    print("\nSaving all changes")
                    quit = "q"
                
        # quitting the program
        else:
            print("\nUndoing all changes and exiting the program!")
            quit = "q"

                
def mainMenu():
    print("\nMain Menu:")
    print("\nA) Add a new Profile \nB) Update existing Profiles \nC) Delete an existing Profile \nD) Display current Profiles on Database")
    menuChoice = input("\nSelect A, B, C, D (E to exit): "); choices = ["A","a","B","b","C","c","D","d","E","e"]
    while not menuChoice in choices:
        menuChoice = input("\nInvalid Entry. \nSelect A, B, C, D (E to exit): ")
    return menuChoice

def main(names,surnames,ages,genders):
    menuChoice = mainMenu()
    if menuChoice == "A" or menuChoice == "a":
        adder(names,surnames,ages,genders)
        printIt = input("\nDisplay existing Profiles? Y/N: "); choices = ["Y","y","n","N"]
        while not printIt in choices:
            printIt = ("\nInvalid Entry. Select Y/N: ")
        if printIt == "Y" or printIt == "y":
            printer(names,surnames,ages,genders)
            exit = input("\n\nM to return to Main Menu (E to exit): "); choices = ["M","m","E","e"]
            while not exit in choices:
                exit = input("\nInvalid Entry. \nSelect M to return to Main Menu (E to Exit): ")
            if exit == "M" or exit == "m":
                main(names,surnames,ages,genders)
            else:
                print("\nSaving all changes and exiting.")
        else:
            exit = input("\n\nM to return to Main Menu (E to exit): "); choices = ["M","m","E","e"]
            while not exit in choices:
                exit = input("\nInvalid Entry. \nSelect M to return to Main Menu (E to Exit): ")
            if exit == "M" or exit == "m":
                main(names,surnames,ages,genders)
    elif menuChoice == "B" or menuChoice == "b":
        updater(names,surnames,ages,genders)
        printIt = input("\nDisplay existing Profiles? Y/N: "); choices = ["Y","y","n","N"]
        while not printIt in choices:
            printIt = ("\nInvalid Entry. Select Y/N: ")
        if printIt == "Y" or printIt == "y":
            printer(names,surnames,ages,genders)
            exit = input("\n\nM to return to Main Menu (E to exit): "); choices = ["M","m","E","e"]
            while not exit in choices:
                exit = input("\nInvalid Entry. \nSelect M to return to Main Menu (E to Exit): ")
            if exit == "M" or exit == "m":
                main(names,surnames,ages,genders)
            else:
                print("\nSaving all changes and exiting.")
        else:
            exit = input("\n\nM to return to Main Menu (E to exit): "); choices = ["M","m","E","e"]
            while not exit in choices:
                exit = input("\nInvalid Entry. \nSelect M to return to Main Menu (E to Exit): ")
            if exit == "M" or exit == "m":
                main(names,surnames,ages,genders)
    elif menuChoice == "C" or menuChoice == "c":
        deleter(names,surnames,ages,genders)
        printIt = input("\nDisplay existing Profiles? Y/N: "); choices = ["Y","y","n","N"]
        while not printIt in choices:
            printIt = ("\nInvalid Entry. Select Y/N: ")
        if printIt == "Y" or printIt == "y":
            printer(nameList,surnameList,ageList,genderList)
            exit = input("\n\nM to return to Main Menu (E to exit): "); choices = ["M","m","E","e"]
            while not exit in choices:
                exit = input("\nInvalid Entry. \nSelect M to return to Main Menu (E to Exit): ")
            if exit == "M" or exit == "m":
                main(names,surnames,ages,genders)
            else:
                print("\nSaving all changes and exiting.")
        else:
            exit = input("\n\nM to return to Main Menu (E to exit): "); choices = ["M","m","E","e"]
            while not exit in choices:
                exit = input("\nInvalid Entry. \nSelect M to return to Main Menu (E to Exit): ")
            if exit == "M" or exit == "m":
                main(names,surnames,ages,genders)
    elif menuChoice == "D" or menuChoice == "d":
        printer(names,surnames,ages,genders)
        exit = input("\n\nM to return to Main Menu (E to exit): "); choices = ["M","m","E","e"]
        while not exit in choices:
           exit = input("\nInvalid Entry. \nSelect M to return to Main Menu (E to Exit): ")
        if exit == "M" or exit == "m":
            main(names,surnames,ages,genders)
        else:
            print("\nSaving all changes and exiting.")


main(nameList,surnameList,ageList,genderList)


#updater(nameList,surnameList,ageList,genderList)
#adder(nameList,surnameList,ageList,genderList)
#deleter(nameList,surnameList,ageList,genderList)
#printer(nameList,surnameList,ageList,genderList)



