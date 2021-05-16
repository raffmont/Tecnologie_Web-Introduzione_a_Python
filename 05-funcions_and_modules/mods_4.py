from codicefiscale import codicefiscale

person={
	"surname":'Montella',
	"name":'Raffaele',
	"sex":'M',
	"birthdate":'10/05/1972',
	"birthplace":'Napoli'
}

result = codicefiscale.encode(
	surname=person["surname"],
	name=person["name"],
	sex=person["sex"],
	birthdate=person["birthdate"],
	birthplace=person["birthplace"])

print(result)

