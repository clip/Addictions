#Addictions Dopamine Hackathon
#CNTRL + C to break LOOP in terminal
# PUT FUNCTIONS AT TOP FIRST
import random
import time

# Food Addiction Simulation
def food(): #Starts the food addiction game.
    day = 1
    budget = 500
    total_calories = 0 #variables for a counter that works with while true.

    healthy_items = [item.lower() for item in ['Salad', 'Fruit', 'Grilled Chicken', 'Quinoa', 'Veggies']]
    unhealthy_items = [item.lower() for item in ['Pizza', 'Burger', 'Soda', 'Fried Chicken', 'Candy']] #for loop to go through and loop all the items to be shortened.

    while True: #repeated day night cycle.
        print(f"Day {day}...")
        time.sleep(3)
        print(f"It's morning! Time for breakfast. \nYour balance is ${budget}.")
        time.sleep(5)

        # Breakfast options
        healthy_choice_breakfast = random.choice(healthy_items)
        unhealthy_choice_breakfast = random.choice(unhealthy_items)

        cost = random.randint(8, 20)  # Healthy food cost
        cost2 = random.randint(2, 10)  # Unhealthy food cost

        while True:  # Make sure User Choice is valid.
            print(f"Choose between ${cost} {healthy_choice_breakfast} and ${cost2} {unhealthy_choice_breakfast}.")
            user_choice = input('What are you craving? ').lower()

            if user_choice == healthy_choice_breakfast:
                calories = random.randint(50, 200)
                print(f"You chose {healthy_choice_breakfast}.")
                total_calories += calories
                budget -= cost
                print(f'You lost ${cost}. Total balance: ${budget}.')
                break
            elif user_choice == unhealthy_choice_breakfast:
                calories = random.randint(600, 1200)
                print(f"You chose {unhealthy_choice_breakfast}.")
                total_calories += calories
                budget -= cost2
                print(f'You lost ${cost2}. Total balance: ${budget}.')
                break
            else:
                print("Invalid choice! Choose between the items listed.")

        time.sleep(3)
        print('The morning is passing by... Noon is approaching! It\'s time for lunch soon!')
        time.sleep(3)

        # Lunch options
        healthy_choice_lunch = random.choice(healthy_items)
        unhealthy_choice_lunch = random.choice(unhealthy_items)

        cost = random.randint(8, 20)  # Healthy food cost
        cost2 = random.randint(2, 10)  # Unhealthy food cost

        while True:  # Validate choice
            print(f"Choose between ${cost} {healthy_choice_lunch} and ${cost2} {unhealthy_choice_lunch}.")
            user_choice = input('What are you craving? ').lower()

            if user_choice == healthy_choice_lunch:
                calories = random.randint(50, 200)
                print(f"You chose {healthy_choice_lunch}.")
                total_calories += calories
                budget -= cost
                print(f'You lost ${cost}. Total balance: ${budget}.')
                break
            elif user_choice == unhealthy_choice_lunch:
                calories = random.randint(600, 1200)
                print(f"You chose {unhealthy_choice_lunch}.")
                total_calories += calories
                budget -= cost2
                print(f'You lost ${cost2}. Total balance: ${budget}.')
                break
            else:
                print("Invalid choice! Choose between the items listed.")

        time.sleep(3)
        print('Noon has passed. Evening is approaching. Dinner is here!')
        time.sleep(5)

        # Dinner options
        healthy_choice_dinner = random.choice(healthy_items)
        unhealthy_choice_dinner = random.choice(unhealthy_items)

        cost = random.randint(8, 20)  # Healthy food cost
        cost2 = random.randint(2, 10)  # Unhealthy food cost

        while True:  # Validate choice
            print(f"Choose between ${cost} {healthy_choice_dinner} and ${cost2} {unhealthy_choice_dinner}.")
            user_choice = input('What are you craving? ').lower()

            if user_choice == healthy_choice_dinner:
                calories = random.randint(400, 730)
                print(f"You chose {healthy_choice_dinner}.")
                total_calories += calories
                budget -= cost
                print(f'You lost ${cost}. Total balance: ${budget}.')
                break
            elif user_choice == unhealthy_choice_dinner:
                calories = random.randint(800, 2000)
                print(f"You chose {unhealthy_choice_dinner}.")
                total_calories += calories
                budget -= cost2
                print(f'You lost ${cost2}. Total balance: ${budget}.')
                break
            else:
                print("Invalid choice! Choose between the items listed.")

        time.sleep(3)
        print(f"Day {day} is over...")
        time.sleep(3)
        print('Resting...') #day is over and cycles.
        time.sleep(5)

        # Checks for End game conditions to break while loop and brings up statistics to show the user how the addiction works.
        if (total_calories >= 10000) and (day <= 7):
            print("Hey! You've gained more than 10,000 calories within a week!")
            time.sleep(2)
            print("This is very dangerous for an average person. Would you like to know more?")
            choice = input("Yes or No: ").lower()

            if choice == 'yes':
                print("The U.S. Department of Health says that adult males generally require 2,000-3000 calories per day to maintain weight while adult females need around 1,600-2,400.")
                time.sleep(1)
                print("For more assistance on losing weight or finding a solution to weight problems, please contact a trusted provider. Example: https://www.obesity.org/contact-us/")
                time.sleep(1)
                print("Thank you for playing!")
                break
            else:
                print("Okay, no worries! \nThank you for playing!")
                break

        if (total_calories < 10000) and (day >= 7):
            print("Hey! You've gained less than 10,000 calories within a week!")
            time.sleep(1)
            print("Thank you for playing. You've done great and completed this game without reaching obesity.")
            break

        if (budget <= 0):
            print("Hey! You've run out of money!")
            time.sleep(1)
            print("You didn't manage your budget well enough! \nThanks for playing!")
            break

        day += 1  # Increment day at the end of the loop

