import numpy as np
import scipy.io
import pandas as pd
#import os

#Carpeta donde se ubica el script
script_path = "C:\\jactools\\anompytso\\"

mat_t = scipy.io.loadmat(script_path+'database\\TEMP_TOTAL_1991_2020_V2.mat');
mat_s = scipy.io.loadmat(script_path+'database\\PSAL_TOTAL_1991_2020_V2.mat');
mat_o = scipy.io.loadmat(script_path+'database\\MonthlyTSOClimatology.mat'); 
long = scipy.io.loadmat(script_path+'database\\lon.mat')['lon']
lati = scipy.io.loadmat(script_path+'database\\lat.mat')['lat']


#Calcular anomalia 
def anom(x,y,z,t,temp_v,sali_v,oxig_v):
    dept = mat_t['Zst']
    temp = mat_t['TEMP_monthly']
    sali = mat_s['PSAL_monthly']
    oxig = mat_o['oxygen'] 
    """
    Esta función calcula la anomalía de Temperatura, Salinidad (climatología 1991-2020)
    y la anomalía de Oxígeno (climatología antigua).
    Args:
        x  (float)     : Longitud Oesta en formato decimal
        y  (float)     : Latitud Norte en formato decimal
        z  (float)     : Profundidad positivo hacia el fondo
        t  (float)     : Mes del año 
        temp_v (float) : Valor de temperatura
        sali_v (float) : Valor de salinidad
        oxig_v (float) : Valor de oxigeno
    Returns:
        [temp_anom, sali_anom] (list) : Climatología T y S.
    """
    long_idx = (np.abs(long - x)).argmin() #devuelve el índice de la celda correspondiente a la longitud dada
    lati_idx = (np.abs(lati - y)).argmin() #devuelve el índice de la celda correspondiente a la latitud dada
    #dept_idx = (np.abs(dept*-1 - z*-1)).argmin() #devuelve el índice de la celda correspondiente a la profundidad dada
    month_idx = t-1 #devuelve el índice de la celda correspondiente al mes dado
    
    dept_aux = dept[:,0];
    temp_aux = temp[long_idx,lati_idx,:,month_idx]
    sali_aux = sali[long_idx,lati_idx,:,month_idx]
    oxig_aux = oxig[long_idx,lati_idx,:,month_idx] 
    
    dept_interp = np.arange(dept_aux[0],dept_aux[-1]+1,1)
    temp_interp = np.interp(dept_interp, dept_aux, temp_aux)
    sali_interp = np.interp(dept_interp, dept_aux, sali_aux)
    oxig_interp = np.interp(dept_interp, dept_aux, oxig_aux)
    zinterp_idx = np.abs(dept_interp*-1 - z*-1).argmin()
    
    temp_anom = temp_v - temp_interp[zinterp_idx]
    sali_anom = sali_v - sali_interp[zinterp_idx]
    oxig_anom = oxig_v - oxig_interp[zinterp_idx]
    
    #temp_anom = temp_v - temp[long_idx,lati_idx,dept_idx,int(month_idx)]
    #sali_anom = sali_v - sali[long_idx,lati_idx,dept_idx,int(month_idx)]
    return [temp_anom,sali_anom,oxig_anom]

def anom2(x,y,z,t,temp_v,sali_v):
   

    dept = mat_t['Zst']
    temp = mat_t['TEMP_monthly']
    sali = mat_s['PSAL_monthly']
    
    """
    Esta función calcula la anomalía de Temperatura, Salinidad (climatología 1991-2020)
    y la anomalía de Oxígeno (climatología antigua).

    Args:
        x  (float)     : Longitud Oesta en formato decimal
        y  (float)     : Latitud Norte en formato decimal
        z  (float)     : Profundidad positivo hacia el fondo
        t  (float)     : Mes del año 
        temp_v (float) : Valor de temperatura
        sali_v (float) : Valor de salinidad
    
    Returns:
        [temp_anom, sali_anom] (list) : Climatología T y S.
    """
    long_idx = (np.abs(long - x)).argmin() #devuelve el índice de la celda correspondiente a la longitud dada
    lati_idx = (np.abs(lati - y)).argmin() #devuelve el índice de la celda correspondiente a la latitud dada
    dept_idx = (np.abs(dept*-1 - z*-1)).argmin() #devuelve el índice de la celda correspondiente a la profundidad dada
    month_idx = t-1 #devuelve el índice de la celda correspondiente al mes dado
    
    dept_aux = dept[:,0];
    temp_aux = temp[long_idx,lati_idx,:,month_idx]
    sali_aux = sali[long_idx,lati_idx,:,month_idx]
    
    dept_interp = np.arange(dept_aux[0],dept_aux[-1]+1,1)
    temp_interp = np.interp(dept_interp, dept_aux, temp_aux)
    sali_interp = np.interp(dept_interp, dept_aux, sali_aux)
    zinterp_idx = np.abs(dept_interp*-1 - z*-1).argmin()
    
    #temp_anom = temp_v - temp_interp[zinterp_idx]
    #sali_anom = sali_v - sali_interp[zinterp_idx]
    
    temp_anom = temp_v - temp[long_idx,lati_idx,dept_idx,int(month_idx)]
    sali_anom = sali_v - sali[long_idx,lati_idx,dept_idx,int(month_idx)]
    return [temp_anom,sali_anom]
	

