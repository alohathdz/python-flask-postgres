import psycopg2

def select(): 
  try:
    conn = psycopg2.connect(
        host="localhost",
        database="ct526",
        user="postgres",
        password="p@ssw0rd"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM movie;")

    rows = cur.fetchall()

  except psycopg2.Error as e:
    return None

  finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
    return rows