input tele#

find the first index of that string

if first index == (
   check second, third, and fourth index
   if any are not #s then not a valid #

elif first index == #

else not a valid #

##########################

input tele#

find length of string

if length > 14
   not a valid number

if length == 10 or == 7
   then check to see if all numbers
   if all #s
      print valid number
   else
      not a valid number
   break

if length == 12
   check first three indexes
   if all are #s
      if 4th index is dash or period
         check next three indexes
         if all are #s
            if 8th index is dash or period
               check next four indexes
               if all are #s
                  print valid number
               else not a valid number
            else not a valid number
         else not a valid number
      else not a valid number
   else not a valid number

if length == 13
   if first index == (
      if 2,3, and 4th index == #'s
         if 5th index == )
            if 6,7,8 index == #'s
               if 9th index == dash or period
                  if next 4 indexes == #'s
                     print valid number
                  else not a valid number
               else not a valid number
            else not a valid number
         else not a valid number
      else not a valid number
   else not a valid number

if length == 14
   if first index == (
      if 2,3, and 4th index == #'s
         if 5th index == )
            if 6th index == space
               if 7,8,9 index == #'s
                  if 10th index == dash or period
                     if next 4 indexes == #'s
                        print valid number
                     else not a valid number
                  else not a valid number
               else not a valid number
            else not a valid number
         else not a valid number
      else not a valid number
   else not a valid number

if length == 8
   if 1,2,3rd index == #s
      if 4th index == period or dash
         if 5,6,7,8 == #s
            print valid number
         else not a valid number
      else not a valid number
   else not a valid number
