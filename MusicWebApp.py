"""
Put your Flask app code here.
"""


from flask import Flask, request, render_template, url_for, flash, redirect
app = Flask(__name__)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():

	if request.method == 'POST':
		age = request.form['age']
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		Ninja = request.form['Ninja']
		return render_template("UserInterface.html", age= age, firstname = firstname, lastname = lastname, Ninja = Ninja)
	

	return render_template("Toolbox.html")




if __name__ == "__main__":
	app.run()