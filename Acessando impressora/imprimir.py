import win32print
import win32api
import os, sys
import time

# escolhe a impressora
listaimpressoras = win32print.EnumPrinters(2)
impressora = listaimpressoras[10]

# win32print.SetDefaultPrinter(impressora[2])


#manda imprimir todos os arquivos
caminho = r"C:\Users\gustavo.felix\Downloads\Imprimir"
lista_arquivos = os.listdir(caminho)

# https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
for arquivo in lista_arquivos:
   win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)


# for file in lista_arquivos:
   
#   # Instantiating the path of the file
#     file_path = f'{caminho}\\{file}'
 
#     # Checking whether the given file is a directory or not
#     if os.path.isfile(file_path):
#         try:
#             # Printing the file pertaining to file_path
#             os.startfile(file_path, 'print')
#             print(f'Printing {file}')
 
#             # Sleeping the program for 5 seconds so as to account the
#       # steady processing of the print operation.
#             time.sleep(5)
#         except:
#             # Catching if any error occurs and alerting the user
#             print(f'ALERT: {file} could not be printed! Please check\
#             the associated softwares, or the file type.')
#     else:
#         print(f'ALERT: {file} is not a file, so can not be printed!')
         
# print('Task finished!')


input("Press Enter to continue...")
