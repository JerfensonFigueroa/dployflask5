
import pickle
import numpy as np
import streamlit as st


pkl_filename = "RandomForest3.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ['Si tiene enfermedad cardiaca','No tiene enfermedad cardiaca']

def prediccion(xin):
    print(xin)
    yout=model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'Tiene enfermedad cardiaca {}\n'.format(labels[y_out])
    return mensaje

def main():
    #Titulo
    html_temp = """
    <h1 style ="color:#181082; text-align:center;"> PREDICTOR CARDIACO # </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Lectura de datos 
    Datos = st.text_input("Ingrese los valores : ")


    #El boton de se us pra iniciar
    if st.button("predicción :"):
        x_in = list(np.float_((Datos.title().split('\t'))))
        x_in = np.asarray(x_in).reshape(1,13)
        print(x_in.shape)

        predictS = prediccion(x_in)
        st.success(predictS)

if __name__=='__main__':
    main()
    
