import math

#Interfaz

while True:
        print (" ")
        print ("Bienvenido al Banco \n\
    Que deseas hacer?\n\
    1.- Solicitar un prestamo\n\
    2.- Imprimir tabla de amortizacion\n\
    3.- Pagar el prestamo\n\
    4.- Cancelacion de Prestamos\n\
    5.- Consulta de prestamo \n ")

        print ("    Mas opciones... \n\
    6.Imprimir estado de cuenta del prestamo \n\
    7.Historial de Pago \n\
    ")
        opcion=int(input("Seleccione una opcion: "))

        #Solicitud de prestamo
        if opcion==1:   
            prestamo = float(input("Digite el monto del prestamo?"))
            tiempo = int(input("Plazo de prestamo (meses)?"))
            interesAnual = float(input("Interes anual a aplicar al prestamo?"))
        #Interes Mensual
        interesMensual = (interesAnual/12)/100
        #Cuota
        cuota = ((prestamo*interesMensual)/(1-(math.pow((1+interesMensual),(tiempo*-1)))))

        #Tabla de Amortizacion
        if opcion==2:
            print(" ")
            print("                     Tabla de Amortizacion")
            print(" ")
            print("     Interes Anual: ",interesAnual,"%","\t\t","Monto: $", prestamo)
            print("         Plazo meses: ", tiempo)
            print("")
            print("{:^10}{:^10}{:^12}{:^10}{:^10}".format("N0Ã‚Â°","Cuota","Interes","Amortizacion","Saldo"))
            nuevoSaldo = prestamo
            for i in range(tiempo+1):
                if(i==0):
                    print("{:^10}{:^10}{:^12}{:^10}".format(i," "," "," ",prestamo))
                else:
                    pagoInteres = nuevoSaldo*interesMensual
                    amorzacion= cuota-pagoInteres
                    nuevoSaldo = nuevoSaldo-amorzacion
                    print("{:^10d}{:^10.2f}{:^10.2f}{:^12.2f}{:^10.2f}".format(i,cuota,pagoInteres,amorzacion,nuevoSaldo))
        
        #Pago de prestamo
        if opcion==3:
            print("Tu pago de este mes es de: ", cuota)
            opt = input("Deseas saldar la cuota de este mes? (si/no)")

            if opt == ("si"):
                print("La deuda de este mes fue saldada")

            if opt == ("no"):
                print("La deuda de este mes no fue saldada")

        #Cancelar el prestamo
        if opcion==4:
            print("Para cancelar el prestamo debes pagar:", prestamo)
            opt = input("Deseas cancelar el prestamo? (si/no)")

            if opt == ("si"):
                print("El prestamo fue cancelado exitosamente")
                prestamo = 0
                tiempo = 0
                interesAnual= 0

                quit()

            if opt == ("no"):
                print("El prestamo no pudo ser cancelado")



        #Consulta de Clientes
        if opcion==5:
            print("De cuanta es mi deuda?")
            print(prestamo)
            print("De cuanta es mi deuda del mes?")
            print(cuota)
            print("De cuanto es el plazo del prestamo?")
            print(tiempo)
            print("De cuanto es el interes anual")
            print(interesAnual)
            print("De cuanto es el interes mensual")
            print(interesMensual)

        #Estado de cuenta del prestamo
        if opcion==6:
            print(" ")
            print("                     Estado de cuenta")
            print(" ")
            print("     Interes Anual: ",interesAnual,"%","\t\t","Monto: $", prestamo)
            print("         Plazo meses: ", tiempo)
            print("")
            print("{:^10}{:^10}{:^10}{:^10}".format("N0Ã‚Â°","Cuota","Interes","Saldo"))
            nuevoSaldo = prestamo
            for i in range(tiempo+1):
                if(i==0):
                    print("{:^10}{:^10}{:^12}{:^10}".format(i," "," "," ",prestamo))
                else:
                    pagoInteres = nuevoSaldo*interesMensual
                    amorzacion= cuota-pagoInteres
                    nuevoSaldo = nuevoSaldo-amorzacion
                    print("{:^10d}{:^10.2f}{:^10.2f}{:^10.2f}".format(i,cuota,pagoInteres,nuevoSaldo))
        

        #Historial de Pago
        if opcion==7:   
        
            mensualidad = cuota
            total=0
        
            x = tiempo
        
            for i in range(x):
                print("El pago de la mensualidad" + str(i+1) + "es: " + str(mensualidad))
                total+=mensualidad
                mensualidad*=2
                print("El pago total es de: " + str(total)) 