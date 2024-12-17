import datetime as dt
def func1(range1,range2):
  
  a = dt.datetime.now()
  b = a.second
  b = int(b)
  final1 = b*9/2-6+9
  if(final1<range1):
    while(final1<range1):
      final1 = final1 * 2
  elif(final1>range2):
    while(final1>range2):
      final1 = final1 /3
      if(final1<range2):
        if(final1<range1):
            while(final1<range1):
              final1 = final1 * 2
          
  print(int(final1))

func1(5,11)






















# while(final1<range1):
# if(final1<range1 or final1>range2):
#   for a in range(1,range2+1):
#     final1 = final1 /2
#     print(final1)
#     if(final1>range1 or final1<range2):
#       print(final1)
#       exit()
