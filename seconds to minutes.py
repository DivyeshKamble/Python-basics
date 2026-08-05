#Program that reads a number of seconds and print it in mins and seconds
ts = int(input("Enter the time in seconds : "))
tm = (ts//60)
t_s = (ts%60)
print (tm , "mins and" , t_s , "secs")