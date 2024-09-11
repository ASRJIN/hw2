import sqlite3
import pandas as pd
import numpy as np


def max_val(input_list):
    """
    :param input_list: a nested list
    :return: the maximum value of each inner list
    """
    # Your code here
    return list(map(max,input_list))


# Update the value of the `Division` column to Hardware for the employee whose ID=3
sql_query_1 = "UPDATE employee_records SET DIVISION = 'Hardware' WHERE ID = 3"

# Delete the entry for all employee whose STARS = 3
sql_query_2 = "DELETE FROM employee_records WHERE STARS = 3"


def train_model():
    np.random.seed(42)
    utility = pd.read_csv('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/utilities.csv',
                          index_col=0)

    # Your code here
    #drop unnecessary columns
    utility = utility.drop(columns=['gasbill', 'elecbill', 'notes'])
    #use month, day, year, temp, kwh, ccf, thermsPerDay, billingDays to predict totalbill
    X = utility[['month', 'day', 'year', 'temp', 'kwh', 'ccf', 'thermsPerDay', 'billingDays']]
    y = utility['totalbill']
    #Split the data into training and testing set (80/20) and use a random seed of 42
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #Using sklearn.preprocessing.StandardScaler to standardize the dataset. 
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    #Set the range of alpha to np.linspace(0.001, 50, 20) 
    alphas = np.linspace(0.001, 50, 20)
    
    best_alpha = 0
    best_r2 = -np.inf
    
    # run a manual grid search for the best alpha
    for alpha in alphas:
        ridge = Ridge(alpha=alpha)
        ridge.fit(X_train_scaled, y_train)
        y_pred = ridge.predict(X_test_scaled)
        r2 = r2_score(y_test, y_pred)
        
        if r2 > best_r2:
            best_r2 = r2
            best_alpha = alpha
    
    # Retrain the model with the best alpha
    best_ridge_model = Ridge(alpha=best_alpha)
    best_ridge_model.fit(X_train_scaled, y_train)
    
    return best_ridge_model, best_alpha, best_r2
        
    

regex_pattern = '\w\w\w'


def play_round():
    # Roll a 100 sided die.
    # Use the roll_dice function defined above.
    # Return True if win and False if lose.
    # Your code here
    roll = roll_dice()
    if roll >= 1 and roll <= 50:
        return True
    else:
        return False


def simple_bettor_v2(initial_funds, initial_wager, intended_rounds):
    # Your code here
    funds = initial_funds
    wager = initial_wager
    game_count = 0
    while game_count < intended_rounds and funds > 0:
        if play_round():
            funds += wager
        else:
            funds -= wager

        game_count +=1
    return game_count

