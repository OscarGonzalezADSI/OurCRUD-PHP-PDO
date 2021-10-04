   
def createSqlSelectRow(table, columns):
    content = str("")
    content += "\t\t$consulta = \"SELECT \n\t\t\t"
    content += ",\n\t\t\t".join(columns)
    content += "\n\t\t\tFROM " + table
    content += "\n\t\t\tWHERE ccod_munic = :ccod_munic\";\n"
    return content
    
def createSqlSelectAll(table, columns):
    content = str("")
    content += "\t\t$consulta = \"SELECT \n\t\t\t"
    content += ",\n\t\t\t".join(columns)
    content += "\n\t\t\tFROM " + table + ";\";\n"
    return content
    
def createSqlSelectCount(table, column):
    content = str("")
    content += "\t\t$consulta = \"SELECT count(" + str(column[0]) + ") as cant \n"
    content += "\t\t\tFROM "+ table + "\";\n";
    return content
    
def viewRow(table, columns):
    content = str("")
    content += "\tfunction viewRow" + table.capitalize() + "($" + columns[0] + ")\n"
    content += "\t{\n"
    content += "\t\trequire_once 'conexion.php';\n"
    content += "\t\t$conexion = new Conexion();\n"
    content += "\t\t$arreglo = array();\n"
    content += createSqlSelectRow(table, columns)
    content += "\t\t$modules = $conexion->prepare($consulta);\n"
    content += "\t\t$modules->bindParam(\":" + columns[0] + "\", $" + columns[0] + ");\n"
    content += "\t\t$modules->execute();\n"
    content += "\t\t$total = $modules->rowCount();\n"
    content += "\t\tif ($total > 0) {\n"
    content += "\t\t\t$i = 0;\n"
    content += "\t\t\twhile ($data = $modules->fetch(PDO::FETCH_ASSOC)) {\n"
    content += "\t\t\t\t$arreglo[$i] = $data;\n"
    content += "\t\t\t\t$i++;\n"
    content += "\t\t\t}\n"
    content += "\t\t}\n"
    content += "\t\treturn $arreglo;\n"
    content += "\t}\n"
    return content

def viewALL(table, column):
    content = str("")
    content += "\tfunction viewAll" + table.capitalize() + "()\n"
    content += "\t{\n"
    content += "\t\trequire_once 'conexion.php';\n"
    content += "\t\t$conexion = new Conexion();\n"
    content += "\t\t$arreglo = array();\n"
    content += createSqlSelectAll(table, column)
    content += "\t\t$modules = $conexion->prepare($consulta);\n"
    content += "\t\t$modules->execute();\n"
    content += "\t\t$total = $modules->rowCount();\n"
    content += "\t\tif ($total > 0) {\n"
    content += "\t\t\t$i = 0;\n"
    content += "\t\t\twhile ($data = $modules->fetch(PDO::FETCH_ASSOC)) {\n"
    content += "\t\t\t\t$arreglo[$i] = $data;\n"
    content += "\t\t\t\t$i++;\n"
    content += "\t\t\t}\n"
    content += "\t\t}\n"
    content += "\t\treturn $arreglo;\n"
    content += "\t}\n"
    return content

def viewCount(table, column):
    content = str("")
    content += "\tfunction viewCount" + table.capitalize() + "()\n"
    content += "\t{\n"
    content += "\t\trequire_once 'conexion.php';\n"
    content += "\t\t$conexion = new Conexion();\n"
    content += createSqlSelectCount(table, column);
    content += "\t\t$modules = $conexion->prepare($consulta);\n"
    content += "\t\t$modules->execute();\n"
    content += "\t\t$data = $modules->fetch(PDO::FETCH_ASSOC);\n"
    content += "\t\t$total = 0;\n"
    content += "\t\t$total = $data['cant'];\n"
    content += "\t\treturn $total;\n"
    content += "\t}\n"
    return content

def createFiletableList(table,campos):
    content = str("<?php\n\n")
    content += "class " + table.capitalize()
    content += "\n{\n"
    content += viewRow(table, campos)
    content += viewALL(table, campos)
    content += viewCount(table, campos)
    content += "}\n"
    return content