def banner_text(text):
    screen_width =int(input("please enter the scrren width in integer: "))
    if len(text) > screen_width - 4:
        #raise valueError("String {0} is larger than specified width {1}".format(text,screen_width))
        print("EKK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text== "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width -4))
        print(output_string)
banner_text("*")
banner_text("Welcome")
banner_text("Hi!, It is inform you that i arranged a event at xyz place")
banner_text("So i requestly invited you to come to this event.")
banner_text("In this even i arranged so many food and drinks.")
banner_text(" ")
banner_text("Thankyou , your dearest......")
banner_text("*")
number = [1,2,3]
print(number.sort())
print(banner_text())