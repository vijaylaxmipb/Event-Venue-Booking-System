from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return "Welcome to the Event Venue Booking System!"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 8080)),
        debug=os.environ.get("DEBUG") == "True"
    )

