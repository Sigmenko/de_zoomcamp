import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@pg-database:5432/ny_taxi')

data = { 
    'user_id': [1,2,3],
    'name': ['Nikita', 'Jessi', 'admin'],
    'role': ['Student', 'Dog', 'System administator'],
    'level': [10, 99, 80]
}

df = pd.DataFrame(data)

print(df)

print("\n🚀 Відправляю дані в базу...")

df.to_sql(name='users_test', con= engine, if_exists= "replace", index=False)