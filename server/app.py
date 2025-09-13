from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Main page with title in h1 element
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    # Print the string to console and display in browser
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    # Display all numbers in the range of the parameter on separate lines with trailing newline
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)