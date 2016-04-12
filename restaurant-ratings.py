# your code goes here
#define a function that takes in a text file
def return_ratings(filename):
    """Take in a text file and returns restaurant ratings"""

    ratings_info = open(filename)

    restaurant_and_ratings = {}

    # Go through each line of the file and assign the
    # name of the restaurant as a key, and rating as a value
    # Adding key:value pairs to the empty dictionary
    for line in ratings_info:
        line = line.rstrip().split(":")
        restaurant_and_ratings[line[0]] = line[1] 

    # Create a list of restaurants, and sort alphabetically 
    alphabetical_restaurants = sorted(list(restaurant_and_ratings))

    # Alternative way to sort dictionary using .items()
    # alphabetical_restaurants = restaurant_and_ratings.items().sort()

    # Printing a sorted list of restaurant names from the list
    # and pairing with values of ratings from the dictionary
    for restaurant in alphabetical_restaurants:
        print "%s is rated at %s." % (restaurant, restaurant_and_ratings[restaurant])
    
    ratings_info.close()

