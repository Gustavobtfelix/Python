import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import Info
import Index
#por questões de segurança e organização crie suas informações e o Index em arquivos separados
def enviaEmail():
    email = Info.Email
    password = Info.Password
    send_to_email = Info.sendTo
    subject = Info.subject
    message = Index.mensagemPassback
    message = message.replace('NOME', Info.NOME)
    message = message.replace('QUANTIDADE', Info.QUANTIDADE)
    cc = Info.ccEmail
    
    #criando instancia
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = ",".join(send_to_email)
    msg['Subject'] = subject
    msg['Cc'] = cc
    msg.add_header('reply-to', Info.ccEmail)
    
    #attach the message using a Mimetext object while declaring it as plain text
    msg.attach(MIMEText(message, 'html'))
    
    #cria conexão com Google smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    try:
        server.sendmail(email, send_to_email, text)
        server.quit()
        print("\tmensagem enviada")
    except:
        print("\temail não enviado para o colaborador {}".format(Info.NOME))
    

if(__name__ == "__main__"):
    enviaEmail()