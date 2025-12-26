import random
from datetime import datetime
errors = ["Error 404", "Server Down", "Timeout", "Hackers Attack"]
with open("logs.txt", "w") as f:
    for i in range(50):
        f.write(f"Час: {datetime.now()} | Подія: {random.choice(errors)}\n")
    