<?php
    require_once 'User2.php';
    require_once 'Student.php';
    require_once 'group.php';

    $i04 = new Group('И-04');

    $x1 = new Student('Максим', 'Макрицкий', 18, 5);
    $x2 = new Student('ыфыв', 'фыв', 10, 2);

    $i04->addStudent($x1);
    $i04->addStudent($x2);

    $i04->display();

?>