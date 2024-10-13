import json
import pg8000
import boto3

def connect_to_db():
    conn = pg8000.connect(
        host="krish.crk8cew4aiu0.ap-south-1.rds.amazonaws.com",
        database="postgres",
        user="postgres",
        password= "postgres",
        port="5432"
    )
    return conn

def lambda_handler(event, context):
    for record in event['Records']:
        message = record['body']
        
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
            conn.commit()
            cur.close()
            conn.close()

            print(f"Message stored: {message}")

        except Exception as e:
            print(f"Error processing message: {e}")