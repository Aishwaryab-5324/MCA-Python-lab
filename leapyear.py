from datetime import datetime

current_year=datetime.now().year
end_year=int(input("enter the final year:"))

print("leap years:")
for year in range(current_year,end_year+1):
    if(year%4==0 and year%100!=0)or(year%400==0):
        print(year,end=" ")
