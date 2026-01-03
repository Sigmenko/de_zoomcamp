import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data_from_api(*args, **kwargs):
    # Офіційний файл з зонами таксі
    url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv'
    
    response = requests.get(url)
    
    # Читаємо CSV
    df = pd.read_csv(io.StringIO(response.text))
    
    # Дивимось, що там всередині
    print(df.head())
    
    return df