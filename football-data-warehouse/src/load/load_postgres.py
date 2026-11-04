from sqlalchemy import create_engine

def get_engine():

    engine = create_engine(
        "postgresql://postgres:root@localhost:5432/football_dw"
    )

    return engine