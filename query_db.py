import psycopg2

def select(): 
  try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",  # Or your PostgreSQL server's IP address
        database="ct526",
        user="postgres",
        password="p@ssw0rd"
    )

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Execute a SQL query
    cur.execute("SELECT * FROM movie;")

    # Fetch all results
    rows = cur.fetchall()


    # Print the fetched rows
#    for row in rows:
#        print(row)

    # Commit changes (if any DML operations like INSERT, UPDATE, DELETE were performed)
    # conn.commit()

  except psycopg2.Error as e:
    return None

  finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
    return rows