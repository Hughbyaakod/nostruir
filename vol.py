import pandas as pd
from sqlalchemy import create_engine

# Create a DataFrame
df = pd.DataFrame({'name': ['User 4', 'User 5']})

# Create a connection to your database
engine = create_engine('your_database_connection_string')

# Use the to_sql() function to write the DataFrame to a table in the database
df.to_sql(name='users', con=engine, if_exists='append')
