from flask import Flask, render_template, request, redirect
import json
import datetime
import os

app = Flask(__name__)
DATA_FILE = 'data/tickets.json'

def load_tickets():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tickets = load_tickets()
        new_ticket = {
            "id": len(tickets) + 1,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "user": request.form['user'],
            "issue": request.form['issue'],
            "solution": request.form['solution'],
            "status": request.form['status']
        }
        tickets.append(new_ticket)
        with open(DATA_FILE, 'w') as f:
            json.dump(tickets, f, indent=4)
        return redirect('/')
    
    return render_template('index.html', tickets=load_tickets()[::-1]) # Newest first

if __name__ == '__main__':
   import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
