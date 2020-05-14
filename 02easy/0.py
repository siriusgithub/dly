def simint (initial,rate,time,per):
           interest = ((initial * rate * time) / per)
           print("\nThe interest accumulated is $%s" % (interest))

def simpri (interest,rate,time):
           initial = ((interest/time) / rate)
           print("\nThe initial amount of money was $%s" % (initial))

def simrat (initial,time,interest):
           rate = (((interest / 3) / initial) * 10)
           print("\nThe rate of interest is \%%s" % (rate))

def simtim (initial,interest,rate):
           time = ((interest / initial) / rate)
           print(
                """
                  \nThe initial value of $%s was invested for %s years. The initial amount of money plus the
                  interest gives a total of $%s
                """ 
                % (initial,time,(initial + interest))
                 )

def comint (initial,rate,time,per):
           interest = (initial * (1 + (rate / per)) * (time * per))
           print("\nThe interest accumulated is $%s" % (interest))

restart = False
quit = False

while restart == False | quit == False

print("Simple Interest (s) or Compound Interest (c)?")

sel = input()

if sel == "s":
   print(
        """
          What would you like to find? Interest (i), initial amount of money/starting amount of money (s), the 
          rate of interest (r), or the time spent investing (t)? 
         """
         )

   find = input() 

   if find == "i":
      print("\nPlease enter the initial amount of money without the $ sign (EX. 5025.23): ")
      initial = float(input())
      print("\nPlease enter the rate of interest in percentage form without the % sign (EX. 9.4): ")
      rate = float(input())
      rate = rate * .01
      print("\nPlease enter the length of investment in years (EX. 0.5): ")
      time = float(input())

      simint(initial,rate,time)

   if find == "s":
      print("\nPlease enter the interest accumulatted (EX. 336.03): ")
      interest = float(input())
      print("\nPlease enter the rate of interest in percentage form without the % sign (EX.9.4): ")
      rate = float(input())
      rate = rate * .01
      print("\nPlease enter the length of investment in years (EX. 0.5): ")
      time = float(input())

      simpri(interest,rate,time)

   if find == "r":
      print("\nPlease enter the initial amount of money without the $ sign (EX. 5025.23): ")
      initial = float(input())
      print("\nPlease enter the length of investment in years (EX. 0.5): ")
      time = float(input())
      print("\nPlease enter the interest accumulatted (EX. 336.03): ")
      interest = float(input())

      simrat(initial,time,interest)

   if find == "t":
      print("\nPlease enter the initial amount of money without the $ sign (EX. 5025.23): ")
      initial = float(input())
      print("\nPlease enter the interest accumulatted (EX. 336.03): ")
      interest = float(input())
      print("\nPlease enter the rate of interest in percentage form without the % sign (EX.9.4): ")
      rate = float(input())
      rate = rate * .01

      simtim(initial,interest,rate)

if sel == "c":
   print(
        """
          What would you like to find? Interest (i), initial amount of money/starting amount of money (s), the 
          rate of interest (r), the time spent investing (t), or the number of times the interest is compounded
          (c)? 
         """
         )
   
   find = input()

   if find == "i":
      print("\nPlease enter the initial amount of money without the $ sign (EX. 5025.23): ")
      initial = float(input())
      print("\nPlease enter the rate of interest in percentage form without the % sign (EX. 9.4): ")
      rate = float(input())
      rate = rate * .01
      print("\nPlease enter the length of investment in years (EX. 0.5): ")
      time = float(input())
      print("\nPlease enter the number of times the interest is compounded per year (EX. 21): ")
      per = input()

      comint(initial,rate,time,per)

   if find == "s":
      print("\nPlease enter the rate of interest in percentage form without the % sign (EX. 9.4): ")
      rate = float(input())
      rate = rate * .01
      print("\nPlease enter the length of investment in years (EX. 0.5): ")
      time = float(input())
      print("\nPlease enter the number of times the interest is compounded per year (EX. 21): ")
      per = input()
      print("\nPlease enter the interest accumulatted (EX. 336.03): ")
      interest = float(input())
