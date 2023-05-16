### Introduction
- This the week 2 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Define a function called `max_val(input_list)` that takes a nested list `input_list` and return the maximum value of each inner list.
   - E.g.: `L = [[1,2,5], [4,3,3], [1,7,6]]` `max_val(L) => [5,4,7]`
2. Write the sql query to do the following. You can assume that we have created the `employee_records` table from the lecture
   - Update the value of the `DIVISION` column to `Hardware` for the employee whose `ID=3` 
   - Delete the entry for all employee whose `STARS = 3`
3. In this homework, we will study ridge regression with the utilities data set
   - Remove `gasbill`, `elecbill` and `notes` columns from the dataframe
   - `kwh` means kilowatt-hours and `ccf` means cooling capacity factor
   - The goal is to use `month`, `day`, `year`, `temp`, `kwh`, `ccf`, `thermsPerDay`, `billingDays` to predict `totalbill`
   - Split the data into training and testing set (80/20) and use a random seed of 42
   - Using `sklearn.preprocessing.StandardScaler` to standardize the dataset. Remember to `fit_transform` on the training set and just `transform` on the test set.  
   - Set the range of alpha to `np.linspace(0.001, 50, 20)` and run a manual grid-search (for-loop) to find the optimal value of alpha (in terms of R-squared value on the test set).
   - Retrain the ridge model with the best alpha and return it.
4. Write a regex pattern that will match any 3-character (or more) sequence. For example
   - `re.search(regex_pattern, 'abc de')` => Match
   - `re.search(regex_pattern, 'abcde')` => Match
   - `re.search(regex_pattern, 'ab cd')` => Not match
5. Populate the `simple_bettor_v2` function by making some changes to the `simple_bettor` function from the lecture.
   - Copy the `play_round` function from the previous homework.
   - Increase the wager size to 3000.
   - Modify it so that it returns the game_count instead of funds.