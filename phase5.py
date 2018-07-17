print "Welcome to my fiendish little bomb. You have 6 phases with\nwhich to blow yourself up. Have a nice day!\nPhase 1 defused. How about the next one?\nThat's number 2.Keep going!\nHalfway there!\nSo you got that one.  Try this one.\n"
word1=raw_input()
l=len(word1)
given="isrveawhobpnutfg"
answer="giants"
if(l!=6):
	print "\nBOOM!!!"
	print "The bomb has blown up.\n"
	exit(0)
else:
	word2=[]
	for i in range(0,l):
		word2.append(given[(ord(word1[i])&15)])

	word3=''.join(x for x in word2)
	for i in range(0,l):
		if(word3[i]!=answer[i]):
			print "\nBOOM!!!"
			print "The bomb has blown up.\n"
			exit(0);
	print "Good work!  On to the next...\n"
