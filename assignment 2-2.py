'''
COMPUTER APPLICATIONS IN CIVIL ENGINEERING CE 257
    Github Link: https://github.com/dkadjei4
    @author: Daniel A. Kusi
'''
car_brand = {
    'Lamborghini':'465,000',
    'Cardillac':'53,000',
    'Porsche':'255,000',
    'Supra':'37,000',
    'Bentley':'110,000',
    'Genysis':'35,000',
    'Nissan':'55,000',
    'Renault':'57,800',
    'Ferrari':'551,000',
    'Bugatti':'100,000'
}           
#Available car brands
car_name=str(input('Please enter a car brand: '))
# get user input for car brand
if car_name in car_brand:
    print('Yes, this brand is available.')
    print('The {0} car brand costs ${1}.'.format(car_name, car_brand[car_name]))
else:
    print('No, this brand is not available.')