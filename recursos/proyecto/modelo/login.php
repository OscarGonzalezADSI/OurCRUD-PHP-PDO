<?php
//session_start();
require 'conexion.php';
$conexion = new Conexion();

if (isset($_POST['usu']) && isset($_POST['pass'])) {

    $loginNombre = $_POST["usu"];
    $loginPassword = $_POST["pass"];

    $sql = "SELECT * FROM usuario WHERE usuario='" . $loginNombre . "' AND contrasena='" . $loginPassword . "'";
    $modules = $conexion->prepare($sql);
    $modules->execute();
    $total = $modules->rowCount();

    if ($total > 0) {
        $row = $modules->fetch(PDO::FETCH_ASSOC);
        if (($row['usuario'] == $loginNombre) && ($row['contrasena'] == $loginPassword) && ($row['rol'] == 1)) {
            session_start();
            $_SESSION['id'] = $row['identificacion'];
            $_SESSION['nombre'] = $row['nombre'];
            $_SESSION['usuario'] = $row['usuario'];
            $_SESSION['email'] = $row['email'];
            $_SESSION['rol'] = $row['rol'];
            $_SESSION['dpto'] = $row['ccod_depto'];
            header("Location: ../admin/index.php");
        } elseif (($row['usuario'] == $loginNombre) && ($row['contrasena'] == $loginPassword) && ($row['rol'] == 3)) {
            session_start();
            $_SESSION['id'] = $row['identificacion'];
            $_SESSION['nombre'] = $row['nombre'];
            $_SESSION['usuario'] = $row['usuario'];
            $_SESSION['email'] = $row['email'];
            $_SESSION['rol'] = $row['rol'];
            $_SESSION['dpto'] = $row['ccod_depto'];
            header("Location: ../recaudos/index.php");
        } else {
            //session_destroy();
            echo '<script language = javascript>
            alert("Datos incorectos del usuario.");
            self.location = "../index.php" 
            </script>';
        }
    } else {
        $sqlext = "SELECT * FROM extensionista WHERE usuario='" . $loginNombre . "' AND contrasena='$loginPassword'";
        $modext = $conexion->prepare($sqlext);
        $modext->execute();
        $totalext = $modext->rowCount();

        if ($totalext > 0) {
            $rowext = $modext->fetch(PDO::FETCH_ASSOC);
            $rol = 2;
            if ($rowext['usuario'] == $loginNombre && $rowext['contrasena'] == $loginPassword) {
                session_start();
                $_SESSION['id'] = $rowext['doc_tecnico'];
                $_SESSION['nombre'] = $rowext['nombre_tecnico'] . " " . $rowext['apellido_tecnico'];
                $_SESSION['usuario'] = $rowext['usuario'];
                $_SESSION['rol'] = 2;
                //$_SESSION['email'] = $rowext['email'];
                header("Location: ../extensionista/index.php");
            } else {
                //session_destroy();
                //$myerror = $conexion->error;
                //echo "Error... " . $myerror;
                echo '<script language = javascript>
                alert("Datos incorectos del extensionista 1.");
                self.location = "../index.php" 
                </script>';
            }
        } else {
            //session_destroy();
            //$myerror = $conexion->error;
            //echo "Error... " . $myerror;
            echo '<script language = javascript>
            alert("Datos incorectos del extensionista 2.");
            self.location = "../index.php" 
            </script>';
        }
    }
} else {
    //session_destroy();
    echo '<script language = javascript>
	alert("Por favor verifique la información registrada.");
	self.location = "../index.php"
	</script>';
}
