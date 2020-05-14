# in prompts, must assign vaiables to themselves with the float function to turn them into flaots

import math

# SIMPLE INTEREST FUNCTIONS 
def simint (ini,rat,tim,per): 
    int = (ini * rat * tim * per) 
    print("\nInterest = $%s\n" % (int))
# INITIAL
def simini (int,rat,tim,per):
    ini = (int / (rat * tim * per))
    print("\nInitial = $%s\n" % (ini))
# RATE
def simrat (int,ini,tim,per):
    rat = (int / (ini * tim * per))
    rat = rat * 10
    print("\nRate = %s%%\n" % (rat))
# TIME
def simtim (int,ini,rat,per):
    tim = (int / (ini * rat * per))
    print("\nTime = %s Years\n" % (tim))
# APPLIED PER YEAR
def simper (int,ini,rat,tim):
    per = (int / (ini * rat * tim))
    if per == 1:
       print("\nInterest Applied Once Per Year\n")
    else:
        print("\nInterest Applied %s Times Per Year\n" % (per))

# COMPOUND INTEREST FUNCTIONS
def comtot (ini,rat,tim,per): 
    tot = ini * ((1 + (rat / per)) ** (per * tim))
    print("\nInterest = $%s\n" % (int))
# INITIAL
def comini (tot,rat,tim,per):
    ini =  (tot / ((1 + (rat * per)) ** (per * tim)))
    print("\nInitial = $%s\n" % (ini))
# RATE
def comrat (tot,ini,tim,per):
    rat = per(((tot/ini) ** (1.0 / (per * tim))) - 1)
    rat = rat * 10
    print("\nRate = %s%%\n" % (rat))
# TIME
def comtim (tot,ini,rat,per):
    tim = (((math.log(tot / ini)) / (math.log(1 + (rat / per)))) / per)
    print("\nTime = %s Years\n" % (tim))
# APPLIED PER YEAR
#def comper (tot,ini,rat,tim):
#    per = "blank"
#    if per == 1:
#       print("\nInterest Applied Once Per Year\n")
#    else:
#        print("\nInterest Applied %s Times Per Year\n" % (per))

