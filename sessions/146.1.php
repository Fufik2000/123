<?php
	session_start();
	$_SESSION['num_1'] = '1';
    $_SESSION['num_2'] = '2';
    $_SESSION['sum'] = $_SESSION['num_1'] + $_SESSION['num_2'];
?>