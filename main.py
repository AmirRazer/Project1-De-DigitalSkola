# import conection 

# if __name__ == '__main__':
#     #conection data source
#     conf = conection.config('marketplace_prod')
#     conn,engine = conection.getconn(conf, 'marketplace_prod')
#     cursor = conn.cursor()

#     #conection dwh
#     conf_dwh = conection.config('dwh')
#     conn_dwh,engine_dwh = conection.getconn(conf_dwh, 'dwh')
#     cursor_dwh = conn_dwh.cursor()



#     #conection query string

#     #get data

import conection 
import os
import sqlparse
import pandas as pd
if __name__ == '__main__':
    #conection data source
    conf = conection.config('marketplace_prod')
    conn, engine = conection.getconn(conf, 'marketplace_prod')
    if conn:
        cursor = conn.cursor()
    else:
        print("Failed to establish a connection to marketplace_prod.")

    #conection dwh
    conf_dwh = conection.config('dwh')
    conn_dwh, engine_dwh = conection.getconn(conf_dwh, 'dwh')
    if conn_dwh:
        cursor_dwh = conn_dwh.cursor()
    else:
        print("Failed to establish a connection to dwh.")

    #conection query string
    path_query = os.getcwd() + '/query/'
    query = sqlparse.format(
        open(path_query + 'query.sql').read(),strip_comments=True
    ).strip()
    dwh_design = sqlparse.format(
        open(path_query + 'dwh_desaign.sql').read(),strip_comments=True
    ).strip()
    #get data
    try:   
        print('[Info] service etl is running...')
        df = pd.read_sql(query, engine)
        
        #create schema dwh
        cursor_dwh.execute(dwh_design)
        conn_dwh.commit()

        #ingest data ti dwh
        df.to_sql(
            'dim_orders_amir',
            engine_dwh,
            schema='public',
            if_exists='append',
            index=False
        )

    except Exception as e:
        print('[info] ini eror' )
        print(str(e))