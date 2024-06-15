#!/home/jack/miniconda3/envs/cloned_base/bin/python
import json
import logging
import os
import sqlite3
from sys import argv
#database_name = '/home/jack/Desktop/HDD500/databases/dialogueEXP2_app_f.db'
database_name = 'CHATGPT_text.db'
conn = sqlite3.connect(database_name)
cursor = conn.cursor()
cnt = 0
'''
    scheme show tables;
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY,
        filename TEXT NOT NULL,
        content BLOB NOT NULL,
        text_content TEXT NOT NULL,
        hash_value TEXT NOT NULL,
        format TEXT NOT NULL
    )
'''
# Define the search terms
search_terms = argv[1].split(",")  # Split the input string by comma to get individual search terms

# Construct the WHERE clause for the SQL query to filter rows based on all search terms
where_conditions = []
for term in search_terms:
    where_conditions.append(f"text_content LIKE '%{term}%'")
where_clause = " AND ".join(where_conditions)

# Execute the SELECT query with the constructed WHERE clause
query = f"SELECT ROWID,* FROM files WHERE {where_clause}"
rows = cursor.execute(query)

# Iterate over the resulting rows and print the ROWID and user_ChatGPT_PAIR column
for row in rows:
    cnt += 1
    print(row[0], row[1],"\n",row[4],"\n","COUNT:",cnt)

# Close the connection
conn.close()
