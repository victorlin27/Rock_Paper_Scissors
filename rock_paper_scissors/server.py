from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'men'

@app.route('/')
def index():
    if 'draws' not in session:
        session['draws']= 0
        session['loses'] = 0
        session['wins'] = 0
        session['outcomes'] = []
    return render_template('index.html')

@app.route('/choice', methods=['POST'])
def choice():
    opp_choice = ['Rock','Paper','Scissors']
    randomint = random.randint(0,len(opp_choice) -1)
    session['opp_choice'] = opp_choice[randomint]
    session['our_choice'] = request.form['our_choices']
    if session['our_choice'] == session['opp_choice']:
        session['draws'] += 1
        session['result'] = 'Draw'
        color = 'blue'
    elif session['our_choice'] =='Rock' and session['opp_choice'] =='Paper':
        session['loses'] += 1
        session['result'] = 'Lose'
        color = 'red'        
    elif session['our_choice'] =='Rock' and session['opp_choice'] =='Scissors':
        session['wins'] += 1
        session['result'] = 'Win'
        color = 'green'        
    elif session['our_choice'] =='Paper' and session['opp_choice'] =='Rock':
        session['wins'] += 1
        session['result'] = 'Win' 
        color = 'green'       
    elif session['our_choice'] =='Paper' and session['opp_choice'] =='Scissors':
        session['loses'] += 1
        session['result'] = 'Lose'
        color = 'red'
    elif session['our_choice'] =='Scissors' and session['opp_choice'] =='Paper':
        session['wins'] += 1
        session['result'] = 'Win'
        color = 'green'
    elif session['our_choice'] =='Scissors' and session['opp_choice'] =='Rock':
        session['loses'] += 1
        session['result'] = 'Lose'
        color = 'red'
    message = (f"Your opponent chose {session['opp_choice']}, You chose {session['our_choice']}. You {session['result']}")
    session['outcomes'].append({'color': color , 'message': message})
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)