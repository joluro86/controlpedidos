import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP y credenciales
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
smtp_username = 'joluro86@hotmail.com'
smtp_password = 'CASInunca86++'

# Información del remitente y destinatario
remitente = 'joluro86@hotmail.com'
destinatario = 'jorge.rodriguezj@udea.edu.co'

# Crear el objeto del mensaje
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = 'Asunto del correo'

# Cuerpo del mensaje
cuerpo = '¡Hola! Este es el cuerpo del correo.'
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Enviar el correo electrónico
with smtplib.SMTP(smtp_server, smtp_port) as servidor:
    servidor.starttls()
    servidor.login(smtp_username, smtp_password)
    servidor.send_message(mensaje)

print('Correo electrónico enviado exitosamente.')
