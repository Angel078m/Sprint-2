# Step 0 - import sqelite3
import sqlite3
import queries as q

# step1 - Connect to Database
# triple-check the spelling of your database filename
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - Make the 'cursor'
cursor = connection.cursor()

# step 3 - write a query
# (see queries.py file)

#step 4 - Execute the query on the cursor and fetch the results
# 'Pulling the result from the cursor'
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
