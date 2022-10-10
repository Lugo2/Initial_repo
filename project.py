import random
city_list=['Tijuana','Lima','Amsterdam','Cairo','Bangkok','Melbourne']
eats_list = ['Tacos el Gordo', 'Bodega de Trattoria','Vapiano', 'Hamada Sheraton', 'Sen', 'Chin Chin']
transportation_list = ['taxi', 'metro', 'bicycle rental', 'on foot', 'Skytrain', 'tram']
entertainment_list=['Mamut cerveceria', 'Lacro Museum', 'Canal Cruise', 'Cairo Citadel', 'Siam Park', 'Flemington Racecourse']
# Tijuana_eats=['Tacos el Gordo','Villa Marina Tijuana','Da Salvatore','Saketori-Ya']
# Tijuana_transportation=['taxi','bus','car rental','bicycle']
# Tijuana_entertainment=['Centro Cultural Tijuana','Mamut Cerveceria','Cinepolis','Malecon']

# Lima_eats=['La Bodega de la Trattoria','Pizza Raul','Polleria Rokys','Chifa Oriental']
# Lima_transportation=['metro','car rental','taxi','on foot']
# Lima_entertainment=['Plaza Mayor','Lacro Museum','Morro Solar','Lima Golf Club']

# Amsterdam_eats=['Sea Palace','Vapiano','The Lobby','Mr Porter']
# Amsterdam_transportation=['by foot','bicycle rental','tram','ferrie']
# Amsterdam_entertainment=['Canal Cruise','Madame Tussauds Museum','Melkweg','Red Light District']

# Cairo_eats=['7agoga','Hamada Sheraton','Burger Factory','Tivoli Plaza']
# Cairo_transportation=['metro','taxi','bus','on foot']
# Cairo_entertainment=['Cairo Citadel','The Egyptian Museum','Cairo Tower','Nile River Cruise']

# Bangkok_eats=['Sen','Yada Cafe','Choongman Chicken','Thai food keto']
# Bangkok_transportation=['Skytrain','taxi','bus','by foot']
# Bangkok_entertainment=['Siam Park','Art and Culture Centre','The Grand Palace','Safari World']

# Melbourne_eats=['Chin Chin','True South','Oscars Hangout','Siam Spicy']
# Melbourne_transportation=['tram','bus','taxi','car rental']
# Melbourne_entertainment=['Forum Melbourne','Flemington Racecourse','Queen Victoria Market','ACMI']

def program_introduction():
    print('Hello! I am your friendly neighborhood Day Trip Generator, I will be helping you plan your coming trip. Lets go!')


def random_city_chooser():
    destination=random.choice(city_list)
    return destination

def random_eats_chooser():
    destination=random.choice(eats_list)
    return destination

def random_transportation_chooser():
    transport=random.choice(transportation_list)
    return transport

def random_entertainment_chooser():
    entertainment=random.choice(entertainment_list)
    return entertainment


def city_rerandomizer():
    random_city = random_city_chooser()
    user_input = input(f'For starters, I have selected: {random_city}, for your destination. Is this where you would like to go?y/n')
    while user_input == 'n' or 'y':
        if user_input == 'n':
            random_city = random_city_chooser()
            user_input = input(f'Sorry to see that, your next possible location I have selected: {random_city}. Is this where you would like to go?y/n')
        else:
            print(f'Sweet! This day trip location will be: {random_city}.')
            return random_city

def eats_rerandomizer():
    random_eats = random_eats_chooser()
    user_input = input(f'Great! Now onto choosing grub, I have selected: {random_eats} as your restaurant. Is this where you would like to go?y/n')
    while user_input == 'n' or 'y':
        if user_input == 'n':
            random_eats = random_eats_chooser()
            user_input = input(f'Sorry to see that, your next possible restaurant I have selected: {random_eats}. Is this where you would like to go?y/n')
        else:
            print(f'Perfect! This day trip restaurant location will be: {random_eats}.')
            return random_eats  

def transportation_rerandomizer():
    random_transportation = random_transportation_chooser()
    user_input = input(f'Great! Now lets choose mode of transportation, I have selected: {random_transportation} as your mode. Is this what you would like?y/n')

    while user_input == 'n' or 'y':
        if user_input == 'n':
            random_transportation = random_transportation_chooser()
            user_input = input(f'Sorry to see that, your next possible transportation I have selected: {random_transportation}. Is this what you would like?y/n')
        else:
            print(f'Perfect! This day trip transportation mode will be: {random_transportation}.')
            return random_transportation
             
def entertainment_rerandomizer():
    random_entertainment = random_entertainment_chooser()
    user_input = input(f'Great! Now lets choose type of entertainment, I have selected: {random_entertainment} as your entertainment. Is this what you would like?y/n')
    while user_input == 'n' or 'y':
        if user_input == 'n':
            random_entertainment = random_entertainment_chooser()
            user_input = input(f'Sorry to see that, your next possible entertainment type I have selected: {random_entertainment}. Is this what you would like?y/n')
        else:
            print(f'Perfect! This day trip entertainment type will be: {random_entertainment}.')
            return random_entertainment


def day_trip_generator():
    program_introduction()
    city = city_rerandomizer()
    eats = eats_rerandomizer()
    transportation = transportation_rerandomizer()
    entertainment = entertainment_rerandomizer()
    print(f'I have selected a randomized day trip for you!')
    print(f'Destination: {city}')
    print(f'Restaurant: {eats}')
    print(f'Transportation: {transportation}')
    print(f'Entertainment: {entertainment}')
    trip = input('Do you like this trip? Please enter complete/incomplete.')
    while trip == 'incomplete' or 'complete':
        if trip == 'incomplete':
            change = input(f'My fault, we can fix that. What would you like to change? Destination? Restaurant? Transportation? Or entertainment? Please enter D/R/T/E ')
            if change == 'D':
                city = city_rerandomizer()
                print(f'Awesome! looks like you liked your trip. Here are the details, you will be going to {city}, eating from {eats}, moving around the city on {transportation}, finally with a fun activity to entertain yourself: {entertainment}.')
                trip = input('Do you like this change? Please enter complete/incomplete.')
            elif change == 'R':
                eats = eats_rerandomizer()
                print(f'Awesome! looks like you liked your trip. Here are the details, you will be going to {city}, eating from {eats}, moving around the city on {transportation}, finally with a fun activity to entertain yourself: {entertainment}.')
                trip = input('Do you like this change? Please enter complete/incomplete.')
            elif change == 'T':
                transportation = transportation_rerandomizer()
                print(f'Awesome! looks like you liked your trip. Here are the details, you will be going to {city}, eating from {eats}, moving around the city on {transportation}, finally with a fun activity to entertain yourself: {entertainment}.')
                trip = input('Do you like this change? Please enter complete/incomplete.')
            elif change == 'E':
                entertainment = entertainment_rerandomizer()
                print(f'Awesome! looks like you liked your trip. Here are the details, you will be going to {city}, eating from {eats}, moving around the city on {transportation}, finally with a fun activity to entertain yourself: {entertainment}.')
                trip = input('Do you like this change? Please enter complete/incomplete.')
        else:
            print(f'Awesome! looks like you liked your trip. Here are the details, you will be going to {city}, eating from {eats}, moving around the city on {transportation}, finally with a fun activity to entertain yourself: {entertainment}.')
            print('I hope you enjoy your trip as much as I did helping you choose it. Happy travels!')
            break
day_trip_generator()