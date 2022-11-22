import csv

try:
    print("Welcome to Titanic passenger analyzer")
    file_name = input("Enter filename for titanic data:\n")
    with open(file_name, 'r') as titanicFile:
        titanic = csv.reader(titanicFile)
        numberOfPassenger = -1
        for i in titanic:
            if len(i[3]) != 0:
                numberOfPassenger = int(numberOfPassenger) + 1
        print('The file contains '+str(numberOfPassenger)+' passengers')
    titanicFile.close()
    while True:
        print("")
        print("You can do the following")
        print("1) Calculate passengers with missing ages")
        print("2) Calculate passengers without a cabin")
        print("3) Calculate average age of passengers (skip missing ages)")
        print("0) Exit")
        selection = -1
        # while True:
        try:
            selection = int(input("Your choice:"'\n'))

        except ValueError:
            print('Faulty user input. Exiting.')
            break
        if selection == 1:
            missingAgeCounter = 0
            properAgeCounter = -1
            with open(file_name, 'r') as titanicFile:
                titanic = csv.reader(titanicFile)
                for i in titanic:
                    if len(i[5]) == 0:
                        print(i[3], 'was missing age')
                        missingAgeCounter = missingAgeCounter + 1
                    else:
                        properAgeCounter = properAgeCounter + 1
            titanicFile.close()
            print('We had ' + str(missingAgeCounter) + ' passengers with missing age')
            print('We have ' + str(properAgeCounter) + ' passengers with proper age')
        if selection == 2:
            missingCabinCounter = 0
            properCabinCounter = -1
            with open(file_name, 'r') as titanicFile:
                titanic = csv.reader(titanicFile)
                for i in titanic:
                    if len(i[10]) == 0:
                        print(i[3], 'was missing cabin')
                        missingCabinCounter = missingCabinCounter + 1
                    else:
                        properCabinCounter = properCabinCounter + 1
            titanicFile.close()
            print('We had ' + str(missingCabinCounter) + ' passengers with missing cabin')
            print('We have ' + str(properCabinCounter) + ' passengers with proper cabin')
        if selection == 3:
            ageList = []
            missingAgeCounter1 = 0
            properAgeCounter1 = -1
            with open(file_name, 'r') as titanicFile:
                titanic = csv.reader(titanicFile)
                for i in titanic:
                    if len(i[5]) != 0:
                        ageList.append(i[5])
                        properAgeCounter1 = properAgeCounter1 + 1
                    else:
                        missingAgeCounter1 = missingAgeCounter1 + 1
                ageList.remove("Age")
            titanicFile.close()
            ageAverage = 0
            for j in ageList:
                age = float(j)
                ageAverage = ageAverage + age
            print('We had ' + str(missingAgeCounter1) + ' passengers with missing age')
            print('We have ' + str(properAgeCounter1) + ' passengers with proper age')
            print("Average age of all "+str(properAgeCounter1)+" passengers was "+str(round(ageAverage / len(ageList)))+" years")
        if selection == 0:
            break

except FileNotFoundError:
    print("Error processing file '{}', stopping.".format(file_name))
# except OSError:
# print("The file was empty, no car brand was recognized.")
