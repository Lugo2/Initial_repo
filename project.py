city_list=['Tijuana','Lima','Amsterdam','Cairo','Bangkok','Wagga Wagga']
Tijuana_eats=['Sabor a Mi','Tacos el Gordo','Villa Marina Tijuana','Da Salvatore','Saketori-Ya']
Tijuana_transportation=['taxi','bus','car rental','bicycle']
Tijuana_entertainment=['','','','','']

Lima_eats=['','','','','']
Lima_transportation=['','','','']
Lima_entertainment=['','','','','']

Amsterdam_eats=['','','','','']
Amsterdam_transportation=['bicycle','','','']
Amsterdam_entertainment=['','','','','']

Cairo_eats=['','','','','']
Cairo_transportation=['','','','']
Cairo_entertainment=['','','','','']

Bangkok_eats=['','','','','']
Bangkok_transportation=['','','','']
Bangkok_entertainment=['','','','','']

Wagga_Wagga_eats=['','','','','']
Wagga_Wagga_transportation=['','','','']
Wagga_Wagga_entertainment=['','','','','']

print('Hello, I am your firendly neighborhood day trip generator! Today we will be planning your next day trip. Lets go!')
import random

destination=random.choice(city_list)
input(f'I have chosen {destination} for you, is this where you would like to go? y/n')

answer=input
def find_out(answer): #get the parameter to be defined by user imput
    answer='y'or'n'
    for answer in input:

        if answer=='n':
            destination=random.choice(city_list)
            input(f'Sorry to see that, would {destination} work? y/n')

        elif answer=='y':
            return destination
        print(f'Awesome, we have determined you want to go to {destination}.')

user_answer=find_out(input)