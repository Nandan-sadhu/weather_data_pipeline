from pipeline.ingest import fetch_weather_data
from pipeline.transform import transform_weather_data
from pipeline.load import save_to_db, save_to_parquet

def main():
    # Step 1: Fetch
    json_data = fetch_weather_data()
    if not json_data:
        print("No data fetched.")
        return

    # Step 2: Transform
    df = transform_weather_data(json_data)

    # Step 3: Load
    save_to_db(df)
    save_to_parquet(df)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()