zi = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']
venit = [145,167,584,283,829,192,182] 
print(' Venitul saptamanal:', sum(venit))
print(' Media venitului zilnic:', sum(venit)/7)
print(' Ziua cu cel mai mare venit:',zi[venit.index(max(venit))])
print(' Ziua cu cel mai mic venit:',zi[venit.index(min(venit))])