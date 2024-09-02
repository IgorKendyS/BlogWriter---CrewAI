#!/usr/bin/env python
import sys
from blogwriter.crew import BlogwriterCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

#!/usr/bin/env python
import sys
from blogwriter.crew import BlogwriterCrew

def run():
    """
    Run the crew with dynamic input from the user for the article topic.
    """
    # Solicitar o assunto do artigo ao usuário
    assunto = input("Por favor, insira o assunto do artigo: ")

    # Configurar as entradas para o crew com base no assunto fornecido
    inputs = {
        'topic': assunto
    }
    
    try:
        # Inicializar o crew e executar com as entradas fornecidas
        crew_instance = BlogwriterCrew()
        result = crew_instance.crew().kickoff(inputs=inputs)
        
        # Salvar o resultado em um arquivo .txt
        with open('resultado_artigo.txt', 'w', encoding='utf-8') as file:
            file.write(str(result))

        print("Artigo salvo em 'resultado_artigo.txt'")
    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")




def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BlogwriterCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BlogwriterCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BlogwriterCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

if __name__ == "__main__":
    run()
