import random
l=['r','p','s']
d={'r':'rock','p':'paper','s':'scissor'}
us=0
cs=0
while True:

	i=input("enter ur choice")
	if i=='q':
		print("game is oveer")
		print("comp score and user score",cs,us)
		if us>cs:
			print("user win")
		if cs>us:
			print("comp won")
		if cs==us:
			print("tie")
	c=random.choice(l)
	print("comp",d[c],"user",d[i])

	if i==c:
		print("tie")
	elif i=='r' and c=='s':
		print("user wins")
		us=us+1
	elif i=='p' and c=='r':
		print("user has won")
		us=us+1
	elif i=='s' and c=='p':
		print("user wins")
	else:
		print("comp wins")


    
