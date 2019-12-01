#Question No: 4
def mailaddress ():
    first = str('Syed Faisal')
    last = str('Ali')
    designation = str('Asst. Prof.')
    department = str('Deparment of Computer Science')
    workplace = str('Usman Institute of Technology')
    address = str('Gulshan e Iqbal')
    zip_code = 75300
    city = str('Karachi')
    print('{0} {1}\n{2}\n{3}\n{4}\n{5}, {6}\n{7},'.format(first, last, designation, department, workplace, address, zip_code, city))
mailaddress()