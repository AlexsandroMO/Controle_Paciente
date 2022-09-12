import sqlite3
from datetime import datetime
import pandas as pd
import pandasql as pdsql


def create_db():
  conn = sqlite3.connect('DB_PROJECT.db')
  c = conn.cursor()
  
  table_createdb = f"""
                      CREATE TABLE Paciente (
                        ID INTEGER PRIMARY KEY,
                        NAME VARCHAR(50) NOT NULL,
                        AGE DATE NOT NULL,
                        GEN VARCHAR(10) NOT NULL,
                        CPF INTEGER NOT NULL,
                        P_PAC INTEGER,
                        A_PAC REAL,
                        DATE_LOG DATE NOT NULL
                      )
                    """
  
  c.execute(table_createdb)
  
  conn.commit()
  conn.close()

  return 'Criado!'


def create_data(name,age, gen, cpf, p_pac, a_pac):
    current_date = datetime.now()
    conn = sqlite3.connect('DB_PROJECT.db')
    c = conn.cursor()
    
    data_create = f"""
                       INSERT INTO Paciente(NAME,AGE,GEN,CPF,P_PAC,A_PAC,DATE_LOG)
                       VALUES ('{name}', '{age}','{gen}',{cpf},{p_pac},{a_pac},'{current_date}')
    """
    c.execute(data_create)
    
    conn.commit()
    conn.close()


def read_all():
  conn = sqlite3.connect('DB_PROJECT.db')
  c = conn.cursor()

  sql_datas = f'''
                    SELECT * FROM Paciente;
  '''

  read = pd.read_sql_query(sql_datas, conn)
  conn.close()

  return read


def read_id(page_id):

  conn = sqlite3.connect('DB_PROJECT.db')
  c = conn.cursor()

  sql_datas = f"""
                  SELECT * FROM Paciente WHERE ID={page_id};
              """

  read_db = pd.read_sql_query(sql_datas, conn)
  conn.close()

  return read_db


def ed_data(id_name,name,age,gen,cpf,p_pac,a_pac):
  print('>>>>>: ',id,name,age, gen, cpf, p_pac, a_pac)
  current_date = datetime.now()
  conn = sqlite3.connect('DB_PROJECT.db')
  c = conn.cursor()

  qsl_datas = f"""
                  UPDATE Paciente set NAME='{name}', AGE='{age}', GEN='{gen}', CPF={cpf}, P_PAC={p_pac}, A_PAC={a_pac}, DATE_LOG='{current_date}' Where ID={id_name};
              """

  c.execute(qsl_datas)

  conn.commit()
  conn.close()


def del_data(id_name):
  conn = sqlite3.connect('DB_PROJECT.db')
  c = conn.cursor()

  qsl_datas = f"""
                  DELETE from Paciente Where ID={id_name};
              """
  c.execute(qsl_datas)

  conn.commit()
  conn.close()