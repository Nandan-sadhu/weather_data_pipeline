import pandas as pd

def main():
    df = pd.read_parquet("data/processed/weather.parquet")

    print("🔍 Data Overview:")
    print(df.info())

    print("\n📊 Head of Data:")
    print(df.head())

    print("\n📈 Temperature Statistics:")
    print(df['temperature'].describe())

    print("\n📅 Date Range:")
    print(f"From {df['datetime'].min()} to {df['datetime'].max()}")

    print("\n🕒 Number of fetch batches (non-null fetched_at):")
    print(df['fetched_at'].notnull().sum())

if __name__ == "__main__":
    main()
