from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine(
        "postgresql+psycopg2://nirdeshzoc@localhost:5432/sales_db"
    )

    df.to_sql("sales", engine, if_exists="replace", index=False)

    print("✅ Success: data loaded into database.")