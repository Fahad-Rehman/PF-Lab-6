#Question No: 7
import time
def POS():
    name = str('Muhammad Umer')
    date = time.strftime('%d/11/%Y')
    burger_type = str('Burger type:\tDouble Cheese Burger')
    quantity1 = str('Quantity\t    ')
    quantity2 = 2
    rate1 = str('Rate\t\t\t')
    rate2 = 150
    sum = (rate2 * quantity2)
    GST = str('GST\t\t\t\t')
    GST1 = (sum / 100) * 13
    amount1 = str('Amount\t\t\t')
    amount2 = sum + GST1
    cash = str('Cash Recieved\t')
    cash1 = 500
    total_sum1 = str('Cash to Return\t')
    total_sum2 = (cash1 - (amount2 + GST1))
    print('{0}\n{1}\n\n{2}\n{3}{4}\n{5}{6}\n{7}{8}\n{9}{10}\n{11}{12}\n{13}{14}'.format(name, date, burger_type, quantity1, quantity2, rate1, rate2, GST, GST1, amount1, amount2, cash, cash1, total_sum1, total_sum2))
    print('\nThank You For Choosing Us!')
POS()
