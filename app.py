import nltk
from nltk.chat.util import Chat,reflections

from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    query=request.args.get('query')
    print(query)
    ques1=r'how are you'
    answer1=[
    'all well',
    'I am good',
    'awesome'
    ]
    ques2=r'what can you do'
    answer2=[
    'I can reply to your queries',
    'I am here to answer your questions',
    'I can chat with you'
    ]
    ques3=r'(.*) is your name'
    answer3=[
    'my name is chatty',
    'I am chatty'
    ]
    ques4=r'(.*)mausam(.*)baarish'
    answer4=[
    'it looks it will rain today',
    'aaj mausam bahut beiman hai bada'
    ]
#Question answer pairs
    qa_pair=[
    (ques1,answer1),
    (ques2,answer2),
    (ques3,answer3),
    (ques4,answer4)
    ]
    chatbot=Chat(qa_pair)
    if query != None:
        response=chatbot.respond(query)
        print(response)
       
    else:
        response=''
     
    return render_template('index.html',result=response)

@app.route('/chatbot')
def chat():
    return"<h2>Chat Bot</h2>"

app.run(debug=True)