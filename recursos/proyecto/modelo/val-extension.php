<?php
session_start();
require_once 'conexion.php';
require_once "datos-distritos.php";
$conexion = new Conexion();
$misdistritos = new misDistritos();

$idu = $_SESSION['id'];
$nombre = $_SESSION['nombre'];
$user = $_SESSION['usuario'];
//$email = $_SESSION['email'];
//$rol = $_SESSION['rol'];
//$dpto = $_SESSION['dpto'];
$departamento = "Norte de Santander";

/** Información del extensionista */
$conusu = "SELECT * FROM extensionista WHERE doc_tecnico=" . $idu;
$modules = $conexion->prepare($conusu);
$modules->execute();
$rusu = $modules->fetch(PDO::FETCH_ASSOC);

/** Información del extensionista y distrito */
$conexdis = "SELECT * FROM distrxextensionista WHERE doc_tecnico=" . $idu;
$modexdis = $conexion->prepare($conexdis);
$modexdis->execute();
$resexdis = $modexdis->fetch(PDO::FETCH_ASSOC);
$id_distr = $resexdis['id_distr'];

/** Información del distrito */
$condistr = "SELECT * FROM distrito WHERE id_distr=" . $id_distr;
$moddistr = $conexion->prepare($condistr);
$moddistr->execute();
$resdistr = $moddistr->fetch(PDO::FETCH_ASSOC);
$id_distr = $resdistr['id_distr'];
$nom_distr = $resdistr['nom_distr'];

if (!$_SESSION) {
    echo '<script language = javascript>
    alert("Usuario no autenticado.")
    self.location = "../index.php"
    </script>';
} elseif ($idu != $rusu['doc_tecnico']) {
    session_destroy();
    echo '<script language = javascript>
    self.location = "../index.php"
    </script>';
}
