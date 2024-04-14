from flask import Flask, render_template, request, url_for, redirect


app= Flask(__name__) #Se inicializa la aplicación


@app.route('/')
def index():
    #return "Hola" 
    
    data ={
        'titulo': 'Index',
        'bienvenida': 'Ingresa tus resultados en las Pruebas Saber 2022',
    }
    return render_template('index.html', data = data) #Retornar una plantilla html

@app.route('/index2')
def index2():
    #return "Hola" 

    return render_template('index2.html') #Retornar una plantilla html


############################################################################

@app.route('/promedio', methods=['POST'])
def promedio():
    # Obtener los datos enviados por el formulario
    formulario1 = float(request.form['formulario1'])
    formulario2 = float(request.form['formulario2'])
    formulario3 = float(request.form['formulario3'])
    formulario4 = float(request.form['formulario4'])
    formulario5 = float(request.form['formulario5'])
    formulario6 = float(request.form['formulario6'])

    # Inicializar result_soc con un valor predeterminado

    if formulario6 >= 347.60 or formulario6 >= 296.72:
        result_glo = "Se encuentra en un nivel superior"
        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)

    elif formulario6 >= 293.53 or formulario6 >= 264.66:
        result_glo = "Se encuentra en un nivel alto"
        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)
    elif formulario6 >= 261.62 or formulario6 >= 227.69:
        result_glo = "Se encuentra en un nivel medio"
        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)
    elif formulario6 >= 225.26 or formulario6 >= 184.5:
        result_glo = "Se encuentra en un nivel bajo"
        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)

    else:
        result_glo = "Se encuentra en un nivel bajo"
        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)


    # Retornar el resultado a la plantilla HTML
    return render_template('resultado.html', resultado=result_glo, resultado2=result_soc, resultado3=result_mat, resultado4=result_LectC, resultado5=result_Ing, resultado6=result_CN, formulario1=formulario1, 
                           formulario2=formulario2, formulario3=formulario3, formulario4=formulario4, formulario5=formulario5, formulario6=formulario6)

def determinar_nivel_social(puntajeSoc):
        if puntajeSoc >= 66.73 or puntajeSoc >= 56.69:
            return "Se encuentra en un nivel superior"
        elif puntajeSoc >= 63 or puntajeSoc >= 43:
            return "Se encuentra en un nivel alto"
        elif puntajeSoc >= 51.45 or puntajeSoc >= 39.5:
            return "Se encuentra en un nivel medio"
        elif puntajeSoc >= 46.5 or puntajeSoc >= 32:
            return "Se encuentra en un nivel bajo"
        else:
            return "Se encuentra en un nivel bajo"
        
def determinar_nivel_matematicas(puntajeMat):
        
        if puntajeMat >= 71.57 or puntajeMat >= 57:
            return "Se encuentra en un nivel superior"
        elif puntajeMat >= 60 or puntajeMat >= 54.25:
            return "Se encuentra en un nivel alto"
        elif puntajeMat >= 57 or puntajeMat >= 45:
            return "Se encuentra en un nivel medio"
        elif puntajeMat >= 49 or puntajeMat >= 34.83:
            return "Se encuentra en un nivel bajo"
        else:
            return "Se encuentra en un nivel bajo"

def determinar_nivel_LectCri(puntajeLect):
        if puntajeLect >= 71.05 or puntajeLect >= 53:
            return "Se encuentra en un nivel superior"
        elif puntajeLect >= 61.5 or puntajeLect >= 50:
            return "Se encuentra en un nivel alto "
        elif puntajeLect >= 59 or puntajeLect >= 44:
            return "Se encuentra en un nivel medio "
        elif puntajeLect >= 54 or puntajeLect >= 31:
            return "Se encuentra en un nivel bajo "
        else:
            return "Se encuentra en un nivel bajo "

def determinar_nivel_Ingles(puntajeIngl):
        if puntajeIngl >= 79 or puntajeIngl >= 59.69:
            return "Se encuentra en un nivel superior "
        elif puntajeIngl >= 62.63 or puntajeIngl >= 44:
            return "Se encuentra en un nivel alto "
        elif puntajeIngl >= 58 or puntajeIngl >= 39:
            return "Se encuentra en un nivel medio "
        elif puntajeIngl >= 49 or puntajeIngl >= 32:
            return "Se encuentra en un nivel bajo "
        else:
            return "Se encuentra en un nivel bajo "

def determinar_nivel_CNatura(puntajeNatu):
        if puntajeNatu >= 69 or puntajeNatu >= 57:
            return "Se encuentra en un nivel superior "
        elif puntajeNatu >= 58 or puntajeNatu >= 48.83:
            return "Se encuentra en un nivel alto "
        elif puntajeNatu >= 60 or puntajeNatu >= 39:
            return "Se encuentra en un nivel medio "
        elif puntajeNatu >= 47 or puntajeNatu >= 36:
            return "Se encuentra en un nivel bajo "
        else:
            return "Se encuentra en un nivel bajo "

############################################################################
    

if __name__ == '__main__': #Si esta desde el main, entonces se corre el pograma
    app.run(debug=True)