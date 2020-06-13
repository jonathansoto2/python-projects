'''Jonathan Soto MWF 10am CSC 240 1/14/19'''

def easterSundayDate():

    months = ["null", "Jan ", "Feb ", "Mar ", "Apr ", "May " , "Jun ", "Jul ", "Aug ", "Sep ", "Oct ", "Nov ", "Dec " ]
    true = 0
    while true == 0:
        y = str(input("Enter a year and I will return the date of Easter: "))
        
        if y.isnumeric():
            y = int(y)
            if y == 0:
                print("thank you")
                true = 1
                break
            a = y % 19
            b = y // 100
            c = y % 100
            d = b // 4
            e = b % 4
            g = (8 * b + 13) // 25
            h = (19 * a + b - d - g + 15) % 30
            j = c // 4
            k = c % 4
            m = (a + 11 * h) // 319 
            r = (2 * e + 2 * j - k - h + m + 32) % 7
            n = (h - m + r + 90) // 25
            p =  (h - m + r + n + 19) % 32
            p = str(p)
            y = str(y)
            easterDate = str (months[n] + p)
            print(easterDate + ", " + y)
        else:
            print("try again")

        

if __name__ == "__main__":
    print("Press 0 to exit")
    easterSundayDate()
    