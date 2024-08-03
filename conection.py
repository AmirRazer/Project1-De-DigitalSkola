# import os
# import json
# import psycopg2
# from sqlalchemy import create_engine


# def config(conection_db):
#     path = os.getcwd()
#     with open(path + '/config.json') as file:
#         conf = json.load(file)[conection_db]
#     return conf

# def getconn(conf, name_con):
#     try:
#         conn = psycopg2.connect(
#             host=conf['host'],
#             database=conf['db'],
#             user=conf['user'],
#             password=conf['password'],
#             port=conf['port']
#         )
#         print(f"Connected to {name_con}!")
#         engine = create_engine(
#             "postgressql+psycopg2://{}:{}@{}:{}/{}".format(
#                 conf['user'],
#                 conf['password'],
#                 conf['host'],
#                 conf['port'],
#                 conf['db']
#             )
#         )
#         return conn, engine
#     except Exception as e:
#         print(f"Error: {e}")
#         return None, None
import os
import json
import psycopg2
from sqlalchemy import create_engine

def config(conection_db):
    path = os.getcwd()
    with open(path + '/config.json') as file:
        conf = json.load(file)[conection_db]
    return conf

def getconn(conf, name_con):
    try:
        conn = psycopg2.connect(
            host=conf['host'],
            database=conf['db'],
            user=conf['user'],
            password=conf['password'],
            port=conf['port']
        )
        print(f"Connected to {name_con}!")
        engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
                conf['user'],
                conf['password'],
                conf['host'],
                conf['port'],
                conf['db']
            )
        )
        return conn, engine
    except Exception as e:
        print(f"Error: {e}")
        return None, None