min_salary = 30000.00
min_years = 2
salary = float(input('Enter your annual salary:'))
years_on_job = int(input('Enter number of years' + 'years employed'))
If salary >= min_salary:
    If years_on_job >= min_years
        print('You qualify for the loan.')
    else:
        print('You must have been employed', 'for at least', min_years, 'years to qualify')
else:
    print('You must earnat least $', format(min_salary, ',.2f')' per year to qualify.', sep='')