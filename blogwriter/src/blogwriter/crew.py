from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.tools import DuckDuckGoSearchRun
from .tools.custom_tool import MyCustomTool

# Inicializar as ferramentas
search_tool = DuckDuckGoSearchRun()

@CrewBase
class BlogwriterCrew():
    """Blogwriter crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def agente_lider(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_lider'],
            verbose=True,
            tools=[]  # Sem ferramentas específicas, atua na coordenação
        )

    @agent
    def agente_planejador_de_conteudo(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_planejador_de_conteudo'],
            verbose=True,
            tools=[search_tool]  # Ferramentas de planejamento e pesquisa
        )

    @agent
    def estrategista_seo(self) -> Agent:
        return Agent(
            config=self.agents_config['estrategista_seo'],
            verbose=True,
            tools=[search_tool]  # Ferramentas de SEO e pesquisa rápida
        )

    @agent
    def escritor_de_conteudo(self) -> Agent:
        return Agent(
            config=self.agents_config['escritor_de_conteudo'],
            verbose=True,
            tools=[MyCustomTool]  # Ferramentas de escrita e suporte
        )

    @agent
    def revisor_qualidade_coerencia(self) -> Agent:
        return Agent(
            config=self.agents_config['revisor_qualidade_coerencia'],
            verbose=True
        )

    @agent
    def especialista_faq_dados_complementares(self) -> Agent:
        return Agent(
            config=self.agents_config['especialista_faq_dados_complementares'],
            verbose=True,
            tools=[search_tool]  # Ferramentas para FAQs e pesquisa rápida
        )

    @task
    def definir_parametros_task(self) -> Task:
        return Task(
            config=self.tasks_config['definir_parametros_task'],
        )

    @task
    def otimizacao_seo_task(self) -> Task:
        return Task(
            config=self.tasks_config['otimizacao_seo_task'],
        )

    @task
    def criacao_conteudo_task(self) -> Task:
        return Task(
            config=self.tasks_config['criacao_conteudo_task'],
        )

    @task
    def revisao_qualidade_task(self) -> Task:
        return Task(
            config=self.tasks_config['revisao_qualidade_task'],
        )

    @task
    def criacao_faq_task(self) -> Task:
        return Task(
            config=self.tasks_config['criacao_faq_task'],
        )

    @task
    def compilacao_revisao_final_task(self) -> Task:
        return Task(
            config=self.tasks_config['compilacao_revisao_final_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Blogwriter crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,  # Defines the order of task execution
            verbose=True
        )
