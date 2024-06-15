import sqlite3
from sys import argv

def search_db(search_term):
    # Connect to the database
    conn = sqlite3.connect('instance/blog2.db')
    cursor = conn.cursor()

    # Split the input search term by space to get individual words
    search_terms = search_term.split()

    # Construct the WHERE clause for the SQL query to filter rows based on any of the search terms
    where_conditions = []
    for term in search_terms:
        where_conditions.append("content LIKE ?")
    
    where_clause = " OR ".join(where_conditions)
    query = f"SELECT ROWID, content FROM post WHERE {where_clause}"

    # Execute the SELECT query with the constructed WHERE clause
    rows = cursor.execute(query, ['%' + term + '%' for term in search_terms])

    data = []
    results = []

    # Iterate over the resulting rows and count the number of matching words
    for row in rows:
        row_id, content = row
        word_count = sum(content.lower().count(term.lower()) for term in search_terms)
        if word_count > 0:
            results.append((row_id, content, word_count))
    
    conn.close()

    # Sort the results by the number of matching words in descending order
    results.sort(key=lambda x: x[2], reverse=True)

    # Format the results for printing
    for idx, result in enumerate(results, start=1):
        row_id, content, word_count = result
        data.append(f'{row_id} {content[:50]}... ({word_count} matches) {idx}')

    if not data:
        return ["No results found."]
    else:
        return data

if __name__ == '__main__':
    if len(argv) < 2:
        print("Please provide a search term.")
    else:
        search_term = argv[1]
        lines = search_db(search_term)
        for line in lines:
            print(line)
