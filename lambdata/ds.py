import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

def train_validation_test_split(self, df, features, target,
                                train_size=0.7, val_size=0.1,
                                test_size=0.2, random_state=None,
                                shuffle=True):
    '''
    This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or 
    matrices into train, validation, and test subsets.
​
    Args:
        df (Pandas DataFrame): Dataframe with code.
        X (list): A list of features.
        y (str): A string with target column.
        train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
        val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
        test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
        random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
        shuffle (bool): Whether or not to shuffle the data before splitting
​
    Returns:
        Train, test, and validation dataframes for features (X) and target (y). 
    '''

    X = df[features]
    y = df[target]

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
        random_state=random_state, shuffle=shuffle)

    return X_train, X_val, X_test, y_train, y_val, y_test


def list2column(list, df, colname):
    '''
    Enter your list, dataframe and column name 
    function takes the list and turns it into a column in the entered dataframe 
    '''
    series = pd.Series(list)
    df[colname] = series


def datecreate(df, col):
    df[col] = pd.to_datetime(df[col], infer_datetime_format=True)
    year = []
    [year.append(yr) for yr in df[col].Year]
    df[year] = year
    month = []
    [month.append(mon) for mon in df[col].Month]
    df[month] = month
    day = []
    [day.append(dy) for dy in df[col].Day]
    df[day] = day

def abb_to_state(my_df):
    '''
    Takes in a dataframe with state codes and expands them to full state names
    '''
    new_df = my_df.copy
    names_map = {'AL':'Alabama', 'AK':'Alaska', 'AZ':'Arizona', 'AR': 'Arkansas',
    'CA':'California', 'CO':'Colorado'}
    new_df['State'] = new_df['state_code'].map(names_map)
    return new_df


if __name__ == '__main__':
    #simple test of enlarge function
    # print(enlarge(5))
    

    breakpoint()