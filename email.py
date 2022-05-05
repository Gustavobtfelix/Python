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
    
    #criando instancia
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    
    #attach the message using a Mimetext object while declaring it as plain text
    msg.attach(MIMEText(message, 'html'))
    
    #cria conexão com Google smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    
    print("mensagem enviada")
    

if(__name__ == "__main__"):
    enviaEmail()