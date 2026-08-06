# Import ElementTree module
import xml.etree.ElementTree as ET
# Import re module, needed to help format the desired strings in movie.xml file
import re
# Load and parse xml file
tree = ET.parse("movie.xml")
root = tree.getroot()
# Collect unique child tags of movie elements using iter()
movie_child_tags = set()
for movie in root.iter("movie"):
    movie_child_tags.update(child.tag for child in movie)
# Display all child tags of the movie element, joining them with a comma and space
print("The four child tags of the movie element are: " + ", ".join(movie_child_tags) + ".\n")            
# Format and display all the movie descriptions
print("All movie descriptions:")
for description in root.iter("description"):
    # Join text and remove extra spaces and newlines
    movie_descriptions = " ".join(description.itertext()).strip()
    # Replace multiple spaces and newlines with a single space
    movie_descriptions = re.sub(r"\s+", " ", movie_descriptions)
    # Display each description clearly with some formatting
    print(f"- {movie_descriptions}")
# Initialise count variables
favorite_count = 0
non_favorite_count = 0
# Count the number of favourite and non-favourite movies
for movie in root.iter("movie"):
    # Homogenize cases
    favorite = movie.get("favorite", "").lower()                                                       
    if favorite == "true":
        favorite_count += 1
    elif favorite == "false":
        non_favorite_count += 1
# Display favorite and non-favorite counts
print(f"\nThe number of favorite movies is: {favorite_count}")
print(f"The number of non-favorite movies: {non_favorite_count}")