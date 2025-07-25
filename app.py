from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///chetan.db'
db =SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def add_user():
    if request.method=='POST':
            email = request.form['email']
            password = request.form['password']
            u1 = User(email=email, password=password)
            db.session.add(u1)
            db.session.commit()

    data = User.query.all()
    return render_template("login.html",data=data)

@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)