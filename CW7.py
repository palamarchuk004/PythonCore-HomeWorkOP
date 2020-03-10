            #Погода.

# import pyowm
# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key
# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place(input('Input citi: '))
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>
# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print('Wind', w.get_wind()["speed"])
# print('Humidity', w.get_humidity())
# print('Temperature', w.get_temperature('celsius')['temp'])
# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)

            #Гра! Відгадай число.

# import random
# x=random.randint(1, 100)
# while True:
#     i=int(input('Введіть число: '))
#     if i == x:
#         print('Гру завершено!')
#         break
#     elif i < x:
#         print('Більше')
#     elif i > x:
#         print('Менше')

            #Площа прямокутника, трикутника та кола.

# import math
# def pr(a,b):
#     print('Площа прямокутника: ', a*b)
#     return
# def tr(c,d,e,p):
    
#     print('Площа трикутника: ',  (math.pow((p*(p-c)*(p-d)*(p-e)), 0.5)
#     ))
#     return
# def cl(r):
#     print('Площа круга: ', (math.pi*math.pow(r, 2)))
#     return
# i=input("Для вибору обчислення площі прямокутника натисніть: 1\nДля вибору обчислення площі трикутника натисніть: 2\nДля вибору обчислення площі кола натисніть: 3\nЗробіть свій вибір:  ")
# if i == '1':
#     a=int(input('Введіть першу сторону прямокутника: '))
#     b=int(input('Введіть другу сторону прямокутника: '))
#     pr(a, b)

# elif i == '2':
#     c=int(input('Введіть першу сторону трикутника: '))
#     d=int(input('Введіть другу сторону трикутника: '))
#     e=int(input('Введіть третю сторону трикутника: '))
#     tr(c, d, e, p=((c+d+e)/2))
# elif i == '3':
#     r=int(input('Введіть радіус круга: '))
#     cl(r)
# else:
#     print('Error')

    



   

