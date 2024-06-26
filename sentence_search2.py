import sqlite3
from sys import argv

def search_db(search_term):
    # Connect to the database
    conn = sqlite3.connect('/home/jack/Desktop/FlaskBlog/instance/blog3.db')
    cursor = conn.cursor()

    # Split the input search term into individual words
    search_terms = set(search_term.lower().split())

    # Construct the WHERE clause for the SQL query to filter rows based on any of the search terms
    where_conditions = []
    for term in search_terms:
        where_conditions.append("content LIKE ?")
    
    where_clause = " OR ".join(where_conditions)
    query = f"SELECT ROWID, content FROM post WHERE {where_clause}"

    # Execute the SELECT query with the constructed WHERE clause
    rows = cursor.execute(query, ['%' + term + '%' for term in search_terms])

    best_match = None
    max_unique_count = 0

    # Iterate over the resulting rows
    for row in rows:
        row_id, content = row
        content_words = set(content.lower().split())
        unique_count = len(search_terms & content_words)
        
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            best_match = (row_id, content, unique_count)

    conn.close()

    if best_match:
        row_id, content, unique_count = best_match
        return [f"ROWID: {row_id}\nContent:\n{content}\nUnique matches: {unique_count}"]
    else:
        return ["No results found."]

if __name__ == '__main__':
    if len(argv) < 2:
        print("Please provide a search term.")
    else:
        search_term = argv[1]
        results = search_db(search_term)
        for result in results:
            print(result)
