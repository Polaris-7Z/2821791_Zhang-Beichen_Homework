# Write a program that asks you HOW MANY FRIENDS you have and then HOW MANY SWEETS YOU HAVE to share with your friends.
f = int(input("How many friends do you have?"))
s = int(input("How many sweets do you have?"))

print('You should give', s // f , "sweet(s) to each friend and then keep" , s % f , "for yourself.")

quit()
