import smtplib
import pandas as pd
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_emails_blindado():
    # ================= SUAS CONFIGURAÇÕES =================
    MEU_EMAIL = "seu_email@gmail.com"
    MINHA_SENHA = "xxxx xxxx xxxx xxxx"  
    
    # Nome exato do arquivo que você enviou (deve estar na mesma pasta do script)
    NOME_DO_ARQUIVO = "deputado.xls"

    # Assunto do e-mail
    ASSUNTO = "Anistia Ampla GEral e Irrestrita Já"

    # ================= 1. CARREGAMENTO BLINDADO =================
    print("Lendo arquivo com motor Python (modo robusto)...")
    
    try:
        # --- O SEGREDO DO DATA SCIENCE ---
        # engine='python': Evita o erro de Buffer Overflow
        # sep=None: O Python detecta sozinho se é , ou ;
        # on_bad_lines='skip': Pula linhas defeituosas em vez de travar
        df = pd.read_csv(
            NOME_DO_ARQUIVO, 
            encoding='latin1', 
            sep=None, 
            engine='python', 
            on_bad_lines='skip'
        )
        
        # Limpeza básica dos nomes das colunas
        df.columns = df.columns.str.strip()
        print(f"Colunas detectadas: {df.columns.tolist()}")
        
        # Verifica se achou as colunas certas
        # Nota: Às vezes o CSV vem com nomes ligeiramente diferentes, ajustamos aqui
        if 'Correio Eletrônico' in df.columns:
            coluna_email = 'Correio Eletrônico'
        elif 'Email' in df.columns: # Tenta achar variações
            coluna_email = 'Email'
        else:
            print("ERRO: Não achei a coluna de E-mail. Verifique a lista de colunas acima.")
            return

        if 'Nome Parlamentar' in df.columns:
            coluna_nome = 'Nome Parlamentar'
        else:
            coluna_nome = df.columns[0] # Se não achar, pega a primeira coluna como nome

        # Filtra e limpa
        df_limpo = df.dropna(subset=[coluna_email])
        total = len(df_limpo)
        
        print(f"SUCESSO! Base carregada: {total} contatos válidos.")
        
    except FileNotFoundError:
        print(f"ERRO: Arquivo '{NOME_DO_ARQUIVO}' não encontrado.")
        return
    except Exception as e:
        print(f"Erro crítico na leitura: {e}")
        return

    # ================= 2. ENVIO =================
    try:
        print("-" * 30)
        print("Conectando ao Gmail...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(MEU_EMAIL, MINHA_SENHA)
        print("Login OK! Enviando...")

        contador = 0
        
        for index, linha in df_limpo.iterrows():
            nome = str(linha[coluna_nome]).strip()
            email_destino = str(linha[coluna_email]).strip()
            
            if "@" not in email_destino:
                continue

            # Montagem do E-mail
            corpo_mensagem = f"""
            Excelentíssimo(a) {nome_deputado},

            Escrevo para expressar meu firme posicionamento e solicitar seu voto favorável à proposta de Anistia no Brasil, que defendo que seja ampla, geral e irrestrita.

            É fundamental que esta Casa Legislativa promova a liberdade dos prisioneiros relacionados aos eventos de 8 de janeiro e lidere a luta pela plena liberdade em nosso país. 
            Conto com seu apoio para garantir a justiça e o bem-estar de todos os cidadãos.

            Agradeço a sua atenção e dedicação ao serviço público.

            Atenciosamente,
            
            """

            # Criando o e-mail
            msg = MIMEMultipart()
            msg['From'] = MEU_EMAIL
            msg['To'] = email_destino
            msg['Subject'] = ASSUNTO
            msg.attach(MIMEText(corpo_mensagem, 'plain'))

            try:
                server.sendmail(MEU_EMAIL, email_destino, msg.as_string())
                contador += 1
                print(f"[{contador}/{total}] Enviado: {nome}")
                time.sleep(3) # Pausa de segurança
            except Exception as e:
                print(f"Falha no envio para {nome}: {e}")

        server.quit()
        print("Processo finalizado!")

    except Exception as e:
        print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    enviar_emails_blindado()