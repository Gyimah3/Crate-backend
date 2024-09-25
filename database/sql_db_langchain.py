from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import sessionmaker
from functools import lru_cache

@lru_cache(maxsize=1)
def get_engine():
    return create_engine("sqlite:///crate_data.db")

def init_db():
    # Load retail_data.csv
    df_retail = pd.read_csv("database/retail_data.csv")
    # Removing commas from 'Unit_Price' and converting to float
    df_retail['Unit_Price'] = df_retail['Unit_Price'].str.replace(',', '').astype(float)
    # Removing commas from 'Sales_Volume(KG_LTRS)' and converting to float
    df_retail['Sales_Volume(KG_LTRS)'] = df_retail['Sales_Volume(KG_LTRS)'].str.replace(',', '').astype(float)
    # Converting 'Period' to datetime using the specified format
    df_retail['Period'] = pd.to_datetime(df_retail['Period'], format='%b-%y')
    # Removing commas from 'Sales_Value' and converting to float
    df_retail['Sales_Value'] = df_retail['Sales_Value'].str.replace(',', '').astype(float)

    # Load crate.csv
    df_crate = pd.read_csv("database/crate_imputed.csv")
    # Add any necessary preprocessing for df_crate here

    engine = get_engine()
    
    # # Write both dataframes to SQLite
    # df_retail.to_sql("retail_data", engine, index=False, if_exists="replace")
    df_crate.to_sql("crate_data", engine, index=False, if_exists="replace")

db = SQLDatabase(engine=get_engine())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
init_db()
