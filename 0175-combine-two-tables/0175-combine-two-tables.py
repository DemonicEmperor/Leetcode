import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df =  pd.merge(person,address, how = "left",on = "personId")
    selected = df[["firstName" , "lastName" , "city" , "state"]]
    return selected
    