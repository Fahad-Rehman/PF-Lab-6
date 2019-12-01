def fee_voucher():
    Dict1 = {'Name':'Fahad',
            'Roll No':'19B-008-SE',
             'Section':'A',
            'Semester':'First',
            'Semester Fees':98000,
            'Misc Fees':5000}
    Dict2 = {'Name':'Daniyal',
            'Roll No':'19B-037-SE',
             'Section':'A',
            'Semester':'First',
            'Semester Fees':98000,
            'Misc Fees':5000}
    Dict3 = {'Name':'Abdullah',
            'Roll No':'19B-089-SE',
             'Section':'A',
            'Semester':'First',
            'Semester Fees':98000,
            'Misc Fees':5000}
    total_fees = Dict1.get('Semester Fees') + Dict1.get('Misc Fees')
    print('\nLogo\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogo\t\t\t\t\t\t\t\t\t\t\t\tLogo\n\n\t\t\tUsman Institute Of Technology\t\t\t\t\t\t\t\t\t\tUsman Institute Of Technology\t\t\t\t\t\tUsman Institute Of Technology\nBank Copy\t\t\t Fee Voucher\t\t\t\t\t\t\t\t\tUniversity Copy\t\tFee Voucher\t\t\t\t\t\tStudent Copy\t\tFee Voucher\n')
    print('Name:\t  {0}\t\t\t\tSemester Fees: {4}\t\t\t\t\tName:\t   {0}\t\tSemester Fees: {4}\t\tName:\t  {0}\t\t\tSemester Fees:\t{4}\nRoll No:  {1}\t\tMisc Fees:\t\t{5}\t\t\t\t\tRoll No:   {1}\tMisc Fees:\t\t{5}\t\tRoll No:  {1}\tMisc Fees:\t\t {5}\nSection:  {2}\t\t\t\t\tTotal Fees:\t  {6}\t\t\t\t\tSection:   {2}\t\t\tTotal Fees:\t  {6}\t\tSection:  {2}\t\t\t\tTotal Fees:\t   {6}\nSemester: {3}\t\t\t\t\t\t\t\t\t\t\t\t\t\tSemester:  {3}\t\t\t\t\t\t\t\t\tSemester: {3}'.format(Dict1.get('Name'),Dict1.get('Roll No'),Dict1.get('Section'),Dict1.get('Semester'),Dict1.get('Semester Fees'),Dict1.get('Misc Fees'), total_fees))
    print('\n\n')
    print('\nLogo\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogo\t\t\t\t\t\t\t\t\t\t\t\tLogo\n\n\t\t\tUsman Institute Of Technology\t\t\t\t\t\t\t\t\t\tUsman Institute Of Technology\t\t\t\t\t\tUsman Institute Of Technology\nBank Copy\t\t\t Fee Voucher\t\t\t\t\t\t\t\t\tUniversity Copy\t\tFee Voucher\t\t\t\t\t\tStudent Copy\t\tFee Voucher\n')
    print('Name:\t  {0}\t\t\tSemester Fees: {4}\t\t\t\t\tName:\t   {0}\t\tSemester Fees: {4}\t\tName:\t  {0}\t\tSemester Fees:\t{4}\nRoll No:  {1}\t\tMisc Fees:\t\t{5}\t\t\t\t\tRoll No:   {1}\tMisc Fees:\t\t{5}\t\tRoll No:  {1}\tMisc Fees:\t\t {5}\nSection:  {2}\t\t\t\t\tTotal Fees:\t  {6}\t\t\t\t\tSection:   {2}\t\t\tTotal Fees:\t  {6}\t\tSection:  {2}\t\t\t\tTotal Fees:\t   {6}\nSemester: {3}\t\t\t\t\t\t\t\t\t\t\t\t\t\tSemester:  {3}\t\t\t\t\t\t\t\t\tSemester: {3}'.format(Dict2.get('Name'), Dict2.get('Roll No'), Dict2.get('Section'), Dict2.get('Semester'),Dict2.get('Semester Fees'), Dict2.get('Misc Fees'), total_fees))
    print('\n\n')
    print('\nLogo\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogo\t\t\t\t\t\t\t\t\t\t\t\tLogo\n\n\t\t\tUsman Institute Of Technology\t\t\t\t\t\t\t\t\t\tUsman Institute Of Technology\t\t\t\t\t\tUsman Institute Of Technology\nBank Copy\t\t\t Fee Voucher\t\t\t\t\t\t\t\t\tUniversity Copy\t\tFee Voucher\t\t\t\t\t\tStudent Copy\t\tFee Voucher\n')
    print('Name:\t  {0}\t\t\tSemester Fees: {4}\t\t\t\t\tName:\t   {0}\t\tSemester Fees: {4}\t\tName:\t  {0}\t\tSemester Fees:\t{4}\nRoll No:  {1}\t\tMisc Fees:\t\t{5}\t\t\t\t\tRoll No:   {1}\tMisc Fees:\t\t{5}\t\tRoll No:  {1}\tMisc Fees:\t\t {5}\nSection:  {2}\t\t\t\t\tTotal Fees:\t  {6}\t\t\t\t\tSection:   {2}\t\t\tTotal Fees:\t  {6}\t\tSection:  {2}\t\t\t\tTotal Fees:\t   {6}\nSemester: {3}\t\t\t\t\t\t\t\t\t\t\t\t\t\tSemester:  {3}\t\t\t\t\t\t\t\t\tSemester: {3}'.format(Dict3.get('Name'), Dict3.get('Roll No'), Dict3.get('Section'), Dict3.get('Semester'),Dict3.get('Semester Fees'), Dict3.get('Misc Fees'), total_fees))

fee_voucher()