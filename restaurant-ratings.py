# your code goes here
#define a function that takes in a text file
restaurant_and_ratings = {}

def return_ratings(filename):
    """Take in a text file and returns restaurant ratings"""

    ratings_info = open(filename)


    # Go through each line of the file and assign the
    # name of the restaurant as a key, and rating as a value
    # Adding key:value pairs to the empty dictionary
    for line in ratings_info:
        line = line.rstrip().split(":")
        restaurant_and_ratings[line[0]] = line[1] 

    # Create a list of restaurants, and sort alphabetically 
    alphabetical_restaurants = sorted(list(restaurant_and_ratings))

    # Alternative way to sort dictionary using .items()???
    # alphabetical_restaurants = restaurant_and_ratings.items().sort()

    # Printing a sorted list of restaurant names from the list
    # and pairing with values of ratings from the dictionary
    for restaurant in alphabetical_restaurants:
        print "%s is rated at %s." % (restaurant, restaurant_and_ratings[restaurant])
    
    ratings_info.close()

def add_new_restaurant_rating(filename):
    # get the name of the restaurant from the user and the rating
    # then add this info to the restaurants_and_ratings dictionary
    users_restaurant = raw_input("Provide name of restaurant: ")
    users_restuarant_score = raw_input("Provide restaurant rating on scale of 1 to 5: ")
    restaurant_and_ratings[users_restaurant] = users_restuarant_score
    #call return_ratings functions to sort all restauratns including new 
    return_ratings(filename)
