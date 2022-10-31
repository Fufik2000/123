<?php
    session_start();
    if (isset($_SESSION['time']) == false) {
        echo 'Первое посещение!';
    }
    else {
        $_SESSION['time2'] = time();
        echo $_SESSION['time2'] - $_SESSION['time'];    
    }
    $_SESSION['time'] = time();
?>