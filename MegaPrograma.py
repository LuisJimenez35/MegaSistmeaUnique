from email.message import EmailMessage
import smtplib
import pymysql
import random
#Sistema de Bienvenida
print("Bienvenido al sistema de usuario")
#Base de datos (Prototipo)
listcorreos = ["Year@gmail.com" , "luis34@gmail.com"]
listpass = ["1224" , "1234"]
#Registrarse y Iniciar Sesion
vueltatotal = 1
while vueltatotal == 1:
    rootmen = int(input("1=Registrarse\n2=Iniciar Secion\n"))
    if rootmen == 1:
        vueltas = 0 
        while vueltas == 0:
            print("Registrar Usuario")
            regcor = input("Digte un Correo:")
            regpass = input("Digite la nueva password: ")
            if "@" in regcor:
                if regcor in listcorreos:
                    print("Debe Ingresar un Correo distinto")
                    vueltas = 0
                else:
                    if regpass in listpass:
                        print("Debe Ingresar una Contraseña distinta")
                    else:
                        listcorreos.append(regcor)
                        listpass.append(regpass)
                        vueltatotal = 1
                        vueltas = 1
                        print("Usuario Nuevo Registrado")
            else:
                print("El correo debe contener un @ dentro")
    if rootmen == 2:
        v = 3
        while v > 0:
            print("Inicio de sesion\n")
            gmail = input("Digite su correo: ")
            passw = input("Digite su password: ")
            if gmail in listcorreos and passw in listpass:
                print("Correo y password correctos\nIngresando al sistema\n")
                #Menu Principal
                mo = "S"
                while mo.upper() == "S":
                    menu=int(input("Menu\n1=Mensaje bonito\n2=Mega Calculadora\n"))
                    #Mensaje Bonito
                    if menu == 1:
                        print("Pinche estupido ten una linda semana UwU")
                    #Calculadora Repetitiva
                    elif menu == 2:
                        op = "S"
                        while op.upper() == "S":
                            print("Bienvenido al sistema de calculadora super chafa")
                            n1 = int(input("Digite el primer numero "))
                            n2 = int(input("Digite el primer numero "))
                            opcion = input("Digite una de las siguientes opciones :\n S=Suma \n R=Resta \n M=Multiplicacion \n D=Division \n (Puede digitar en minsucula o mayusucula)\n")
                            if opcion.upper()=="S":
                                print("La suma de",n1,"y",n2,"es:",n1+n2)
                            elif opcion.upper()=="R":
                                print("La resta de",n1,"y",n2,"es:",n1-n2)
                            elif opcion.upper()=="M":
                                print("La multiplicacion de",n1,"y",n2,"es:",n1*n2)
                            elif opcion.upper()=="D":
                                float(n1)
                                float(n2)
                                print("La division de",n1,"y",n2,"es:",n1/n2)
                            op = input("Desea Repetir otra operacion?\nSi=S\nNo=N\n")
                        print("Cerrando el programa")
            #Menu Administrador
            elif passw == "Admin123":
                adm = 1
                while adm == 1:
                    print("Bienvenido al sistema de administracion que desea hacer?")
                    admin=int(input("\n1=Ver los datos de usuarios\n2=Eliminar Usuario\n3=Mandar un correo de soporte\n"))
                    if admin == 1:
                        miConexion = pymysql.connect( host='localhost', user= 'root', passwd='Halobat17.', db='users' )
                        cur = miConexion.cursor()
                        cur.execute( "SELECT Usuario, Correo ,Pass FROM usuarios" )
                        print("Usuarios dosponibles:\n")
                        for Usuario, Correo, Pass in cur.fetchall() :
                            print("\nId:",Usuario, "\nCorreo:",Correo, "\nPassword:",Pass)
                        adm = 1
                    elif admin== 2:
                        print("Eliminar Usuario")
                        adm = 1
                    elif admin == 3:
                        print("Mandar un correo de soporte")
                        remitente = "luismorajimenez35@gmail.com"
                        destinatario=input("Digite el correo al cual enviar el msj: ")
                        mensaje = input("Digite el mensaje a enviar: ")
                        email = EmailMessage()
                        email["From"] = remitente
                        email["To"] = destinatario
                        email["Subject"] = "Correo se Soporte de Megaproyecto de Prime"
                        email.set_content(mensaje)
                        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
                        smtp.login(remitente, "fcvjqpolkfqrqnod")
                        smtp.sendmail(remitente, destinatario, email.as_string())
                        print("Correo enviado con exito")
                        adm = 1
                    elif admin > 3:
                        ah=int(input("\nOpcion Incorrecta\nDesea volver al menu de administracion?\n1=Si\n2=No\n"))
                        if ah==1:
                            adm=1
                        else:
                            adm = 2
                            v= 3
            else:
                v = v-1
                print("Correo y password no encontrados ,le quedan",v,"intentos")
                recover=input("Olvido su Contraseña?\nS=Si\nN=No\n ")
                if recover == "S":
                    codver = ['Y123', 'Q3456', 'IL24323', 'P353']
                    for i in range(1):
                        ul=(random.choice(codver))
                    remitente = "luismorajimenez35@gmail.com"
                    destinatario= input("Digite el correo al que quiere que se le envie el soporte: ")
                    mensaje = ("Digite este codigo para ver su contraseña anterior: "+ul)
                    email = EmailMessage()
                    email["From"] = remitente
                    email["To"] = destinatario
                    email["Subject"] = "Correo de Recuperacion de Contraseña"
                    email.set_content(mensaje)
                    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
                    smtp.login(remitente, "fcvjqpolkfqrqnod")
                    smtp.sendmail(remitente, destinatario, email.as_string())
                    print("Revise su bandeja de entrada")
                    cod= input("Digite el codigo que se le envio a su bandeja de entrada: ")
                    if cod == ul :
                        print("Su contraseña anterior era :",regpass)
                        v=3
                    else:
                        print("Fallo del codigo , volviendo al sistema de Bienvenida....\n")
                        v=3
                else:
                    print("Volviendo al sistema")
        print("Desmasiados intentos fallidos \nCerrando el sistema.....")
        exit()
