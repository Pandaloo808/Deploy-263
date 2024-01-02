from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def anything():
	return "hello I am Riya and I am Happy, Merry Christmas🎄🎅🤶❄￣へ￣"


if __name__=='__main__':
	app.run()