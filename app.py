from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy employee data (you might have a database in practice)
employee_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_employee', methods=['POST'])
def submit_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        email = request.form['email']
        phone = request.form['phone']

        # Simulating saving employee data to a dictionary
        employee_data[name] = {
            'name': name,
            'position': position,
            'email': email,
            'phone': phone,
            # Add other data as needed
        }

        # Redirect to the employee dashboard with the submitted employee's name
        return redirect(url_for('employee_dashboard', employee_name=name))

@app.route('/employee_dashboard/<employee_name>')
def employee_dashboard(employee_name):
    employee = employee_data.get(employee_name)
    return render_template('ind.html', employee=employee)

if __name__ == '__main__':
    app.run()
