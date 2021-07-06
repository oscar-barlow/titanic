import pandas as pd

def clean_titanic_data(data: pd.DataFrame, inplace: bool = False) -> pd.DataFrame:
    data["SexCode"] = data["Sex"].apply(lambda sex: 1 if sex == "male" else 2)
    data.drop(columns=['Name', 'Ticket', 'Cabin', 'Embarked', 'Sex'], inplace=inplace)
    return data