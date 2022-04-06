"""
'Welcome to Em's Movie Cinema'
"""
#Tuple Movie Choices
movies = ('1:Business Propasal','2:Twenty One Twenty Five','3:Thirty Nine','4:Flower of Evil', '5:It')
sessions = ('1:morning', '2:evening', '3:afternoon')
#Seats for each movie and each sessions
movie1 = {'morning': [], 'evening' :[], 'afternoon': []}
movie2 =  {'morning': [], 'evening' :[], 'afternoon': []}
movie3 = {'morning': [], 'evening' :[], 'afternoon': []}
movie4 =  {'morning': [], 'evening' :[], 'afternoon': []}
movie5 =  {'morning': [], 'evening' :[], 'afternoon': []}



print("Welcome to the Cinemia")
#name = input('What is your name? ')
#phone_number = input ('What is your phone number? ')
name = 'Em'
phone_number = 91929192

print("These are todays movies")
print("*************************************")
for movie in movies:
    print(movie)

movie_choice = None
while movie_choice not in range(1,6):
    try:
        movie_choice = int(input ('Please, enter your movie: '))
    except:
        print ('Please enter a number between 1 and 5')
        movie_choice = None

print("Available sessions")
print("*************************************")
for session in sessions:
    print(session)

session_choice = None
while session_choice not in sessions:
    try:
        movie_choice = int(input ('Please, enter your session: '))
    except:
        print ('Please enter a number between 1 and 4')
        movie_choice = None

    sessions_choice = input ('Please, enter your sessions: ')

#Finally print user's choices
print (f"Name: {name}, Phone number: {phone_number}, Movie: {movie_choice}")
#movie seat choices 
available_seats = ["1","2","3","6", "7", "8"]
print(available_seats)
def seats(seat):
    seat = seat.lowers ()
    match seat:
        case"1":
            return 0
        case"2":
            return 1
        case"3":
            return 2
        case"6":
            return 3
        case"7":
            return 4
        case"8":
            return 5
        case _: 
            return "Invalid seat"
seat = input("These seats are available, which seat would you like to choose? ")
if (seats(seat))== "Invalid seat":
    while (seats(seat)) == "Invalid seat":
        seat == input("These seats are available, which would you like?  ")
        if (seats(seat) !="Invalid seat":
            available_seats[seats[seat]] = "(X)"
            break
    else:
        print(" ")
        print("Error, your seat is not available")
        print(" ")
        print(available_seats)
        seat = input("These seats are available, which would you like? ")     
        print(" ")       

available_seats[seats[seat]] = "(X)"
print(available_seats):




book_again = True 

while book_again:
    Ticket_Sytem()
    #customers final decisions
    answer = ''
    while answer not in ("yes", "no"):
        answer = input("Do you want to book your movie ticket again? ")
        answer = answer.lower ()

        if answer == "yes":
            book_again = True 
        else:
            book_again = False

        print('Thank you for visitng us and enjoy your movie') 
