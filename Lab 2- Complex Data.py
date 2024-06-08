def main():

# Define the complex data structure
    about_me ={
            'full_name': 'Joelle Waugh',
            'Student_id':10338342,
            'Pizza_toppings': [
                'pepperoni', 
                'mushrooms',
                'olives'
            ],
            'movies':[
                {
                    'title': 'Lord of the rings',
                    'genre': 'fanasty'
                },

                {
                    'title': 'iRobot',
                    'genre': 'sci-fi/Action'
                }
            ]
            
        }

# Add a new movie to the data structure
    about_me['movies'].append({'title': 'Inception','genre':' Sci-fi/Action'})
# Function that prints student name and ID	
def print_student_name_and_id(about_me):
    name = about_me['full_name'].split(' ')
    print (f'My name is {about_me['full_name']} , but you can call me {name[0]}.')

    print (f'My student ID is {about_me['Student_id']}')
    print()
    return
    
#Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)

    for i,t in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = t.lower()

    about_me['pizza_toppings'].sort()
    return

# Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
      toppings = (f'My favourite pizza toppings are:{about_me['pizza_toppings_1']} {about_me['pizza_toppings_2']} {about_me['pizza_toppings_3']}')
      print(toppings)
      print('-'* len (toppings))
    
      for t in about_me['pizza_toppings']:
          print (f'- {t}')
      print()

      return

# Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print(f"I like to watch {about_me['movies:genre[0]']},{about_me['movies:genre[1]']},{about_me['movies:genre[2]']} movies.")
    return 

#  Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    print(f"Some of my favourite movies are {about_me['movies'['title']]. split(' ')}, end = ' '!")
    movie_list=''
    for m in 'movies'['title']:
        movie_list += m['title'] + ','
    print (movie_list)
    return
    
if __name__ == '__main__':
    main()