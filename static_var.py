def weather(T,H,w):
    W=0.5*(T**2)-0.2*H+0.1*w-15 
    if W>300:
        print("weather is SUNNY")
    elif 200<W<=300:
        print("weather is CLOUDY")
    elif 100<W<=200:
        print("weather is RAINY")
    else :
        print("weather is STORMY")
 

#T=float(input("enter temperature: "))
#H=float(input("enter humidity: "))
#w=float(input("enter wind speed: "))
print("\n\ntest case 1:")
weather(25,70,15)
print("\n\ntest case 2:")
weather(30,60,10)
print("\n\ntest case 3:")
weather(20,80,5)
print("\n\ntest case 4:")
weather(15,90,25)