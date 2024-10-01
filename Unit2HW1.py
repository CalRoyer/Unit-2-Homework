'''
Cal Royer
10/1/24
Unit 2 Homework 1
'''
print('Problem 1'.center(20,'-'))
print('The Hidden Treasure Map')
print('The Magic Classroom')
print('The Food Search')

print('problem 2'.center(20,'-'))
print("""                                                                                                                                                          
 ,-----.,--.                                     ,--.   ,--.                         ,-----.,--.                                    ,--.                 
'  .--./|  ,---.  ,---.  ,---.  ,---.  ,---.      \  `.'  /,---. ,--.,--.,--.--.    '  .--./|  ,---.  ,--,--.,--.--. ,--,--. ,---.,-'  '-. ,---. ,--.--. 
|  |    |  .-.  || .-. || .-. |(  .-' | .-. :      '.    /| .-. ||  ||  ||  .--'    |  |    |  .-.  |' ,-.  ||  .--'' ,-.  || .--''-.  .-'| .-. :|  .--' 
'  '--'\|  | |  |' '-' '' '-' '.-'  `)\   --.        |  | ' '-' ''  ''  '|  |       '  '--'\|  | |  |\ '-'  ||  |   \ '-'  |\ `--.  |  |  \   --.|  |    
 `-----'`--' `--' `---'  `---' `----'  `----'        `--'  `---'  `----' `--'        `-----'`--' `--' `--`--'`--'    `--`--' `---'  `--'   `----'`--'    
                                                                                                                                                         """)

print('Problem 3'.center(20,'-'))
distance = 173.8
miles_per_gallon = int(input("How many miles per gallon does your car get? "))
price_of_gallon = float(input("How much does a gallon of gas cost near your house? "))
gas_capacity = int(input("How many gallons of gas does your car hold? "))
gas_filled = float(input("What fraction of your tank did you fill up? (example: 0.5 for half, 1 for full) "))
gas_needed = distance/miles_per_gallon
cost_of_trip = (gas_needed * price_of_gallon) * gas_filled
print(f"The cost to drive from Portland to Seattle is approximately ${cost_of_trip}")