def gamble():
    total = 0 #variables to check
    win = 0
    lose = 0
    counter = 1000
    print('Guess a number from 1-10 to earn money!')
    print('type 100 any time in the inputs to learn about your statistics!')
    print('A win is worth $180 and a loss is worth -$60')

    while counter >= 0: #Makes sure that for statistics its not doing 0 / 0 which causes an error.
    
      if total > 0: #Win rate
          calculate_wr = round((win / total) * 100, 2)
      else:
          calculate_wr = 0.0  
          
      if total > 0: #Loss rate
          calculate_lr = round((lose / total) * 100, 2)
      else:
          calculate_lr = 0.0 

      print('$:', counter)
      user_guess = int(input('Guess: '))
      total += 1
      Random_number = (random.randint(1, 10))
      if user_guess == Random_number: #Modify variables if user wins/losses etc.
          counter += 180
          print('the selected number was', Random_number)
          print('You gained 180 dollars.')
          win += 1
      elif user_guess == 100:
          print(f'Here are your statistics! \n Win rate: {calculate_wr}% \n Loss rate: {calculate_lr}% \n Total games: {total}')
          continue
      else:
          counter -= 60
          print('the selected number was', Random_number)
          print('You lost 60 dollars.')
          lose += 1

      if counter <= 0:
          print('You have gone bankrupt. \n Please use this as a learning lesson to stop gambling!')
          break

