def func(n):
	if(n<=1):
		return 1
	else:
		return func(n-1)+func(n-2)	


print "Welcome to my fiendish little bomb. You have 6 phases with\nwhich to blow yourself up. Have a nice day!\nPhase 1 defused. How about the next one?\nThat's number 2.Keep going!\nHalfway there!\n"
l=[]
l=raw_input().split()	
if(len(l)==1):
	if(l[0].isdigit()==True):
		res=func(int(l[0]))
		if(res==55):
			print "So you got that one.  Try this one." 
		else:
			print "\nBOOM!!!"
			print "The bomb has blown up.\n"
	


	else:
		print "\nBOOM!!!"
		print "The bomb has blown up.\n"

else:
	print "\nBOOM!!!"
	print "The bomb has blown up.\n"			
