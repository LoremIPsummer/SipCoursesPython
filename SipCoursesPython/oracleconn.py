from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import cx_Oracle
import sys
import os

host="localhost"
port="1521"
sid='XE'
user="sipcourse"
password="sipcourse"
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

clientPath = os.path.abspath(os.path.dirname(sys.argv[0]))+"\oracleclient"
cx_Oracle.init_oracle_client(clientPath)

sip_engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)
course_map = declarative_base()
Session = sessionmaker(bind=sip_engine)





