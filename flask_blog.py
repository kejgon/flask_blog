from flask import Flask, render_template, url_for
from forms import  RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='ff93cedce7fbdd43168d6be0145e0952'

posts =[
    {'title':'First Post Blog',
     'author':'John Doe',
     'contents':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum',
     'posted_on':'Jan 20, 2024'},
     {'title':'Second Post Blog',
     'author':'John Peter',
     'contents':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum',
     'posted_on':'Jan 20, 2024'}
]

### HOME ROUTE
@app.route("/")
def home():
    """
    Route to display a simple "Hello, World!" message.

    Returns:
        str: A string containing the HTML markup for the "Hello, World!" message.
    """
    return render_template('index.html',posts=posts)


### ABOUT US ROUTE
@app.route("/about")
def about():
    return render_template('about.html',title='About us')

### REGISTER ROUTE
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

### LOGIN ROUTE
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == "__main__":
    app.run(debug=True)
