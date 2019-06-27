from app import app
@app.route('/index')
def index():
    user = {'username':'amritpal gamer’}
    return ''' 
html
head
title homepage-micro_blog title
/head
body
h1 hello, ''' +user['username']+ '''!/h1
body
html'''            
            




    

