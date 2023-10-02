from flask import Flask, jsonify, request
from flask_cors import CORS
import kGraph

my_graph = kGraph.get_data()

app = Flask(__name__)
CORS(app)

questions = [
    {
        'id': 1,
        'book': 'Rainha Vermelha',
        'question': 'Quais são os sangues novos?',
        'answer': 'answer'
    },
    {
        'id': 2,
        'book': 'Rainha Vermelha',
        'question': 'Quais personagens tem irmãos?',
        'answer': 'answer'
    },
    {
        'id': 3,
        'book': 'Rainha Vermelha',
        'question': 'Quantos personagens têm no livro?',
        'answer': 'answer'
    },
    {
        'id': 4,
        'book': 'Rainha Vermelha',
        'question': 'Quais poderes têm no livro?',
        'answer': 'answer'
    },
    {
        'id': 5,
        'book': 'Rainha Vermelha',
        'question': 'Qual poder da família do rei?',
        'answer': 'answer'
    },
    {
        'id': 6,
        'book': 'Rainha Vermelha',
        'question': 'Qual família a Evangeline pertence?',
        'answer': 'answer'
    },
    {
        'id': 7,
        'book': 'Rainha Vermelha',
        'question': 'Qual família têm mais pessoas?',
        'answer': 'answer'
    },
    {
        'id': 8,
        'book': 'Rainha Vermelha',
        'question': 'Qual poder da Mare?',
        'answer': 'answer'
    },
    {
        'id': 9,
        'book': 'Rainha Vermelha',
        'question': 'Quais são os filhos do rei Tiberias?',
        'answer': 'answer'
    },
    {
        'id': 10,
        'book': 'Rainha Vermelha',
        'question': 'Quais tipos de sangue existe no livro?',
        'answer': 'answer'
    },
]
# Consultar(todos)
@app.route('/questions', methods=['GET'])
def get_questions():
    for key, value in my_graph.items():
        # Encontrar o dicionário correspondente em questions pelo valor da chave 'id'
        question = next((q for q in questions if q['id'] == key), None)
        
        # Se encontrar o dicionário, atualizar o valor da chave 'answer'
        if question:
            question['answer'] = value
    for q in questions:
        print(q)
    return jsonify(questions)

# Consultar(id)
@app.route('/questions/<int:id>',methods=['GET'])
def get_question_by_id(id):
    for question in questions:
        if question.get('id') == id:
            return jsonify(question)
            
# Editar
@app.route('/questions/<int:id>',methods=['PUT'])
def edit_question_by_id(id):
    modified_question = request.get_json()
    for index, question in enumerate(questions):
        if question.get('id') == id:
            questions[index].update(modified_question)
            return jsonify(questions[index])

# Criar
@app.route('/questions',methods=['POST'])
def add_new_question():
    new_question = request.get_json()
    questions.append(new_question)
    
    return jsonify(questions)

# Excluir
@app.route('/questions/<int:id>',methods=['DELETE'])
def delete_question(id):
    for index, question in enumerate(questions):
        if question.get('id') == id:
            del questions[index]

    return jsonify(questions)

app.run(port=5000, host='localhost', debug=True)