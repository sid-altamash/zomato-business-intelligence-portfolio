import glob
import os
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Database Configuration
DB_USER = 'root'
DB_PASSWORD = 'Altamash%401'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'zomato_db'

# Build connection string
connection_string = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(connection_string)

def import_csv_to_mysql():
    csv_files = glob.glob('*.csv')
    
    if not csv_files:
        print('❌ No CSV files found in this directory!')
        return
    
    print(f'Found {len(csv_files)} CSV files. Preparing database...\n')
    
    # Step A: Completely wipe out old tables and ignore all constraints first
    with engine.begin() as conn:
        conn.execute(text('SET FOREIGN_KEY_CHECKS = 0;'))
        
        # Automatically fetch and drop every table currently in zomato_db
        result = conn.execute(text("SHOW TABLES;"))
        tables = [row[0] for row in result]
        
        for table in tables:
            print(f'Dropping old conflicting table: `{table}`')
            conn.execute(text(f'DROP TABLE IF EXISTS `{table}`;'))
            
        conn.execute(text('SET FOREIGN_KEY_CHECKS = 1;'))

    print('\nOld database clutter cleared. Starting fresh import...\n')
    
    # Step B: Loop through and import each CSV file cleanly
    for file_path in csv_files:
        base_name = os.path.basename(file_path)
        table_name = base_name.split('.')[0].replace('(1)', '').replace('(2)', '').strip().lower().replace(' ', '_')
        
        try:
            print(f'Reading "{base_name}" -> Target Table: `{table_name}`')
            df = pd.read_csv(file_path)
            
            # Clean column names
            df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
            
            # Push DataFrame to MySQL as a clean flat table
            df.to_sql(table_name, con=engine, if_exists='replace', index=False, chunksize=5000)
            print(f'✅ Successfully imported {len(df)} rows into MySQL table: `{table_name}`\n')
            
        except Exception as e:
            print(f'❌ Error importing {base_name}: {e}\n')

if __name__ == '__main__':
    print('Starting clean table import into MySQL...\n')
    import_csv_to_mysql()
    print('Data import process completed!')