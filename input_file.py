def weather(T, H, w):
    W = 0.5 * (T ** 2) - 0.2 * H + 0.1 * w - 15
    if W > 300:
        print("weather is SUNNY")
    elif 200 < W <= 300:
        print("weather is CLOUDY")
    elif 100 < W <= 200:
        print("weather is RAINY")
    else:
        print("weather is STORMY")

# Open the file in read mode
file_path = "D:\OneDrive\Desktop\Pk_project\input\inp.txt"  # Replace with the actual path to your file
with open(file_path, 'r') as file:
    # Read the values from the file
    lines = file.readlines()

# Extract temperature, humidity, and wind speed from the lines
T = float(lines[0].strip())
H = float(lines[1].strip())
w = float(lines[2].strip())

# Call the weather function with the read values
weather(T, H, w)
