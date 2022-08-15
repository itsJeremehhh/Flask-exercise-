# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_params():
    """Add a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def sub_params():
    """Subtrack a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = sub(a, b)
    
    return str(result)

@app.route("/mult")
def mult_params():
    """Multiply a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = mult(a, b)
    
    return str(result)

@app.route("/mult")
def div_params():
    """Divide a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = div(a, b)
    
    return str(result)

operators = {
    "add": add, 
    "sub": sub, 
    "mult": mult, 
    "div": div, 
}

@app.route("/math/<oper")
def math(oper):
    """Do math on a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)