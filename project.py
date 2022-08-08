city_list=['Tijuana','Lima','Amsterdam','Cairo','Bangkok','Wagga Wagga']
Tijuana_eats=['Tacos el Gordo','Villa Marina Tijuana','Da Salvatore','Saketori-Ya']
Tijuana_transportation=['taxi','bus','car rental','bicycle']
Tijuana_entertainment=['Centro Cultural Tijuana','Mamut Cerveceria','Cinepolis','Malecon']

Lima_eats=['La Bodega de la Trattoria','Pizza Raul','Polleria Rokys','Chifa Oriental']
Lima_transportation=['metro','car rental','taxi','on foot']
Lima_entertainment=['Plaza Mayor','Lacro Museum','Morro Solar','Lima Golf Club']

Amsterdam_eats=['','','','']
Amsterdam_transportation=['','','','']
Amsterdam_entertainment=['','','','']

Cairo_eats=['','','','']
Cairo_transportation=['','','','']
Cairo_entertainment=['','','','']

Bangkok_eats=['','','','']
Bangkok_transportation=['','','','']
Bangkok_entertainment=['','','','']

Wagga_Wagga_eats=['','','','']
Wagga_Wagga_transportation=['','','','']
Wagga_Wagga_entertainment=['','','','']

# def program_intoduction():
#     print('Hello, I am your firendly neighborhood day trip generator! Today we will be planning your next day trip. Lets go!')
# program_intoduction()

import random

def random_city_chooser(destination):
    destination=random.choice(city_list)
    return destination

random_city=random_city_chooser(city_list)

def prompt_user_location():
    answer=input(f'We have selected: {random_city}. Is this where you would like to go?y/n')
    return answer

user_input=prompt_user_location()
print(user_input)


# answer=input(f'I have chosen {destination} for you, is this where you would like to go? y/n')



# def new_city_chooser(no):#parameter will be user saying no to input prompt
#     new_destination=random.choice(city_list)#trying to 
#     return new_destination





