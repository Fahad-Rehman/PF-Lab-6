#Question No: 2
def Forecast():
    forecast = str('It will be a sunny day today')
    print(forecast)
    count = forecast.count('day')
    print(count)
    weather = forecast.find('sunny')
    print(weather)
    change = forecast.replace('sunny', 'cloudy')
    print(change)
Forecast()