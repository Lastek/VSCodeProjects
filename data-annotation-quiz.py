# Ingest data from a google doc file 
# The file contains a table with columns: x-coordinate, Character, y-coordinate
# We need to read these coordinates and the character and place it in a grid which is printed in a fixed-width font.
# The grid has min coord of 0 and no maximum
# The Character is unicode character

import requests
import pandas as pd
# Get the google doc file
url = 'https://docs.google.com/document/u/0/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub?pli=1'

data = None
df = pd.read_html(url, encoding='utf-8', header=0)
df

# Create a 2D list to represent the grid
grid = [[' ' for _ in range(df['x-coordinate'].max() + 1)] for _ in range(df['y-coordinate'].max() + 1)]

# Loop over the rows of the DataFrame
for index, row in df.iterrows():
    # Get the x and y coordinates and the character
    x = row['x-coordinate']
    y = row['y-coordinate']
    character = row['Character']
    
    # Place the character in the right position on the grid
    grid[y][x] = character

# Print the grid
for row in grid:
    print(''.join(row))