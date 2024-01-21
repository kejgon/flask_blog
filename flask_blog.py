from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/")
def home():
    """
    Route to display a simple "Hello, World!" message.

    Returns:
        str: A string containing the HTML markup for the "Hello, World!" message.
    """
    return render_template('index.html',posts=posts)



@app.route("/about")
def about():
    return render_template('about.html',title='About us')


if __name__ == "__main__":
    app.run(debug=True)
