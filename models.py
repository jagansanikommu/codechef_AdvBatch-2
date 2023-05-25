import sqlite3 as sql
from os import path
from datetime import datetime
from Test import count



ROOT = path.dirname(path.relpath((__file__)))

def create_post(content):
    con=sql.connect(path.join(ROOT,'database.db'))
    cun = con.cursor()
    cun.execute('insert into posts(name, content) values(?, ?)', ("jagan", content))
    con.commit()
    con.close()

def get_posts():
    con=sql.connect(path.join(ROOT,'database.db'))
    cun = con.cursor()
    cun.execute('select content from posts')
    posts =cun.fetchall()
    return posts

def clear_data():
    con=sql.connect(path.join(ROOT,'database.db'))
    cun = con.cursor()
    cun.execute('DELETE FROM posts;',)
    con.commit()
    con.close()

def get_data(batch):
    con=sql.connect(path.join(ROOT,'database.db'))
    cun = con.cursor()
    cun.execute("select * from "+batch)
    data = cun.fetchall()
    return data

def update_data(batch):
    if (datetime.weekday(datetime.now()))!=3:
        return "Updation allowed only on Monday"
    else:
        con=sql.connect(path.join(ROOT,'database.db'))
        cun = con.cursor()
        # undo changes
        cun.execute('select user_name from '+batch)
        data =cun.fetchall()
        data1 = count(data)
        cun.execute('update '+batch+' set previous_week = recent_week ',)
        for i in range(len(data)):
            img=data1[i]
            cun.execute('update '+batch+' set recent_week = ? where s_no = ?', (img,i+1))
        cun.execute('update '+batch+' set count = recent_week - previous_week ',)
        con.commit()
        con.close()
        return "Updated Successfully"
    

