def putConexion():
    content = str("")
    content += "<?php\n"
    content += "date_default_timezone_set(\"America/Bogota\");\n"
    content += "require_once 'conexion.php';\n"
    content += "$conexion = new Conexion();\n"
    content += "if (isset($_GET['accion'])) {\n"
    content += "\t$accion = $_GET['accion'];\n"
    return content

def createPost(campos):
    content = str("")
    for campo in campos:
        content += "\t\t$" + campo + " = $_POST[\'" + campo + "\'];\n"
    return content

def createPostDelete(campos):
    content = str("\t\t$" + campos[0] + " = $_POST[\'" + campos[0] + "\'];\n")
    return content

def createSqlInsert(table, campos):
    content = str("")
    content += "\t\t$sql = \"INSERT INTO "
    content += table + "(\n\t\t\t" 
    content += ", ".join(campos)
    content += "\n\t\t\t)VALUES ("
    i = 0
    while(len(campos)>i):
        content += "?,"
        i += 1   
    content = content[:-1]+ ")\";\n"
    return content

def createSqlUpdate(table, campos):
    content = str("")
    content += "\t\t$sql = \"UPDATE "+ table +" SET "
    i = 1
    while(len(campos) > i):
        content += "\n\t\t\t" + campos[i] + "=:" + campos[i] + ","
        i+=1
    content = content[:-1]+ "\n\t\t\tWHERE " + campos[0] + " = :" + campos[0] + ";\";\n"
    return content

def createSqlDelete(table, campos):
    content = str("")
    content += "\t\t$sql = \"DELETE FROM "+ table
    content += " WHERE " + campos[0] + " = :" + campos[0] + ";\";\n"
    return content

def createbindParamInsert(campos):
    content = str("\t\t$reg = $conexion->prepare($sql);\n")
    i = int(1)
    for campo in campos:
        content += "\t\t$reg->bindParam(" + str(i) + ", $" + campo + ");\n"
        i += 1
    return content

def createbindParamUpdate(campos):
    content = str("\t\t$reg = $conexion->prepare($sql);\n")
    i = int(1)
    for campo in campos:
        content += "\t\t$reg->bindParam(\":" + campo + "\", $" + campo + ");\n"
        i += 1
    return content

def createbindParamDelete(campos):
    content = str("\t\t$reg = $conexion->prepare($sql);\n")
    i = int(1)
    content += "\t\t$reg->bindParam(\":" + campos[0] + "\", $" + campos[0] + ");\n"
    return content

def validationExecute():
    content = str("")
    content += "\t\tif ($reg->execute() === TRUE) {\n"
    content += "\t\t\techo 1;\n"
    content += "\t\t} else {\n"
    content += "\t\t\techo 0;\n"
    content += "\t\t}\n"
    return content

def createInsert(table, campos):
    content = str("")
    content += "\tif ($accion == 'registrar') {\n"
    content += createPost(campos)
    content += createSqlInsert(table, campos)
    content += createbindParamInsert(campos)
    content += validationExecute()
    return content

def createUpdate(table, campos):
    content = str("")
    content += "\t} else if ($accion == 'modificar') {\n"
    content += createPost(campos)
    content += createSqlUpdate(table, campos)
    content += createbindParamUpdate(campos)
    content += validationExecute()
    return content

def createDelete(table, campos):
    content = str("")
    content += "\t} else if ($accion == 'eliminar') {\n"
    content += createPostDelete(campos)
    content += createSqlDelete(table, campos)
    content += createbindParamDelete(campos)
    content += validationExecute()
    return content

def createFileAction(table, campos):
    content = str("")
    content += putConexion()
    content += createInsert(table, campos)
    content += createUpdate(table, campos)
    content += createDelete(table, campos)
    content += "\t} else {\n"
    content += "\t\techo 2;\n"
    content += "\t}\n"
    content += "} else {\n"
    content += "\techo 3;\n"
    content += "}\n"
    return content
