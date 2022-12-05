from datetime import date
def main():
    print('''
     _______________________________________________________________
    |                       * Your Choice ... *                     | 
    |                                                               |      
    |  •  ENTER "1" To Move Further & Calculate The Leap Years >>>  |            
    |                                                               |      
    |  •  PRESS ANY DIGIT TO EXIT >>>                               |                      
    |_______________________________________________________________|       ''')
    print("")
    User_Choose = int(input("⦿  ENTER YOUR CHOICE : "))
    print("")
    print("")

    if User_Choose == 1:
        print("~~~  PLEASE FILL THE BELOW DETAILS  ~~~~")
        print("")
        print("TO PRINT ALL THE LEAP YEARS & NON LEAP YEARS IN RANGE >>>")
        print("")
        First_date = input(" ⦿  Enter Starting Date Range In Format (DD/MM/YYYY) : ")
        print("")

        Current_Date = input(" ⦿  Enter Closing Date Range In Format (DD/MM/YYYY) : ")
        print("")

        list1 = First_date.split("/")
        list2 = Current_Date.split("/")

        start_year = int(list1[2])
        end_year = int(list2[2])

        leap_year = []
        non_leap_year = []
        for x in range(start_year,end_year+1):
            if(x % 400 == 0) and (x % 100 == 0):
                leap_year.append(x)
            elif(x % 4 ==0) and (x % 100 != 0):
                leap_year.append(x)
            else:
                non_leap_year.append(x)
    else:
        print("Exited >>>")
        exit()
    print(f"► LEAP YEAR'S ARE >>> {leap_year}")
    print("")
    print(f"► NON LEAP YEAR'S ARE >>> {non_leap_year}")
main()