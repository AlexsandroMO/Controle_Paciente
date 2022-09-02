import sqlite3
from datetime import datetime

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

