cheat = "UGxheWVyTGV2ZWw9OTk5OTk5OTk5O1BsYXllckV4cD05OTk5OTk5OTk5O1BsYXllckhQPTk4NzY1NDMyMTtQbGF5ZXJBdGs9OTg3NjU0MzIxO1BsYXllckRlZj05ODc2NTQzMjE7UGxheWVyTmFtZT1Cb2Rv"
alphabet = "abcdefghijklmnopqrstuvwxyz"
newcheat = ""
for i in cheat:
	if i in alphabet.upper():
		newcheat += i.lower()
	elif i in alphabet.lower():
		newcheat += i.upper()
	else:
		newcheat += i

print newcheat
