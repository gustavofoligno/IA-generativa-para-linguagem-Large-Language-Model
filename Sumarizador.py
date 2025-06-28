import streamlit as st
from transformers import pipeline

# Título e descrição
st.set_page_config(
    page_title="Sumarizador (Hugging Face)", layout="centered")
st.title("📄 Sumarizador com Hugging Face")
st.write("Este app utiliza o modelo padrão da Hugging Face para gerar um resumo.")

# Entrada do texto
texto = st.text_area("Insira o texto a ser resumido:", height=300)

# Upload de arquivo
arquivo = st.file_uploader("Ou envie um arquivo .txt", type="txt")
if arquivo:
    texto = arquivo.read().decode("utf-8")

# Botão para gerar resumo
if st.button("Gerar Resumo"):
    if not texto.strip():
        st.warning("Por favor, insira um texto.")
    else:
        with st.spinner("Gerando resumo com modelo padrão da Hugging Face..."):
            summarizer = pipeline("summarization")
            # truncar para evitar erro de tamanho
            texto_truncado = texto.strip().replace("\n", " ")[:1024]
            resultado = summarizer(
                texto_truncado, max_length=130, min_length=30, do_sample=False)
            resumo = resultado[0]['summary_text']

        st.success("Resumo gerado!")
        st.text_area("Resumo", resumo, height=200)
