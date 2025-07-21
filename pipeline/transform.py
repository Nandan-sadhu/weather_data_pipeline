import pandas as pd
from datetime import datetime

def transform_weather_data(json_data):
    hourly = json_data['hourly']
    df = pd.DataFrame({
        'datetime': hourly['time'],
        'temperature': hourly['temperature_2m']
    })
    
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['temperature'] = df['temperature'].astype(float)

    # Add timestamp column for tracking when data was fetched
    df['fetched_at'] = datetime.utcnow().isoformat()

    return df