
       """"
Movie Theatre 
"""
#ask for name and number
import email


print("*******************************")
print("Welcome to Em Movie Theater!")
print("*******************************")
name = input("What is your name? ")
number = None
#checks if input is a number
while not isinstance (number, int):
        try:
            number = int(input("What is your phone number? Please enter a valid phone number? "))
        except:
            print (' Please enter a valid phone number.')
#books movie
movies = ['a. Despicable Me', 'b. Cocomelon', 'c. Superman']
def booking():

    #useful variables
    global movies

    print("----------------------------")
    print("Today's movies")
    print("----------------------------")

    #prints movies
    for movie in movies:
        print (movie)

    movie_choice = None

    #match cases users input to the movies
    while movie_choice not in ('a','b','c'):

        movie_choice = input ('Please, select a movie (a/b/c): ')

        match movie_choice:
            case 'a':
                print('You have chosen', movies[0])
                chosen_movie = movies[0]
            case 'b':
                print('You have chosen', movies[1])
                chosen_movie = movies[1]
            case 'c':
                print('You have chosen', movies[2])
                chosen_movie = movies[2]
            case '':
                print('Invalid choice')
    return chosen_movie
#books time
times = ['a. Morning', 'b. Afternoon', 'c. Evening']
def booking_t():        
    global times
    #prints time
    for time in times:
        print (time)

    time_choice = None

    #match cases users input to the session of movie
    while time_choice not in ('a','b','c'):

        time_choice = input ('Please, select time (a/b/c): ')

        match time_choice:
            case 'a':
                print('You have chosen', times[0])
                chosen_time = times[0]
            case 'b':
                print('You have chosen', times[1])
                chosen_time = times[1]
            case 'c':
                print('You have chosen', times[2])
                chosen_time = times[2]
            case _:
                print('Invalid choice')
    return chosen_time

#seats
movie_seats = (([],[],[]),([],[],[]),([],[],[]))
#for morning cocomelonem

def movie_seat(chosen_movie, chosen_time): 
    booked_seats=[]
    while True:  
        movie_index = movies.index(chosen_movie)
        time_index = times.index(chosen_time)
      
        seats_txt = ''
        for seat_n in range(1,11):
            if seat_n in movie_seats[movie_index][time_index]:
                seats_txt = seats_txt + ' X'
            else:
                seats_txt = seats_txt + f' {seat_n}'

        print (seats_txt)
        #asks for seat and appends it into booked_seats
        chosen_seat = None
        while chosen_seat not in range(1,11):
            #Validate that while not chosen_seat.isnumber():  
            chosen_seat = int(input("What seat do you want? "))
            
            if chosen_seat in movie_seats[movie_index][time_index]:
                print("Seat has been chosen, Please choose a different seat.")
            else:
                movie_seats[movie_index][time_index].append(chosen_seat)
                booked_seats.append(chosen_seat)

        #if the user wants it reruns the program
        choose_again = None
        choose_again = input("Do you want to book a seat again?(y/n): ")
        if choose_again == 'n':
            print("Thanks")
            break
    return booked_seats

#confirmation function
def confirmation(chosen_movie, chosen_time):
    print("So, ", name.title(), "and your phone number ", number, ". You have chosen ", chosen_movie, "at ", chosen_time, ". Your seat is at", chosen_seat), 
    choose_again = None
    choose_again = input("Is this information correct?(y/n): ")
    if choose_again == 'y':
        print("Thanks")
        return False
    else:
        return True

#calls and reruns the program if there was a problem
while True:  
    chosen_movie = booking()
    chosen_time = booking_t()
    chosen_seat = movie_seat(chosen_movie, chosen_time)
    if not confirmation(chosen_movie, chosen_time):
        break
    
