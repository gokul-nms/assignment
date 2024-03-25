#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

first_friend_movies = []
print("First friend. Enter the movies you like (separated by commas):")
first_friend_input = input().strip().split(',')
first_friend_movies.extend([movie.strip().lower() for movie in first_friend_input])
second_friend_movies = []
print("Second friend .enter the movies you like (separated by commas):")
second_friend_input = input().strip().split(',')
second_friend_movies.extend([movie.strip().lower() for movie in second_friend_input])
common_movies = set(first_friend_movies) & set(second_friend_movies)
if len(common_movies) < 3:
    print("Sorry, There is no three common movies in this list .")
else:
    print("You both like these movies:")
    for movie in common_movies:
        print(movie.capitalize())
