from connection import pool

conn = pool.get_connection()
cursor = conn.cursor()

try:
    query = """
    DELETE FROM login_attempts
    WHERE attempt_time < NOW() - INTERVAL 1 DAY
    """

    cursor.execute(query)
    conn.commit()

finally:
    cursor.close()
    conn.close()