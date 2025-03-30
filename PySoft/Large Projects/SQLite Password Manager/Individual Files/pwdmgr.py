import sqlite3
import random
import os
import pwdgen
class PasswordManager():
    def __init__(self,):
          self.cursor, self.connection= self.connect()
          self.create_table()
          self.character_set = '¦¬`1!23£4$€5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?' #can only use this character set because ggle can't handle é in its gmail passwords.
    def connect(self):
            connection = sqlite3.connect('pwd.db')
            cursor = connection.cursor()
            return cursor,connection
    def create_table(self,): #FEED ME THE CURSOR
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pwdlist (
            id integer primary key,
            NAME text,
            USERNAME text,
            SITE text,                   
            PWD text
        );""")
    def add_pwd(self,name, username, site,pwd):
        self.cursor.execute("""INSERT INTO pwdlist
            (NAME,USERNAME,SITE, PWD)
            values (?,?,?,?)
            """,(name,username,site,pwd))
        self.connection.commit()
    def fetch(self):
        self.cursor.execute("""SELECT * FROM pwdlist
        """)
        rows = self.cursor.fetchall()
        return rows
    def select(self,id):
        self.cursor.execute("""SELECT * FROM pwdlist
                             WHERE ID LIKE ? """,(id))
        selection = self.cursor.fetchall()
        return selection
    def update_pwd(self, id, name, username,site, pwd):
         self.cursor.execute("""UPDATE PWDLIST
            SET NAME = ?,
                USERNAME = ?,
                SITE = ?,
                PWD = ?
            WHERE ID LIKE ?""",(name,username,site,pwd,id,))        
         self.connection.commit()
    def del_pwd(self,id):
         self.cursor.execute("""DELETE FROM PWDLIST
            WHERE ID LIKE ?""",(id))        
         self.connection.commit()         
    def del_all(self):
        self.cursor.execute("""DROP TABLE PWDLIST""")
        self.connection.commit()
        
