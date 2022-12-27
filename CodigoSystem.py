import random
from email.message import EmailMessage
import smtplib
import pymysql

listcorreos = ["Year@gmail.com" , "luis34@gmail.com"]
listpass = ["1224" , "1234"]

liststudentsid = []
liststudentsname = []
liststudentsapell = []
liststudentsgrade = []

#Sistema de Bienvenida
print("Bienvenido al sistema")

#Registrarse y Iniciar Sesion
vueltatotal = 1
while vueltatotal == 1:
    rootmen = int(input("1=Registrarse\n2=Iniciar Secion\n3=Cerrar Sistema\n"))
    if rootmen == 1:
        vueltas = 0
        while vueltas == 0:
            print("Registrar Usuario")
            regcor = input("Digte un Correo:")
            regpass = input("Digite la nueva password: ")
            if "@" in regcor and "." in regcor:
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
                print("El correo debe contener un @ o un . dentro")
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
                    menu=int(input("Menu\n1=\n2=\n"))
                    #Mensaje Bonito
                    if menu == 1:
                        print("Pinche estupido ten una linda semana UwU")
                    #Calculadora Repetitiva
                    elif menu == 2:
                        print("Hola")
            #Menu Administrador
            elif passw == "Admin123":
                adm = 1
                while adm == 1:
                    print("Bienvenido al sistema de administracion que desea hacer?")
                    admin=int(input("\n1=Ver los datos de usuarios\n2=Eliminar Usuario\n3=Mandar un correo de soporte\n4=Volver al Inicio de Secion\n"))
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
                        rc = 3
                        while rc == 3:
                            print("Mandar un correo de soporte")
                            remitente = "soportprimeprogram@gmail.com"
                            destinatario=input("Digite el correo al cual enviar el msj: ")
                            if "@" in destinatario and "." in destinatario:
                                mensaje = input("Digite el mensaje a enviar: ")
                                email = EmailMessage()
                                email["From"] = remitente
                                email["To"] = destinatario
                                email["Subject"] = "Correo se Soporte de Megaproyecto de Prime"
                                email.set_content(mensaje)
                                smtp = smtplib.SMTP_SSL("smtp.gmail.com")
                                smtp.login(remitente, "gbaabtuzmxgxrvhn")
                                smtp.sendmail(remitente, destinatario, email.as_string())
                                print("Correo enviado con exito")
                                adm = 1
                                rc = 1
                            else:
                                print("Digite un correo valido")
                                rec = 3
                    elif admin == 4:
                        print("Volviendo al Sistema")
                        adm = 2
                        v= 3
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
                    codver = ['Y123L', 'Q3456R', 'IL24323', 'P353JU03', "IUTFDR0"]
                    for i in range(1):
                        ul=(random.choice(codver))
                    pc = 3
                    while pc == 3:
                        remitente = "soportprimeprogram@gmail.com"
                        destinatario= input("Digite el correo al que quiere que se le envie el soporte: ")
                        if "@" in destinatario and "." in destinatario:
                            mensaje = ("Digite este codigo para ver su contraseña anterior: "+ul)
                            email = EmailMessage()
                            email["From"] = remitente
                            email["To"] = destinatario
                            email["Subject"] = "Correo de Recuperacion de Contraseña"
                            email.set_content(mensaje)
                            smtp = smtplib.SMTP_SSL("smtp.gmail.com")
                            smtp.login(remitente, "gbaabtuzmxgxrvhn")
                            smtp.sendmail(remitente, destinatario, email.as_string())
                            print("Revise su bandeja de entrada")
                            cod= input("Digite el codigo que se le envio a su bandeja de entrada: ")
                            if cod == ul :
                                vver = 3
                                print("Codigo Aceptado\n")
                                while vver ==3:
                                    newpass=input("Digite la nueva password: ")
                                    if newpass in listpass:
                                        print("Digite una password distinta")
                                        vver == 3
                                    elif newpass not in listpass:
                                        if newpass == regpass:
                                            listpass.append(newpass)
                                            listpass.pop(regpass)
                                            print("Pass anterior eliminada\nLa nueva Pass se agrego correctamente")
                                            v=3
                                        else:
                                            listpass.append(newpass)
                                            print("Pass anterior eliminada\nLa nueva Pass se agrego correctamente")
                                            v=3
                            else:
                                print("Fallo del codigo , volviendo al sistema de Bienvenida....\n")
                                v=3
                        else:
                            print("Digite un correo valido")
                            pc = 3
                else:
                    print("Volviendo al sistema")
    if rootmen == 3:
        print("Cerrando Sistema\nGracias por su estadia")
        exit()
    else:
        print("Digite una opcion correcta")
        vueltatotal = 1
print("Desmasiados intentos fallidos \nCerrando el sistema.....")
exit()
