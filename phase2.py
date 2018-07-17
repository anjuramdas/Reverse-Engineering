print "Welcome to my fiendish little bomb. You have 6 phases with\nwhich to blow yourself up. Have a nice day!\nPhase 1 defused. How about the next one?"
word=raw_input()
l=map(int,word.split())
if(len(l)!=6):
	print "\nBOOM!!!"
	print "The bomb has blown up.\n"
	exit()
if(l[0]!=1):
	print "\nBOOM!!!"
	print "The bomb has blown up.\n"
	exit()
for i in range(1,6):
	j=i+1
	j=j*l[i-1]
	if(l[i]!=j):
		print "\nBOOM!!!"
		print "The bomb has blown up.\n"
		exit()
print "That's number 2.  Keep going!"


