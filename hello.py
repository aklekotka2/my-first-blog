
def hi(name):
	if name=="Agnieszka":
		print('Hej '+name+' !')
		print('How are you?')
	elif name=="Ola":
		print('Hej '+name+' !')
		print('How are you?')
	else:
		print('Hej '+name+' !')

hi("Agnieszka")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Agnieszka']
for name in girls:
	hi(name)

for i in range(1, 7):
    print(i)