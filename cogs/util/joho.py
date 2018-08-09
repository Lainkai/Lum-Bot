#This is 日本語 (Japanese) for information
#It Loads files and other data.

import json
import mysql.connector

class joho:

    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)     
    
    def save(self, dicti, path):

        with open(path, "w", encoding="utf-8") as f:
            json.dump(dicti,f)
        
    def sql(self,creds):
        self.mydb = mysql.connector.connect(
            host=creds[0],
            user=creds[1],
            passwd=creds[2],
            database=creds[3]
        )
        self.curs = self.mydb.cursor()
        
    def select(self, column, table, conditional=None):
        if conditional:
            self.curs.execute("SELECT %s FROM %s WHERE %s" % (column, table, conditional))
        else:
            self.curs.execute("SELECT %s FROM %s" % (column, table))
        return self.curs.fetchall()
            