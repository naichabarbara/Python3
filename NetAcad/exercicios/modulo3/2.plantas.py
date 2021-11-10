'''
Escreva um programa que sempre que recebe a palavra 'Spathiphyllum', grita a seguinte string: "Spathiphyllum is the best plant ever!"
'''

plant = input("Name of a plant: ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + plant + " !")
    