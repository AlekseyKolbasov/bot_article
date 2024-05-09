import sqlite3


def create_db():
    db = sqlite3.connect('data_base.sql')
    cur = db.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS arcticls (url text)')
    db.commit()
    db.close()


def add_to_db(url): 
    with sqlite3.connect('data_base.sql') as db:
        cur = db.cursor()
        cur.execute('SELECT url FROM arcticls')
        if url in str(cur.fetchall()):
            return True
        
        else:
            cur.execute(f'INSERT INTO arcticls (url) VALUES ("{url}")')
            db.commit
            pass
            

def take_url():
    with sqlite3.connect('data_base.sql') as db:
        cur = db.cursor()
        cur.execute('SELECT url FROM arcticls')
        if cur.fetchone() == None:
            return False

        else:
            cur.execute('SELECT url FROM arcticls ORDER BY RANDOM()')
            url = cur.fetchone()[0]
            db.commit
            return url
    
    
def delete_arcticle(url):
    with sqlite3.connect('data_base.sql') as db:
        cur = db.cursor()
        cur.execute(f'DELETE FROM arcticls WHERE url = "{url}"')
        db.commit  
    