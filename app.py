from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def places():
    return render_template('places.html')
@app.route('/add', methods=['POST'])
def show():
    addr = request.form.get('place', '', type=str)
    return jsonify(addr)
