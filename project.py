city_list=['Tijuana','Lima','Amsterdam','Cairo','Bangkok','Melbourne']
Tijuana_eats=['Tacos el Gordo','Villa Marina Tijuana','Da Salvatore','Saketori-Ya']
Tijuana_transportation=['taxi','bus','car rental','bicycle']
Tijuana_entertainment=['Centro Cultural Tijuana','Mamut Cerveceria','Cinepolis','Malecon']

Lima_eats=['La Bodega de la Trattoria','Pizza Raul','Polleria Rokys','Chifa Oriental']
Lima_transportation=['metro','car rental','taxi','on foot']
Lima_entertainment=['Plaza Mayor','Lacro Museum','Morro Solar','Lima Golf Club']

Amsterdam_eats=['Sea Palace','Vapiano','The Lobby','Mr Porter']
Amsterdam_transportation=['by foot','bicycle rental','tram','ferrie']
Amsterdam_entertainment=['Canal Cruise','Madame Tussauds Museum','Melkweg','Red Light District']

Cairo_eats=['7agoga','Hamada Sheraton','Burger Factory','Tivoli Plaza']
Cairo_transportation=['metro','taxi','bus','on foot']
Cairo_entertainment=['Cairo Citadel','The Egyptian Museum','Cairo Tower','Nile River Cruise']

Bangkok_eats=['Sen','Yada Cafe','Choongman Chicken','Thai food keto']
Bangkok_transportation=['Skytrain','taxi','bus','by foot']
Bangkok_entertainment=['Siam Park','Art and Culture Centre','The Grand Palace','Safari World']

Melbourne_eats=['Chin Chin','True South','Oscars Hangout','Siam Spicy']
Melbourne_transportation=['tram','bus','taxi','car rental']
Melbourne_entertainment=['Forum Melbourne','Flemington Racecourse','Queen Victoria Market','ACMI']

def program_introduction():
    print('Hello! I am your friendly neighborhood Day Trip Generator, I will be helping you plan your coming trip. Lets go!')
program_introduction()
import random

def random_city_chooser(destination):
    destination=random.choice(city_list)
    return destination

random_city=random_city_chooser(city_list)


def prompt_user_location():
    answer=input(f'For starters, I have selected: {random_city}, for your destination. Is this where you would like to go?y/n')
    return answer

user_input=prompt_user_location()


def new_city_randomizer(new_city):
    if user_input == 'n':
        new_city=random.choice(city_list)
        return new_city
    elif user_input=='y':
        print(f'Sweet! This day trip location will be: {new_city}.')

new_city=new_city_randomizer('n'or'y')


def prompt_user_location():
    new_answer=input(f'Sorry to see that, your next possible location I have selected: {new_city}. Is this where you would like to go?y/n')
    return new_answer

new_answer=prompt_user_location()

