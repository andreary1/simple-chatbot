import os
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader
from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup

os.environ.setdefault("GROQ_API_KEY", "SUA_CHAVE_API")

chat = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

def carregar_sites():
    url_site = input("digite a url do site que deseja observar: ")
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carregar_PDFs():
    caminho_str = input("Digite o caminho completo do PDF: ").strip()
    caminho = Path(caminho_str).expanduser().resolve()
    if not caminho.exists() or caminho.suffix.lower() != ".pdf":
        print("Caminho inválido ou arquivo não é PDF.")
        return ""
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carregar_videos_yt():
    url_video = input("digite a url do vídeo que deseja observar: ")
    loader = YoutubeLoader(url_video, language=['pt'])
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    documento = ''
    return documento

def resposta_bot(mensagens, documento):
    mensagem_sistema = '''Você é um assistente virtual amigável que utiliza as seguintes informações para formular as 
    suas respostas: {informacoes}'''
    mensagens_modelo = [('system', mensagem_sistema)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content

print("Bem vindo ao chatbot! Em que posso ajudar?")
while True:
    selecao = input("1 - analisar site\n2 - analisar PDF\n3 - analisar vídeo\n4 - sair\n")
    match selecao:
        case '1':
            documento = carregar_sites()
            break
        case '2':
            documento = carregar_PDFs()
            break
        case '3':
            documento = carregar_videos_yt()
            break
        case '4':
            break
        case _:
            print("Por favor, digite um valor válido!")


mensagens = []
while True:
    pergunta = input(f"Usuário (digite x se quiser sair): ")
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f"Bot: {resposta}")

print("obrigado por usar o chatbot!")