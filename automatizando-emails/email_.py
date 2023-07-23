from email.message import EmailMessage
import ssl
import smtplib
import mimetypes
import os
from imbox import Imbox
from datetime import datetime
import pandas as pd


email_senha = open('pass', 'r').read()
email_origem = 'conta_email@email.com'
email_destino = 'email_destino@email.com'

# podemos usar um arquivo HTML também
assunto = 'texto'
body_email = open('corpo_email.txt', 'r').read()

# vamos organizar o email para enviar ao SMTP
mensagem = EmailMessage()
mensagem['From'] = email_origem
mensagem['To'] = email_destino
mensagem['Subject'] = assunto

mensagem.set_content(body_email) # para arquivo normal
mensagem.set_content(body_email, subtype='html') # para arquivo html estilizado
safe = ssl.create_default_context()

#enviando anexos
# lembrando que o corpo tem que ser criando antes da formatação da imagem
imagem = 'imagem.png'
mime_type, mime_subtype = mimetypes.guess_type(imagem)[0].split('/')
with open(imagem, 'rb') as ap:
    mensagem.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename = imagem)


# aqui abrimos a conexão com with
with smtplib.SMTP_SSL('aqui vai o servidor', 'porta', context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
    
# ler e-mails
# necessário o pip install imbox
username = 'email@email.com'
password = 'password'

host = 'servidor do email'

mail = Imbox(host, username=username, password=password, ssl=True)

#carregando todas as emails do email, tem vários filtros, verificar a documentação do Imbox
messages = mail.messages()

#lendo uma mensagem
for (uid, message) in messages:
    message.subject
    message.body
    message.sent_from
    message.sent_to
    message.headers
    message.date
    if len(message.attachments) > 0:
        for attach in message.attachments:
            file = open('attachment/arquivo.pdf', 'wb')
            # jogamos o ponteiro do python para o inicio do script
            attach['content'].seek(0)
            file.write(attach['content'].read())
            file.close()
    break
