from flask import Flask, render_template, send_from_directory



app = Flask(__name__)

def serve_directory(root_directory, relative_path):
    index_of_last_slash = relative_path.rfind('/')
    relative_directory = relative_path[:index_of_last_slash] if index_of_last_slash > 0 else ''
    filename = relative_path[index_of_last_slash + 1:] if index_of_last_slash > 0 else relative_path
    directory = root_directory + relative_directory
    print(directory, filename)
    return send_from_directory(directory, filename)

@app.route('/WWM/<path:relative_path>')
def serve_wwm_original(relative_path):

    root_directory = '/home/Timo/Documents/WWM Projekt/'
    return serve_directory(root_directory, relative_path)
    

@app.route('/files/<path:relative_path>')
def serve_files(relative_path):

    root_directory = '/home/timo/my_flask_app/files/'
    return serve_directory(root_directory, relative_path)
    


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('infosite.html')

@app.route('/question/<path:id>')
def question(id):
    id=int(id)
    question=''
    correctanswer=0
    answer1=''
    answer2=''
    answer3=''
    answer4=''
        
    if id == 1:
        question='Kann man nicht einschlafen, so hilf oft...'
        correctanswer=1
        answer1='...Schäfchen zählen.'
        answer2='...Entlein durchgehen.'
        answer3='...Täubchen abklappern.'
        answer4='...Hündlein berechnen.'
    elif id == 2:
        question='Den chemischen Stoff O² nennt man...'
        correctanswer=2
        answer1='...Helium.'
        answer2='...Sauerstoff.'
        answer3='...Methan.'
        answer4='...Kohlensäure.'
    elif id == 3:
        question='Die Mona Lisa wurde von... gemalt.'
        correctanswer=2
        answer1='...Michelangelo'
        answer2='...Leonardo da Vinci'
        answer3='...Pablo Picasso'
        answer4='...Vincent Van Gogh'
    elif id == 4:
        question='Die Redewendung "Auf 180 sein" bedeutet, dass man... ist'
        correctanswer=4
        answer1='...traurig'
        answer2='...glücklich'
        answer3='...hungrig'
        answer4='...wütend'
    elif id == 5:
        question='Die Kindergeschichte... stammt aus Deutschland.'
        correctanswer=1
        answer1='...Biene Maja'
        answer2='...Puuh der Bär'
        answer3='...Lars, der kleine Eisbär'
        answer4='...Thomas, die kleine Lokomotive'
    elif id == 6:
        question='Die Stadt... wird auch als "ewige Stadt" bezeichnet.'
        correctanswer=3
        answer1='...Paris'
        answer2='...Madrid'
        answer3='...Rom'
        answer4='...Wien'
    elif id == 7:
        question='Sprichwörtlich gibt es im...'
        correctanswer=4
        answer1='...Osten nur Altes.'
        answer2='...Norden keine Sitten.'
        answer3='...Süden alles Junge.'
        answer4='...Westen nichts Neues.'
    elif id == 8:
        question='Der Antagonist aus "Star Wars Episode IV: Eine neue Hoffnung" heißt...'
        correctanswer=3
        answer1='...Grand Admiral Tarkin.'
        answer2='...Yoda.'
        answer3='...Darth Vader.'
        answer4='...Luke Skywalker.'
    elif id == 9:
        question='Die kleine Grüne Gestalt aus "Star Wars: The Mandalorian" heißt...'
        correctanswer=1
        answer1='...Grogu.'
        answer2='...Baby Yoda.'
        answer3='...Anakin Skywalker.'
        answer4='...Boba Fett.'
    elif id == 10:
        question='Saladin war ursprünglich Sultan von...'
        correctanswer=3
        answer1='...Galiläa.'
        answer2='...Zypern.'
        answer3='...Ägypten.'
        answer4='...Jordanien.'
        

    return render_template('questionsite.html', id=id, correctanswer=correctanswer, question=question, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4)

@app.route('/won/<path:id>')
def won(id):
    id=int(id)
    price=''

    if id == 1:
        price='€ 0'
    elif id == 2:
        price='€ 50'
    elif id == 3:
        price='€ 100'
    elif id == 4:
        price='€ 500'
    elif id == 5:
        price='€ 1.000'
    elif id == 6:
        price='€ 5.000'
    elif id == 7:
        price='€ 10.000'
    elif id == 8:
        price='€ 50.000'
    elif id == 9:
        price='€ 100.000'
    elif id == 10:
        price='€ 500.000'
    elif id == 11:
        price='€ 1.000.000'


    return render_template('wonsite.html', id=id, price=price)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
