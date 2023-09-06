import psycopg2

# Define your PostgreSQL database connection parameters
db_params = {
    'dbname': 'Adventureworks',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'db',  # e.g., 'localhost' or your database server's IP address
    'port': '5432'   # default is 5432
}
# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
    exit(1)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Define the SQL query to retrieve table metadata
table_name = 'employee'
# Query to retrieve table metadata, including constraints
query = f"""
    SELECT 
        c.column_name, 
        c.data_type, 
        c.character_maximum_length,
        c.numeric_precision,
        c.column_default,
        c.is_nullable,
        cc.constraint_name
    FROM 
        information_schema.columns AS c
    LEFT JOIN 
        information_schema.constraint_column_usage AS cc
    ON 
        c.column_name = cc.column_name
    WHERE 
        c.table_name = '{table_name}';
"""
print(query)

# Execute the query
try:
    cur.execute(query)
except psycopg2.Error as e:
    print("Error executing query:", e)
    conn.close()
    exit(1)

# Fetch all rows from the result set
metadata = cur.fetchall()

# Print the table metadata, including constraints
print(f"Metadata for table '{table_name}':")
for row in metadata:
    column_name, data_type, max_length, numeric_precision, default_value, is_nullable, constraint_name = row#, constraint_type = row
    print(f"Column Name: {column_name}, Data Type: {data_type}, Max Length: {max_length}, Numeric Precision: {numeric_precision}, Default Value: {default_value}, Is Nullable: {is_nullable}")
    if constraint_name:
        print(f"Constraint Name: {constraint_name}") #, Constraint Type: {constraint_type}")


# Close the cursor and database connection
cur.close()
conn.close()
