'''Jonathan Soto MWF 10am CSC240
5 days of temperatures and 4 temperature readings for the day 
2 morning - 2 night
User will enter the start day 1 = sunday, 2 = monday, ...
User will enter the temperatures


day tempss
morning averag
afternoon average
daily average

highest temp of the 5 days
lowest temp of the 5 days
highest daily average 
lowest daiy average

 '''

def play():
        days = get_user_day()

        temps = get_user_temps()

        morning_average = get_morning_average(temps)

        print_days_temps(days, temps, morning_average)

def get_user_day():
        #get a start day
        day_table = ["","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        user_start_day = int(input("Enter the day of the week in numeric form(i.e. 1 for Sunday, 2 for Monday): "))

        if user_start_day > 7 or user_start_day < 1:
                return get_user_day()
# if user_start_day is wednesday  
        elif user_start_day == 4 :
                return [day_table[user_start_day], day_table[5],day_table[6] ,day_table[7] ,day_table[1]]
#if user start day is thursday
        elif user_start_day == 5:
                return [day_table[user_start_day], day_table[6],day_table[7] ,day_table[1] ,day_table[2]]
#if user start day is Friday
        elif user_start_day == 6 :
                return [day_table[6], day_table[7], day_table[1] ,day_table[2] ,day_table[3]]
#if user start day is Saturday
        elif user_start_day == 7 :
                return [day_table[7], day_table[1],day_table[2] ,day_table[3] ,day_table[4]]
        
        return [day_table[user_start_day], day_table[user_start_day + 1], day_table[user_start_day +2],
                day_table[user_start_day + 3], day_table[user_start_day + 4]]
                


def get_user_temps():
        all_temps = []

        #gets the user input and puts it into the day_table array
        k = 0
        for _ in range(5):
                tempList = []
        
                while len(tempList) < 4:
                        user_temp = int(input("enter your 4 temps here: "))
                        if user_temp < -50:
                                print("try again pls ")
                        tempList.append(user_temp)

                all_temps.append(tempList)
        
                k += 1
                if k < 5:
                        print("Enter the following day's temp")
        return all_temps

def get_morning_average(temps):

        morning_averages = temps[0][0] + temps[0][1]
        return morning_averages
        


def print_days_temps(days, temps, morning_average):
        print(str.format("Today is {}. The 4 temps are {} {} {} {}. \n{} temps are {} {} {} {}. \n{} temps are {} {} {} {}. \n{} temps are {} {} {} {}. \n{} the temps are {} {} {} {}. first morning avg {}" , 
                days[0], temps[0][0], temps[0][1], temps[0][2], temps[0][3], days[1], temps[1][0], temps[1][1], temps[1][2], temps[1][3], days[2] , temps[2][0], temps[2][1], temps[2][2], temps[2][3], days[3], temps[3][0], temps[3][1], temps[3][2], temps[3][3], days[4], temps[4][0], temps[4][1], temps[4][2], temps[4][3], morning_average ))


if __name__ == "__main__":
        
        play()