# MAIN
while True:
      # SHOW USER HOW TO RESTART AND QUIT PROGRAM ALONG WITH PROMPT ASKING WHETHER TO USE SIMPLE OR COMPOUND FUNCTIONS
      print("To restart the program type \"restart\" / \"r\". To quit type \"quit\" / \"q\" / \"exit\" / \"e\".")
      sel = input("Simple Interest (s) or Compound Interest (c)?\n")

      # RESTART AND QUIT FOR "SEL"
      if sel == "restart" or sel == "r":
         continue
      elif sel == "quit" or sel == "q" or sel == "exit" or sel == "e":
           quit()

      # PROMPT USER ASKING WHICH VALUE TO FIND, ASSUMES USER ALREADY KNOWS THE REST OF THE VALUES EXCEPT FOR THE ONE UNKNOWN
      elif sel == "s":
           print("What would you like to find? Interest (int), initial amount of money (ini), the rate of interest (rat), the time spent investing (tim), or how many times the interest is applied per year (per)?") 
           fin = input()

           # RESTART AND QUIT FOR "FIN"
           if fin == "restart" or fin == "r":
              continue
           elif fin == "quit" or fin == "q" or fin == "exit" or fin == "e":
                quit()

           # FIND INTEREST
           elif fin == "int":

                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    ini = float(ini)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    rat = float(rat)
                rat = rat * .01

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    tim = float(tim)

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    per = float(per)

                # FUNCTION
                simint(ini,rat,tim,per)

           # FIND INITIAL
           elif fin == "ini":

                # INTEREST
                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    int = float(int)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    float(rat)
                rat = rat * .01

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    tim = float(tim)               

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    per = float(per)

                # FUNCTION
                simini(int,rat,tim,per)

           # FIND RATE
           elif fin == "rat":

                # INTEREST
                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()               
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    int = float(int)

                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    ini = float(ini)

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    tim = float(tim)

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    per = float(per)

                # FUNCTION
                simrat(int,ini,tim,per)

           # FIND TIME
           elif fin == "tim":

                # INTEREST
                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()               
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    int = float(int)

                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    ini = float(ini)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    rat = float(rat)
                rat = rat * .01

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    rat = float(per)

                # FUNCTION
                simtim(int,ini,rat,per)               

           # FIND PER
           elif fin == "per":

                # INTEREST
                print("\nEnter the interest without the $ sign (Ex. 40.25): ")
                int = input()               
                if int == "restart" or int == "r":
                   continue
                elif int == "quit" or int == "q" or int == "exit" or int == "e":
                     quit()
                else:
                    int = float(int)
      
                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    ini = float(ini)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    rat = float(rat)
                rat = rat * .01               

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    tim = float(tim)

                # FUNCTION
                simper(int,ini,rat,tim)

           else:
               print("That is not a valid option, restarting.")

      # PROMPT USER ASKING WHICH VALUE TO FIND, ASSUMES USER ALREADY KNOWS THE REST OF THE VALUES EXCEPT FOR THE ONE UNKNOWN
      elif sel == "c":
           print("What would you like to find? Total (tot), initial amount of money (ini), the rate of interest (rat), the time spent investing (tim), or how many times the interest is applied per year (per)?") 
           fin = input()

           # RESTART AND QUIT FOR "FIN"
           if fin == "restart" or fin == "r":
              continue
           elif fin == "quit" or fin == "q" or fin == "exit" or fin == "e":
                quit()

           # FIND TOTAL
           elif fin == "tot":

                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    ini = float(ini)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    rat = float(rat)
                rat = rat * 0.01

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    tim = float(tim)

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    per = float(per)

                # FUNCTION
                comtot(ini,rat,tim,per)

           # FIND INITIAL
           elif fin == "ini":

                # TOTAL
                print("\nEnter the total without the $ sign (Ex. 40.25): ")
                tot = input()
                if tot == "restart" or tot == "r":
                   continue
                elif tot == "quit" or tot == "q" or tot == "exit" or tot == "e":
                     quit()
                else:
                    tot = float(tot)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    rat = float(rat)
                rat = rat * .01

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    tim = float(tim)               

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    per = float(per)

                # FUNCTION
                comini(tot,rat,tim,per)

           # FIND RATE
           elif fin == "rat":

                # TOTAL
                print("\nEnter the total without the $ sign (Ex. 40.25): ")
                tot = input()
                if tot == "restart" or tot == "r":
                   continue
                elif tot == "quit" or tot == "q" or tot == "exit" or tot == "e":
                     quit()
                else:
                    float(tot)

                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    float(ini)

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    float(tim)

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    float(per)

                # FUNCTION
                comrat(tot,ini,tim,per)

           # FIND TIME
           elif fin == "tim":

                # TOTAL
                print("\nEnter the total without the $ sign (Ex. 40.25): ")
                tot = input()
                if tot == "restart" or tot == "r":
                   continue
                elif tot == "quit" or tot == "q" or tot == "exit" or tot == "e":
                     quit()
                else:
                    float(tot)

                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    float(ini)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    float(rat)
                rat = rat * .01

                # PER
                print("\nEnter how many times the interest is applied per year (EX. 3.4): ")
                per = input()
                if per == "restart" or per == "r":
                   continue
                elif per == "quit" or per == "q" or per == "exit" or per == "e":
                     quit()
                else:
                    float(per)

                # FUNCTION
                comtim(tot,ini,rat,per)               

           # FIND PER
           elif fin == "per":

                # TOTAL
                print("\nEnter the total without the $ sign (Ex. 40.25): ")
                tot = input()
                if tot == "restart" or tot == "r":
                   continue
                elif tot == "quit" or tot == "q" or tot == "exit" or tot == "e":
                     quit()
                else:
                    float(tot)     

                # INITIAL
                print("\nEnter the initial amount of money without the $ sign (EX. 5025.23): ")
                ini = input()
                if ini == "restart" or ini == "r":
                   continue
                elif ini == "quit" or ini == "q" or ini == "exit" or ini == "e":
                     quit()
                else:
                    float(ini)

                # RATE
                print("\nEnter the rate of interest in percentage form without the % sign (EX. 9.4): ")
                rat = input()
                if rat == "restart" or rat == "r":
                   continue
                elif rat == "quit" or rat == "q" or rat == "exit" or rat == "e":
                     quit()
                else:
                    float(rat)
                rat = rat * .01               

                # TIME
                print("\nEnter the length of investment in years (EX. 0.5): ")
                tim = input()
                if tim == "restart" or tim == "r":
                   continue
                elif tim == "quit" or tim == "q" or tim == "exit" or tim == "e":
                     quit()
                else:
                    float(tim)

                # FUNCTION
                comper(tot,ini,rat,tim)

      # ERROR CHECKING
      else:
       print("That is not a valid option, restarting.")
