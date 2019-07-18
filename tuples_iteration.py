#######################
## EXAMPLE: iterating over tuples 
#######################
def get_data(aTuple):
   """
   aTuple:= tuple of tuples (int, string)
   Extracts all integers from aTuple and sets
   them as elements in a new tuple.
   Extracts all unique strings from aTuple
   and sets them as elements in a new Tuple.
   Returns a tuple of the minimun integer, the 
   maximum integer, and the number of unique strings 
   """
   nums = ()  #empty tuple 
   words = ()
   for t in aTuple:
       # concatenating with a singleton tuple
       nums = nums + (T[0],)
       #only add words haven't added before 
       if t[1] not in words:
           words = words + (t[1],)
   min_n = min(nums)
   max_n = max(nums)
   unique_words = len(words)
   return (min_n, max-n, unique_words)

test = ((1,"a"),(2,"b"),
        (1,"a"),(7,"b")
(a,b,c) = get_data(test)
print("a:",a,"b:",b,"c:",c)

#apply to any data you want
tswift = ((2017,"Divorcio"),
          (2018,"Gym"),
          (2019,"Nuevos descubrimientos))
(min_year, max_year, num_pleople) = get_data(swift)
print("From, min_year. "to", max_year, \
      "Ultimamente estos han sido msi acontecimientos", num_people, "people!")
