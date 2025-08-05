# !uv pip install mysql-connector-python



import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

user = mysql.connector.connect(
  user = os.getenv("DB_USER"),
  password = os.getenv("DB_PASSWORD"),
  host = os.getenv("DB_HOST"),
  port = os.getenv("DB_PORT"),
  database = os.getenv("DB_NAME")
)

user_cmd = user.cursor()

query = '''
CREATE TABLE conversation_store(
  "ID" integer NOT NULL,
  "chat_name" character varying(60),
  "conv_id" character varying(20),
  "user_id" integer NOT NULL,
  "message_count" integer,
  "created_at" timestamp,
  "updated_at" timestamp,
  PRIMARY KEY ("ID")
);
'''

user_cmd.execute(query)



# Show tables
show_tables = 'SHOW TABLES;'
user_cmd.execute(show_tables)

# Fetch and print the result
for table in user_cmd.fetchall():
    print(table)


user_cmd.execute('SELECT * FROM conversation_store LIMIT 0')

# Extract column names
column_names = [desc[0] for desc in user_cmd.description]
print(column_names)

message_store = '''
CREATE TABLE message_store(
  "ID" integer NOT NULL,
  "role" integer,
  "conv_id" character varying(20),
  "message_no" integer,
  "message_id" character varying(20),
  "message" text,
  "elapsed_time" integer,
  "Status" integer,
  "created_at" timestamp,
  "updated_at" timestamp,
  PRIMARY KEY ("ID")
);
'''

user_cmd.execute(message_store)

# Show tables
show_tables = 'SHOW TABLES;'
user_cmd.execute(show_tables)

# Fetch and print the result
for table in user_cmd.fetchall():
    print(table)

user_cmd.execute('SELECT * FROM message_store LIMIT 0')

# Extract column names
column_names = [desc[0] for desc in user_cmd.description]
print(column_names)