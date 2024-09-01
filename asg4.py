def get_list(file : str) -> list:
    """
    It gets the list from the file txt and it returns a new list only with the rows from the txt file. 
    
    Argument:
    (str) file - file from we are taking the builidng from

    Returns:
    (list) building list - a 2D list with all the rows from the building
    """
    
    building_list = [] # list to add all the rows

    for line in file:
        row = line.strip().replace('|', ' ').split() # replaces unnecessary characters and split the line into a list
        building_list.append(row) # add the list from the variable row
    
    building_list.reverse() # it's reversed to operate with the table more easily for the stone material (review line 61-63 for more information)
    
    return building_list 



def get_scores(building_list : list) -> list:
    """
    The function takes the building list and it stores each of the material's score. 
    Then it calculates the total score from each material and append each of 
    them to a score list.
    
    
    Argument:
    (list) building list - a list with the rows or floor from the building. Represented as 2D list 

    Returns:
    (list) score total - each of the score from each material all in one list 
    """
    glass_score = 0 
    recycled_score = 0
    stone_score = 0
    wood_score = 0
    # These are the variables to storage the score from each material
    
    count = 0 # It's used for the recycled score to keep track of how many R are found in total

    for row_index in range(len(building_list)): # it gives access to the rows from the table
        row = building_list[row_index] # storage each row from the list
        for col_index in range(len(row)): # it gives access to each to the columns of the table
            col = building_list[row_index][col_index] # storage each die
            if '--' in col:
                continue # jump to the next column 
            elif 'G' in col: 
            # for every G found in the list, it takes the number that it attached to and
            # and it adds that number to the glass score
                glass_score += int(col[1])

            elif 'R' in col: 
            # for every R found it's going to add 1 to the count.
                count += 1

            elif 'S' in col: 
            # for each row, since the table is reversed, it's going to add the specific
            # points depending on the row index the S was found to stone score(see lines 75-82). by flipping the table then 
            # I'm able to score from zero as the lowest row in the building
                if row_index == 0:
                    stone_score += 2
                elif row_index == 1:
                    stone_score += 3        
                elif row_index == 2:
                    stone_score += 5   
                else:
                    stone_score += 8

            elif 'W' in col:
            # for every W found, it's going to check all the adjancents from the position of the variable
            # then for every non empty space in the adjacents, then it's going to add 2 points to wood score
                if building_list.index(row) > 0:
                    if building_list[row_index - 1][col_index] != '--': # checks for elements above
                        wood_score += 2
                if building_list.index(row) < (len(building_list) - 1): 
                    if building_list[row_index + 1][col_index] != '--':# checks for elements below
                        wood_score += 2
                if row.index(col) > 0:
                    if building_list[row_index][col_index - 1] != '--': # checks for elements on the left
                        wood_score += 2
                if row.index(col) < (len(row) -1):
                    if building_list[row_index][col_index + 1] != '--': # checks for elements on the right
                        wood_score += 2
    # this block of code assigns the value of the recycled score by comparing the count variable 
    if count == 0:
        recycled_score = 0
    elif count == 1:
        recycled_score = 2  
    elif count == 2:
        recycled_score = 5   
    elif count == 3:
        recycled_score = 10  
    elif count == 4:
        recycled_score = 15   
    elif count == 5:
        recycled_score = 20 
    else:
        recycled_score = 30 

    # this is the list with the total score. It has all the scores from each material
    return [glass_score, recycled_score, stone_score, wood_score]



def get_table_totals(building_list : list, score_totals : list) -> None:
    """
    Takes the list from the score, and it represents it back like the original 
    file and with the scoring totals from each material. the file is called scoring-results.txt

    Arguments:
    (list) building_list - same list to be able to write it in the new file
    (list) score_totals - a list with the total score in order to add them to the file
    """
    
    score_file = open(r'.\datafiles\scoring-results.txt', 'w')
    building_list.reverse() # to put back in order the row from the building
    string_list = [] # a list to first join the all the row and then use this list to put it back as a string

    for row_index in range(len(building_list)): # goes row by row to join the elements back to a single element
        row = building_list[row_index]
        string_list.append('|'.join(row)) # joins each row into one element with the characters '|' in between and appends each line
        
    line = '\n'.join(string_list) # to join each element back into one string
    
    score_file.write(f'{line}\n\n')
    score_file.write('+----------+----+\n')
    score_file.write(f'| glass    | {score_totals[0]:>2} |\n')
    score_file.write(f'| recycled | {score_totals[1]:>2} |\n')
    score_file.write(f'| stone    | {score_totals[2]:>2} |\n')
    score_file.write(f'| wood     | {score_totals[3]:>2} |\n')
    score_file.write('+==========+====+\n')
    score_file.write(f'| total    | {sum(score_totals):>2} |\n')
    score_file.write('+----------+----+\n')
    # this is the final table score with each of the totals for each material and the final score
    score_file.close()
    


def main() -> None:
    file_reader = open(r'.\datafiles\building.txt', 'r') # opens the file in read mode
    
    building_list = get_list(file_reader) # type: ignore # store the returned value from the function
    file_reader.close()

    get_table_totals(building_list, get_scores(building_list)) # get_scores works as a parameter for get_table_totals
    
main()


#https://stackoverflow.com/questions/11059910/skipping-elements-in-a-list-python how to skip an element in a list with for loops