def screen(): #Starts screen addiction.
    total_hours = 0
    total_dopamine = 0
    day = 1

    while True:
        print(f'Day {day}...')
        print('It\'s morning! What do you want to do? ')
        time.sleep(3)

        healthy_activities = [activity.lower() for activity in ['Exercise', 'Read Books', 'Meditate', 'Walk Outside', 'Cook']]  # new healthy activities
        unhealthy_activities = [activity.lower() for activity in ['Play Video Games', 'Binge Watch TV', 'Scroll on Social Media', 'Watch Endless YouTube', 'Online Gambling']]  # new unhealthy activities

        # Morning choice
        healthy_choice_morning = random.choice(healthy_activities)
        unhealthy_choice_morning = random.choice(unhealthy_activities)

        while True:  # Keep asking until a valid input
            choice = input(f'Do you want to {healthy_choice_morning} or {unhealthy_choice_morning}? ').lower()

            if choice == healthy_choice_morning:
                hours = random.randint(1, 3)
                dopamine = random.randint(1, 5)
                print(f'You will be spending {hours} hours today on {healthy_choice_morning}.\n Dopamine + {dopamine}.')
                total_hours += hours #adds to counter
                total_dopamine += dopamine
                break
            elif choice == unhealthy_choice_morning:
                hours = random.randint(3, 10)
                dopamine = random.randint(10, 25)
                print(f'You will be spending {hours} hours today on {unhealthy_choice_morning}.\n Dopamine + {dopamine}.')
                total_hours += hours
                total_dopamine += dopamine
                break
            else:
                print('Invalid choice. Please try again.')

        time.sleep(4)
        print('Noon has approached! What do you want to do? ')
        time.sleep(1)

        # Noon choice
        healthy_choice_noon = random.choice(healthy_activities)
        unhealthy_choice_noon = random.choice(unhealthy_activities)

        while True:  # Keep asking until a valid input
            choice = input(f'Do you want to {healthy_choice_noon} or {unhealthy_choice_noon}? ').lower()

            if choice == healthy_choice_noon: #if the choice is healthy execute.
                hours = random.randint(1, 3)
                dopamine = random.randint(1, 5)
                print(f'You will be spending {hours} hours today on {healthy_choice_noon}.\n Dopamine + {dopamine}.')
                total_hours += hours
                total_dopamine += dopamine
                break
            elif choice == unhealthy_choice_noon: #if the choice is unhealthy execute.
                hours = random.randint(4, 10)
                dopamine = random.randint(10, 25)
                print(f'You will be spending {hours} hours today on {unhealthy_choice_noon}.\n Dopamine + {dopamine}.')
                total_hours += hours
                total_dopamine += dopamine
                break
            else:
                print('Invalid choice. Please try again.')

        time.sleep(4)
        print('Evening has approached! What do you want to do? ')
        time.sleep(1)

        # Evening choice
        healthy_choice_evening = random.choice(healthy_activities)
        unhealthy_choice_evening = random.choice(unhealthy_activities)

        while True:  # Keep asking until a valid input
            choice = input(f'Do you want to {healthy_choice_evening} or {unhealthy_choice_evening}? ').lower()

            if choice == healthy_choice_evening:
                hours = random.randint(1, 3)
                dopamine = random.randint(1, 5)
                print(f'You will be spending {hours} hours today on {healthy_choice_evening}.\n Dopamine + {dopamine}.')
                total_hours += hours
                total_dopamine += dopamine
                break
            elif choice == unhealthy_choice_evening:
                hours = random.randint(4, 10)
                dopamine = random.randint(10, 25)
                print(f'You will be spending {hours} hours today on {unhealthy_choice_evening}.\n Dopamine + {dopamine}.')
                total_hours += hours
                total_dopamine += dopamine
                break
            else:
                print('Invalid choice. Please try again.')

        time.sleep(1)
        print('Night has approached. Time to rest!')
        time.sleep(1)
        print(f'You have spent a total of {total_hours} hours today on activities.')
        time.sleep(1)
        print(f'Your total dopamine is {total_dopamine}.')
        time.sleep(1)
        print('Resting...')
        time.sleep(5)
        #End Game Conditions to breal loop.
        if (total_dopamine >= 100) and (day <= 7): 
            print("Hey, you've earned over 100 dopamine within a week. \n You've become addicted to an unhealthy lifestyle. #add statistics")
            break
        elif (total_dopamine < 100) and (day >= 7):
            print("You've earned less than 100 dopamine within a week. Great Job! #add statistics")
            break

        day += 1 #add a day after going through the loop til 7 (a week)

#Cool title screen
print("""
       d8888 8888888b.  8888888b. 8888888 .d8888b. 88888888888 8888888 .d88888b.  888b    888  .d8888b.
      d88888 888  "Y88b 888  "Y88b  888  d88P  Y88b    888       888  d88P" "Y88b 8888b   888 d88P  Y88b
     d88P888 888    888 888    888  888  888    888    888       888  888     888 88888b  888 Y88b.
    d88P 888 888    888 888    888  888  888           888       888  888     888 888Y88b 888  "Y888b.
   d88P  888 888    888 888    888  888  888           888       888  888     888 888 Y88b888     "Y88b.
  d88P   888 888    888 888    888  888  888    888    888       888  888     888 888  Y88888       "888
 d8888888888 888  .d88P 888  .d88P  888  Y88b  d88P    888       888  Y88b. .d88P 888   Y8888 Y88b  d88P
d88P     888 8888888P"  8888888P" 8888888 "Y8888P"     888     8888888 "Y88888P"  888    Y888  "Y8888P"



""")
print("Please pick what addiction you're suffering from. \nChoose from the following options: \nSubstance, Gambling, Food, Gaming, Masturbation")

while True: #Addictions to pick from and goes through that function which executes the simulatior code.
    choice = input("Enter your choice: ")
    if (choice == 'substance' or choice == 'Substance'):
        print("You're suffering from Substance addiction.")
        break
    elif (choice == 'gambling' or choice == 'Gambling'):
        gamble()
        break
    elif (choice == 'food' or choice == 'Food'):
        food()
        break
    elif (choice == 'screen' or choice == 'Screen'):
        screen()
        break
    else:
        print("Invalid choice. Please try again.")
