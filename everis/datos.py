import numpy as np

array = [17,5,45,195,77,31,1,81,1,151,9,11,15,157,105,25,101,155,183,17,
99,99,199,81,35,163,37,115,121,175,35,81,197,87,139,97,9,113,125,1,
163,99,63,147,111,159,29,59,187,143,81,135,107,177,61,7,99,27,73,131,
105,141,191,47,9,121,23,85,139,49,137,113,3,65,113,143,75,5,73,183,
45,63,33,143,103,135,127,179,83,185,73,109,45,81,81,57,133,67,27,161,
49,95,65,121,199,7,91,5,89,151,67,107,157,73,169,41,71,35,25,101,
65,197,163,57,129,47,135,21,53,77,81,135,119,109,141,133,37,77,129,141,
135,53,41,137,5,125,25,41,191,127,189,79,127,17,81,183,133,99,189,43,
49,111,117,11,133,147,199,53,195,35,157,157,193,167,29,177,69,179,127,145,
43,73,47,19,151,1,153,89,41,91,71,29,1,123,67,195,69,63,67,191,
157,35,107,57,45,151,63,135,31,189,7,161,9,125,33,29,19,107,113,185,
33,79,11,85,193,71,63,95,111,117,177,49,1,35,109,49,73,59,171,115,
173,113,1,97,71,143,179,15,11,89,89,75,89,121,43,117,103,109,35,117,
39,161,163,137,11,189,95,139,57,147,185,27,173,105,35,155,9,179,111,81,
9,105,17,167,195,71,199,33,15,195,115,65,33,53,53,159,67,55,197,133,
177,73,137,175,115,125,41,145,7,93,67,135,93,111,25,65,127,187,107,139,
9,85,33,147,77,51,79,23,49,189,145,37,17,93,59,65,81,125,153,73,
41,139,73,83,145,61,47,177,69,125,199,139,165,135,119,171,149,9,73,33,
41,147,71,59,157,63,181,3,149,63,99,143,97,173,163,33,47,115,11,109,
3,141,109,143,167,103,109,139,33,185,67,97,123,87,105,3,179,39,135,97]





campo = np.reshape(array,[20,20])
maximo = float('-inf')
for i in range(np.shape(campo)[0]):
    for j in range(np.shape(campo)[1]):
        colecta_abajo = campo[i,j]
        colecta_arriba = campo[i,j]
        colecta_derecha = campo[i,j]
        colecta_izquierda = campo[i,j]
        colecta_diagonal_inferior_derecha = campo[i,j]
        colecta_diagonal_inferior_izquierda = campo[i,j]
        colecta_diagonal_superior_derecha = campo[i,j]
        colecta_diagonal_superior_izquierda = campo[i,j]
        
        if(i >= 3):
            colecta_izquierda += campo[i-1,j]+ campo[i-2,j] + campo[i-3,j]
            if(j >= 3):
                colecta_diagonal_superior_izquierda += campo[i-1,j-1]+ campo[i-2,j-2] + campo[i-3,j-3]
            if(j <= np.shape(campo)[1]-4):
                colecta_diagonal_superior_derecha += campo[i-1,j+1]+ campo[i-2,j+2] + campo[i-3,j+3]
        if(i <= 16):
            colecta_derecha += campo[i+1,j]+ campo[i+2,j] + campo[i+3,j]
            if(j >= 3):
                colecta_diagonal_inferior_izquierda += campo[i+1,j-1]+ campo[i+2,j-2] + campo[i+3,j-3]
            if(j <= np.shape(campo)[1]-4 ):
                colecta_diagonal_inferior_derecha += campo[i+1,j+1]+ campo[i+2,j+2] + campo[i+3,j+3]
        if(j >= 3):
            colecta_arriba += campo[i,j-1]+ campo[i,j-2] + campo[i,j-3]
        if(j <= 16):
            colecta_abajo += campo[i,j+1]+ campo[i,j+2] + campo[i,j+3]
        maximo = max(set([maximo,colecta_abajo,colecta_arriba,colecta_derecha,colecta_izquierda,colecta_diagonal_inferior_derecha,colecta_diagonal_inferior_izquierda,colecta_diagonal_superior_derecha,colecta_diagonal_superior_izquierda]))
print(maximo)


