india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input('please enter first city name').lower()
city2 = input('please enter second city name').lower()
if city1 in india and city2 in india:
    print('Both cities in India')
elif city2 in pakistan and city2 in pakistan:
    print('Your city is in paskistan')
elif city1 in bangladesh and city2 in bangladesh:
    print('Your city in bangladesh')
else:
    print('They dont belong to the same country')


sg = int(input('enter you sugar level'))
if sg > 100:
    print('High')
elif sg < 80:
    print('low')
else:
    print('normal')


