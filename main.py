friends = int(input("How many friends do you have"))
chocolate = int(input("how many chocolates you have to give to your friends? "))
share = chocolate//friends
remainder = chocolate%friends

print("you should share",share,"chocolates to your friends" )
print("you will be left over with", remainder)
quit()



