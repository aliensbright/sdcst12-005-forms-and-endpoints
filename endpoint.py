from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/form.html", methods=['POST'])
def endpoint():
    data = request.form
    print(data)
    output = f"""
    <!doctype html>
    <head>
        <title> Form Result </title>
        <style>
            .result {{
                color: blue;
                font-size: 2em;
            }}
        </style>
    </head>
    <body>
        <div class='result'>Today we went to {data('pname')} Lake. At {data('pname')} 
        Lake, we saw a {data('animal')}. Since I am not scared of {data('animal')}s, I 
        went to pet it with my hand. The {data('animal')} was very {data('adjective')} when I 
        pet it. My friend, {data('fname')}, on the other hand, felt very {data('emotion')}
        and poked it with their {data('tool')} weapon. The {data('animal')} ended up 
        {data('verb')} us. The end.
        </div>
    </body>
    """
    return output 

@app.route("/", methods=["POST"])
def anotherFunction():
    pass


app.run(port=5000)