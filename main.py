from pathlib import Path
import shutil
import fileHandler as file
import creaAccion as acc
import createTableList as tab

path = Path('../proyecto/modelo/')
path.mkdir(parents=True, exist_ok=True)

shutil.copy("recursos/proyecto/modelo/conexion.php", "../proyecto/modelo/conexion.php")
shutil.copy("recursos/proyecto/modelo/login.php", "../proyecto/modelo/login.php")
shutil.copy("recursos/proyecto/modelo/salir.php", "../proyecto/modelo/salir.php")
shutil.copy("recursos/proyecto/modelo/val-extension.php", "../proyecto/modelo/val-extension.php")

table = str("tabla")
campos = ["ccod_munic", "convenio", "imagen"];

content1 = acc.createFileAction(table, campos)
content2 = tab.createFiletableList(table, campos)

file.createFile("../proyecto/modelo/acciones"+ table.capitalize() +".php",content1)
file.createFile("../proyecto/modelo/listar"+ table.capitalize() +".php",content2)
