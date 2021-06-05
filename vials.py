weight = input('Weight in Lbs: ')
mgkg = input('Infliximab Dose: ')
dose = ((float(weight) / 2.2) * float(mgkg)) / 100
print('Vials:', dose)
if dose > 10.5:
	print('Use 500cc bag of NS')
else:
	print('Use 250cc bag of NS')
inf =  input('How many prior infusions has the pt had? ')
if float(inf) > 4:
	infnum = input('How much NS is being used? ')
	if float(infnum) == 250:
		print('Accelerated Rate')
	else:
		print('Extended Rate')
else:
	print('Beginner Rate')