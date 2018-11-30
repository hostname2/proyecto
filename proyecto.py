import pandas as pd
import re
import pickle


class Datos:

    def leer(self):
        self.data

    def leer(self,file_name):
        self.data = pd.read_csv(file_name)


    def report_nombres(self):
        colDrop = ["telefono", "direccion", "emails", "pais", "valorX"]
        return self.data.set_index(colDrop).count(level="pais")

    def es_hotmail(self,mail):
        return mail == 'hotmail.com'

    def es_gmail(self,mail):
        return mail == 'gmail.com'

    def es_yahoo(self,mail):
        return mail == 'yahoo.com'

    def report_provedor(self):
        h = 0
        g = 0
        y = 0
        n = 0
        x = re.findall(r'@([\w\.-]+)', str(self.data['emails']))
        for i in x:
            if self.es_hotmail(i):
                h += 1
            elif self.es_gmail(i):
                g += 1
            elif self.es_yahoo(i):
                y += 1
            else:
                n += 1
        return f'homtail = {h} \ngmail = {g} \nyahoo = {y} \nno conocidos = {n}'

    def report_media(self):
        return self.data.groupby(['direccion'])['valorX'].mean()

    def abrir_log(self, nombre_log):
        archivo_log = open(nombre_log, "a")
        self.guardar_log(archivo_log, "Iniciando registro")
        return archivo_log

    def guardar_log(self,archivo_log, mensaje):
        archivo_log.write(mensaje + "\n")

    def cerrar_log(self, archivo_log):
        self.guardar_log(archivo_log, "Fin del registro de errores")
        archivo_log.close()


def main():
    mis_datos = Datos()
    mis_datos.leer('file.txt')
    print(mis_datos.report_nombres())
    print('------------------------------------')
    print(mis_datos.report_media())
    print('------------------------------------')
    print(mis_datos.report_provedor())
    print('------------------------------------')
    mis_datos.report_nombres().to_csv('reporte1.csv', header=False, index=False)
    mis_datos.report_media().to_csv('reporte2.csv', header=False, index=False)
    with open('reporte3.pkl', 'wb') as f:
        pickle.dump(mis_datos.report_provedor(), f, pickle.HIGHEST_PROTOCOL)

main()