def letnum(letras):
    """
    Esta función da valor numerico de las columnas en excel.
    
    Args:
        letra  (character)  : Letra de la columna en Excel 
   
    Returns:
        num     (integer)   : Número correspondiente a la columna
    """
    letras = letras.upper()  # Convierte a mayúsculas por si acaso
    num = 0
    for char in letras:
        num = num * 26 + (ord(char) - ord('A') + 1)
    return num

def anomfilas(nombrearchivo,nombrehoja,LonC, LatC, ProfC, FechaC, TctdC, SctdC, OctdC):
    """
    Esta función calcula la anomalía de Temperatura, Salinidad (climatología 1991-2020)
    y la anomalía de Oxígeno (climatología antigua).

    Args:
        x  (float)     : Columna de Lon
        y  (float)     : Columna de Lat
        z  (float)     : Columna de Prof
        t  (float)     : Columna de Mes
        temp_v (float) : Columna de  temperatura
        sali_v (float) : Columna de salinidad
    
    Returns:
        [temp_anom, sali_anom] (list) : Climatología T y S.
    """
    Lon = letnum(LonC)-1
    Lat = letnum(LatC)-1
    Prof = letnum(ProfC)-1
    Fecha = int(letnum(FechaC)-1) 
    Tctd = letnum(TctdC)-1
    Sctd = letnum(SctdC)-1
    Octd = letnum(OctdC)-1
    df = pd.read_excel(nombrearchivo,nombrehoja,header=0)
    df['T_anom'] = None;
    df['S_anom'] = None;
    df['O_anom'] = None;
    for j in range(0,df.shape[0]):
            tano = anom(df.iloc[j,Lon],df.iloc[j,Lat],df.iloc[j,Prof],int(df.iloc[j,Fecha]),df.iloc[j,Tctd],df.iloc[j,Sctd],df.iloc[j,Octd])[0]
            sano = anom(df.iloc[j,Lon],df.iloc[j,Lat],df.iloc[j,Prof],int(df.iloc[j,Fecha]),df.iloc[j,Tctd],df.iloc[j,Sctd],df.iloc[j,Octd])[1]
            oano = anom(df.iloc[j,Lon],df.iloc[j,Lat],df.iloc[j,Prof],int(df.iloc[j,Fecha]),df.iloc[j,Tctd],df.iloc[j,Sctd],df.iloc[j,Octd])[2]
            df.at[j, 'T_anom'] = tano
            df.at[j, 'S_anom'] = sano
            df.at[j, 'O_anom'] = oano
    print([df[['T_anom','S_anom','O_anom']]])
    df.to_excel('animaladas.xlsx',index=False)
    return[df.T_anom,df.S_anom,df.O_anom]


### Usuario
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Calcular anomalías T, S, O desde un archivo Excel.")
    parser.add_argument('--archivo', required=True, help='Ruta al archivo Excel')
    parser.add_argument('--hoja', required=True, help='Nombre de la hoja')
    parser.add_argument('--columnas', required=True,
                        help='Columnas en orden: lon,lat,prof,mes,temp,sali,oxi (ej. A,B,C,D,E,F,G)')

    args = parser.parse_args()
    columnas = args.columnas.split(',')

    if len(columnas) != 7:
        raise ValueError("Se esperaban exactamente 7 columnas: lon,lat,prof,mes,temp,sali,oxi")

    # Desempaquetamos los valores
    lonn, latt, proff, fecc, tt, ss, oo = columnas

    # Llamamos a la función principal
    anomfilas(args.archivo, args.hoja, lonn, latt, proff, fecc, tt, ss, oo)
