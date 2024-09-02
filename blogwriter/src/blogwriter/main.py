from flask import Flask, request, jsonify
from blogwriter.crew import BlogwriterCrew

app = Flask(__name__)

@app.route('/generate_article', methods=['POST'])
def generate_article():
    try:
        # Pega o 'topic' do corpo da requisição POST
        data = request.get_json()
        topic = data.get('topic')

        if not topic:
            return jsonify({"error": "Por favor, forneça um tópico no campo 'topic'."}), 400

        # Configura as entradas para o crew com base no tópico fornecido
        inputs = {
            'topic': topic
        }

        # Inicializa o crew e executa com as entradas fornecidas
        crew_instance = BlogwriterCrew()
        result = crew_instance.crew().kickoff(inputs=inputs)

        # Retorna o resultado como resposta JSON
        return jsonify({"result": str(result)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
