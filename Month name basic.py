monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in monthname:
    if len(month) > 7:
        print(f"{month} has more than 7 characters.")
    elif len(month) == 7:
        print(f"{month} has exactly 7 characters.")