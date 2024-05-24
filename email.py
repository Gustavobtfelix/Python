import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import Info
import Index
#por questões de segurança e organização crie suas informações e o Index em arquivos separados
def enviaEmail():
    email = Info.Email #Usuario
    password = Info.Password #senha do usuario
    send_to_email = Info.sendTo # ['email1', 'email2', 'email3']
    subject = Info.subject #"titulo do e-mail"
    message = Index.mensagemPassback #html
    message = message.replace('NOME', Info.NOME)
    message = message.replace('QUANTIDADE', Info.QUANTIDADE)
    cc = Info.ccEmail #['email1', 'email2', 'email3']
    
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