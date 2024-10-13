import pg8000

try:
    conn = pg8000.connect(
        host="krish.crk8cew4aiu0.ap-south-1.rds.amazonaws.com",
        database="postgres",
        user="postgres",
        password="postgres",
        port=5432
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
