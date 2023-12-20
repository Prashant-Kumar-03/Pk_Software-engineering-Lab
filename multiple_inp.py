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
 
print("--let's check weather--")
while(True):
    k=input("don't have any or more inputs? press e for exit else press any other key: ")
    if k=='e':
        print("thanks")
        break;
    else:
        T=float(input("enter temperature: "))
        H=float(input("enter humidity: "))
        w=float(input("enter wind speed: "))
        weather(T, H,w)


