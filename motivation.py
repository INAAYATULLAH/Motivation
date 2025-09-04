from flask import Flask, render_template
import random

app = Flask(__name__)


quotes = [
    ("Believe in yourself, even when others don’t.", "The only validation you need is your own."),
    ("Dreams don’t work unless you do.", "Take the first step today."),
    ("Success begins at the edge of comfort.", "Step beyond your limits."),
    ("Small steps every day create big changes.", "Consistency beats intensity."),
    ("You are stronger than your excuses.", "Push through the resistance."),
    ("Your future is created by what you do today.", "Not tomorrow."),
    ("Every setback is a setup for a comeback.", "Keep moving forward."),
    ("Discipline is the bridge between goals and achievement.", "Stay consistent."),
    ("Great things never come from comfort zones.", "Challenge yourself."),
    ("Don’t wait for opportunity.", "Create it."),
    ("Failure is not the opposite of success.", "It’s part of success."),
    ("Your only limit is your mind.", "Think bigger."),
    ("Winners are not people who never fail.", "They are people who never quit."),
    ("Success doesn’t come to you.", "You go to it."),
    ("The harder you work for something.", "The greater you’ll feel when you achieve it."),
    ("Doubt kills more dreams than failure ever will.", "Trust yourself."),
    ("Push yourself, because no one else will do it for you.", "Stay motivated."),
    ("A little progress each day adds up to big results.", "Keep going."),
    ("Your struggles develop your strengths.", "Embrace them."),
    ("If you get tired, learn to rest.", "Not to quit."),
    ("Don’t stop until you’re proud.", "Make yourself proud first."),
    ("It’s not about being the best.", "It’s about being better than yesterday."),
    ("Courage doesn’t mean you don’t get afraid.", "It means you don’t let fear stop you."),
    ("Action is the foundational key to success.", "Keep taking action."),
    ("Don’t wish for it.", "Work for it."),
    ("Do something today that your future self will thank you for.")


]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
