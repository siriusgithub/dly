# Simple Interest Functions SIMPLE INTEREST FUNCTIONS 
def simint (ini,rat,tim,per): 
    int = (ini * rat * tim * per) 
    print("\nInterest = $%s\n" % (int))
# INITIAL
def simini (int,rat,tim,per):
    ini = (int / (rat * tim * per))
    print("\nInitial = $%s\n" % (ini))
# Rate
def simrat (int,ini,tim,per):
    rat = (int / (ini * tim * per))
    rat = rat * 10
    print("\nRate = %s%%\n" % (rat))
# Time
def simtim (int,ini,rat,per):
    tim = (int / (ini * rat * per))
    print("\nTime = %s Years\n" % (tim))
# Applied Per Year
def simper (int,ini,rat,tim):
    per = (int / (ini * rat * tim))
    if per == 1:
       print("\nInterest Applied Once Per Year\n")
    else:
        print("\nInterest Applied %s Times Per Year\n" % (per))

# Compound Interest Functions

# Main
while True:
      # Show User how to restart and close program
      print("To restart the program type \"restart\" / \"r\". To quit type \"quit\" / \"q\" / \"exit\" / \"e\".")
      # Ask user whether to solve using simple or compound functions 
      sel = input("Simple Interest (s) or Compound Interest (c)?\n")

      # Restart and quit for "sel"
      if sel == "restart" or sel == "r":
         continue
      elif sel == "quit" or sel == "q" or sel == "exit" or sel == "e":
           quit()

      # Simple interest selection and prompt for finding specific unknown, given that all other values are known
      elif sel == "s":
           print("What would you like to find? Interest (int), initial amount of money (ini), the rate of interest (rat), the time spent investing (tim), or how many times the interest is applied per year (per)?") 
           fin = input()

           # Restart and Quit for "fin"
           if fin == "restart" or fin == "r":
              continue
           elif fin == "quit" or fin == "q" or fin == "exit" or fin == "e":
                quit()

           # Finding Interest
           elif fin == "int":


                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    float(ini)

                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    float(rat)
                rat = rat * .01

                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    float(tim)

                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    float(per)

                simint(ini,rat,tim,per)


           elif fin == "ini":


                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    float(int)

                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    float(rat)
                rat = rat * .01

                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    float(tim)               

                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    float(per)

                simini(int,rat,tim,per)


           elif fin == "rat":


                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()               
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    float(int)

                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    float(ini)

                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    float(tim)

                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    float(per)

                simrat(int,ini,tim,per)

           elif fin == "tim":
                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()               
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    float(int)

                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    float(ini)

                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    float(rat)
                rat = rat * .01

                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    float(per)

                simtim(int,ini,rat,per)               

           elif fin == "per":
                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()               
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    float(int)

                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    float(ini)

                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    float(rat)
                rat = rat * .01               

                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    float(tim)

                simper(int,ini,rat,tim)

           else:
               print("That is not a valid option, restarting.")

      else:
       print("That is not a valid option, restarting.")
