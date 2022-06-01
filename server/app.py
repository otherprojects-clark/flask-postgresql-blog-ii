from flask import Flask, request, jsonify
from db.db import Database
from flask_cors import cross_origin
from secrets import token_hex
from arrow import utcnow
from os import environ
from utils.jsonutils import get_json_with_props

environ["FLASK_ENV"] = "development"

app = Flask(__name__)
app.secret_key = token_hex()

def init_db():
  dat = Database()
  cur = dat.db.cursor()
  with open('schema.sql', 'r') as schema:
    cur.execute(schema.read())
  dat.db.commit()
  cur.close()
  dat.db.close()
init_db()

# main
@app.route('/')
def index():
  return "clark johnny sins"

@app.route('/create', methods=['GET', 'POST'])
@cross_origin()
def create():
  dat = Database()
  cur = dat.db.cursor()
  if request.method == "POST":
    data = request.get_json()
    title = data['title']
    content = data['content']
    createdat = utcnow().to('local').format('MMM D, YYYY h:mm A')
    cur.execute(f"insert into posts (title, body, createdat, updatedat) values ('{title}', '{content}', '{createdat}', '-')")
    dat.db.commit()
    cur.close()
    dat.db.close()
    print("Post created successfully")
  return "Post created successfully"

@app.route('/post/<int:id>')
@cross_origin()
@app.errorhandler(404)
def post(id):
  dat = Database()
  cur = dat.db.cursor()
  cur.execute(f"select * from posts where id={id}")
  post = cur.fetchone()

  if not post:
    return "Post not found", 404
  else:
    title = post[1]
    content = post[2]
    createdat = post[3]
    updatedat = post[4]

    return {
      "title": title, 
      "content": content, 
      "createdat": createdat, 
      "updatedat": updatedat
    }

@app.route('/posts')
@cross_origin()
def posts():
  dat = Database()
  cur = dat.db.cursor()
  cur.execute('select * from posts;')
  posts = cur.fetchall()
  cur.close() 
  dat.db.close()
  print(posts)
  res = get_json_with_props(posts)
  return res

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
@cross_origin()
def delete(id):
  dat = Database()
  cur = dat.db.cursor()
  cur.execute(f"select * from posts where id={id}")
  post = cur.fetchone()
  cur.execute('select id from posts')
  if request.method == 'POST':
    cur.execute(f"delete from posts where id={id}")
    dat.db.commit()
    cur.close()
    dat.db.close()
    return "post deleted"
  else: 
    return "get post"

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@cross_origin()
def edit(id):
  dat = Database()
  cur = dat.db.cursor()
  cur.execute(f"select * from posts where id={id}")
  post = cur.fetchone()
  cur.execute('select id from posts')
  if request.method == 'POST':
    data = request.get_json()
    title = data['title']
    content = data['content']
    updatedat = utcnow().to('local').format('MMM D, YYYY h:mm A')

    cur.execute(f"update posts set title='{title}', body='{content}', updatedat='{updatedat}' where id={id};")
    dat.db.commit()
    cur.close()
    dat.db.close()


    print(request.get_json())
  pass
  return ""



if __name__ == '__main__':
  app.run(debug=True)
  