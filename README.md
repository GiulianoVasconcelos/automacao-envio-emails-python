# 📧 Automação de E-mails com Python

Este projeto é uma solução automatizada para envio de e-mails personalizados em massa, capaz de ler bases de dados complexas (CSV/Excel) e lidar com erros de codificação comuns em arquivos publicos.

## 🛠️ Tecnologias Usadas
* **Python 3.10+**
* **Pandas:** Para manipulação e limpeza de dados (Data Cleaning).
* **SMTPlib:** Para conexão segura com servidor de e-mail (Gmail).
* **Tratamento de Exceções:** Script contra erros de encoding (UTF-16/Latin1) e arquivos corrompidos.

## 🚀 Como funciona
1. O script identifica automaticamente o formato do arquivo de contatos (CSV ou Excel).
2. Realiza a limpeza dos dados (tratamento de valores nulos e espaços em branco).
3. Conecta ao servidor SMTP do Google de forma segura.
4. Envia e-mails personalizados ("Olá, [Nome]") com pausas estratégicas para evitar bloqueios de spam.

## 📦 Como usar
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
