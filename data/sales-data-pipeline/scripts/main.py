from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    file_path = "../data/sales_data.csv"
    df = extract_data(file_path)
    cleaned_df = transform_data(df)
    load_data(cleaned_df)

if __name__ == "__main__":
    main()