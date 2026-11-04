import pandas as pd

def transform_data(data):

    df = pd.DataFrame(data)

    columns = [
        "id",
        "name",
        "username",
        "email",
        "phone",
        "website"
    ]

    df = df[columns]

    print(df.head())

    return df