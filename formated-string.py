# QUESTION 1:
# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :
# Twinkle, twinkle, little star,
#	 How I wonder what you are! 
#		 Up above the world so high,   		
#	 	 Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#	 How I wonder what you are


# If this was HTML we would use the <pre> tag.
# But in Python we use triple single quotes or double single quotes.

print(
    '''
    Twinkle, twinkle little star,
        How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
    Twinkle, twinkle little star,
        How I wonder what you are
    '''
)