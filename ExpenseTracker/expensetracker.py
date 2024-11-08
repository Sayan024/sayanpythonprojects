from datetime import date
import csv

filename = "tracker.csv"
stop = False
dt = date.today()
dt = dt.strftime("%d/%m/%Y")

with open(filename, "a", newline="") as file:
    csv_writer = csv.writer(file)
    while not stop:
        expt = int(input("Enter Expense (Type 0 to stop): "))
        if expt != 0:
            c = int(input("Enter the Category :\n"
                           " Press 1 Housing,\n"
                           " Press 2 Utilities,\n"
                           " Press 3 Groceries,\n"
                           " Press 4 Transportation,\n"
                           " Press 5 Entertainment,\n"
                           " Press 6 Health & Wellness,\n"
                           " Press 7 Miscellaneous. \n"
                           " Enter your choice: "))
            match c:
                case 1:
                    cart = "Housing"
                case 2:
                    cart = "Utilities"
                case 3:
                    cart = "Groceries"
                case 4:
                    cart = "Transportation"
                case 5:
                    cart = "Entertainment"
                case 6:
                    cart = "Health & Wellness"
                case 7:
                    cart = "Miscellaneous"
            p = int(input("Enter the payment type :\n"
                           " Press 1 Cash,\n"
                           " Press 2 UPI,\n"
                           " Press 3 Car,\n"))
            match p:
                case 1:
                    pay = "Cash"
                case 2:
                    pay = "Upi"
                case 3:
                    pay = "Card"

            des = input("Enter description :\n")
            csv_writer.writerow([dt, expt,pay,cart, des])
        else:
            stop = True
