def get_vat(payment):
	try:
		payment = float(payment)
		vat = payment / 100 * 18
		return round(vat, 2)
	except (TypeError, ValueError, TabError):
		return 'облом' 


result = get_vat('ololo')
print('Сумма ндс: {}'.format(result))