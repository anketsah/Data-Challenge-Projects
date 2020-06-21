from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

history = []

@app.route('/history')
def get_history():
    return render_template('table.html', history_arr=history)

@app.route('/api/history')
def api_history():
    return jsonify(history)


@app.route('/calculate', methods=['POST','GET'])
def calculate(sum=sum):
    if request.method == 'GET':
        return render_template('app.html')

    elif request.method == 'POST':
        record = []
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        operation = request.form['operation']
        record.append(num1)
        record.append(num2)
        record.append(operation)

        if operation == 'add':
            sum = num1 + num2
        elif operation == 'subtract':
            sum = num1 - num2
        elif operation == 'multiply':
            sum = num1 * num2
        elif operation == 'divide':
             sum = num1 / num2
        else:
            return render_template('app.html')

    record.append(sum)
    history.append(record)

    return render_template('app.html', sum=sum)

