from flask import Flask, render_template, request, redirect, url_for, flash
from controllers.research_letter_controller import research_interest_advanced

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

app.add_url_rule('/research_interest_advanced', 'research_interest_advanced', research_interest_advanced, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)
