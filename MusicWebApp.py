"""
Put your Flask app code here.
"""


from flask import Flask, request, render_template, url_for, flash, redirect
app = Flask(__name__)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
	if request.method == 'POST':
		song = request.form['song']
		print(song)
		if song == "The Best Song Ever":
			print("yes")
			pic = "https://i.kinja-img.com/gawker-media/image/upload/s--qn6H3zL3--/c_scale,fl_progressive,q_80,w_800/jiszvtpozcrbbzxrxmq6.jpg"
		elif song == "Twinkle Twinkle Little Star":
			pic = "http://img.clipartall.com/yellow-star-border-clip-art-clipart-panda-free-clipart-images-yellow-star-clipart-552_599.png"
		else:
			pic = "https://athousandsimpletests.files.wordpress.com/2013/08/all-or-nothing.jpg"
		return render_template("UserInterface.html", song = song, pic = pic)
	

	return render_template("Toolbox.html")




if __name__ == "__main__":
	app.run().run()