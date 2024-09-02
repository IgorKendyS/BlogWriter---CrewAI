from crewai_tools import BaseTool
from crewai_tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Inicializando o wrapper da API do Wikipedia

@tool
class MyCustomTool(BaseTool):
    """
    MyCustomTool é uma ferramenta personalizada que utiliza o mecanismo de pesquisa DuckDuckGo para
    realizar buscas rápidas na web com base no argumento fornecido. É útil para encontrar informações
    rapidamente sem a necessidade de especificar um local ou tipo de pesquisa específico.
    """
    name: str = "my_custom_tool"
    description: str = (
        "Ferramenta personalizada que utiliza DuckDuckGo para fazer uma pesquisa rápida."
    )

    def _run(self, argument: str) -> str:
        """
        Executa uma pesquisa rápida usando o DuckDuckGo com base no argumento fornecido.

        Parâmetros:
        - argument (str): O termo de pesquisa para o qual executar a busca.

        Retorno:
        - str: Resultados da pesquisa retornados pela ferramenta DuckDuckGo.
        """
        search_tool = DuckDuckGoSearchRun()
        result = search_tool.run(argument)  # Faz uma pesquisa usando o termo fornecido em 'argument'
        return result
