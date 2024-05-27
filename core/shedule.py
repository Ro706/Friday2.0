import mysql.connector
from datetime import datetime
from typing import List, Tuple

def get_schedule(day: str) -> List[Tuple[str, str]]:
    """
    Fetch the schedule for a given day from the 'timetable_a_sem1' table.

    Parameters:
    day (str): The day for which the schedule is requested (e.g., 'Monday').

    Returns:
    List[Tuple[str, str]]: A list of tuples containing time and subject.
    """
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',       # e.g., 'localhost'
            user='root',   # e.g., 'root'
            password='root123', # your database password
            database='friday'  # e.g., 'friday'
        )
        cursor = conn.cursor()
        if(conn.is_connected()):
            print("Connected to MySQL database")
        # Query to fetch the schedule for the given day
        query = "SELECT time, subject FROM timetable_a_sem1 WHERE day = %s"
        cursor.execute(query, (day,))
        
        # Fetch all results
        schedule = cursor.fetchall()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        return schedule

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

# Example usage:
day = datetime.now().strftime("%A")
schedule = get_schedule(day)
for time, subject in schedule:
    print(f"Time: {time}, Subject: {subject}")
