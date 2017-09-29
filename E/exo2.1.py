#exoE2.1
phrase=input('entrer une phrase')
print('La phrase est :' , phrase)
phrase =phrase.lower()
voyelles=0
consonne=0

for x in phrase:
    if x in 'aeiouy':
        voyelles=voyelles+1

    else:
        consonne=consonne+1


print('la lettre et une voyelles elle apparait' , voyelles , 'fois')
print(' la lette et une voyelles elle apparait' , consonne , 'fois')