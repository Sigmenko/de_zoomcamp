from sqlalchemy import create_engine, text
db_url = 'postgresql://root:root@localhost:5432/ny_taxi'

engine = create_engine(db_url)

print("try connect")

try:
    with engine.connect() as connection:
        print("acces connect ")

        result = connection.execute(text("SELECT 1"))
        print(f"Result = {result.fetchone()}")

except Exception as e:
    print(f"Problem = {e}")