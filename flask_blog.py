from flask import Flask, render_template 
# __name__ is a special keyword used to represent a class name 
app = Flask(__name__)

posts = [ {
    'author':'Ephie Oyedoh',
    'title':'Ephie\'s Birthday',
    'content':'Hello',
    'date_posted':'18/03/95'
},{
    'author':'Mine Ibi',
    'title':'Mine\'s Birthday',
    'content':'Hello',
    'date_posted':'31/10/99'
}]

@app.route('/')
@app.route('/home')
@app.route('/HOME')
def home ():
    return render_template('home.html', posts=posts)

@app.route('/about')
@app.route('/ABOUT')
def about_us ():
    return render_template('about.html',  title='About')

if __name__ == '__main__':
    app.run(debug=True)

# set FLASK_APP=flask_blog.py
# python -m flask run