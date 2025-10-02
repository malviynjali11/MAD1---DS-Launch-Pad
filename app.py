from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        print(first_name)
        print(last_name)
        return redirect('/dashboard/'+first_name)
    
@app.route('/dashboard/<firstname>', methods=['GET', 'POST'])
def dashboard(firstname):
    if request.method == 'GET':
        return render_template('dashboard.html', first_name=firstname)
    
# methods are the list of methods only allowed methods to the server


if __name__ == "__main__":
    app.run(debug=True)