<?php
    require_once '1.2.php';

    $x = new Car;
    $x->marka = 'Toyota';
    $x->color = 'Белый';
    
    echo $x->marka.' '.$x->color.'<br>';
    $x->go();
    $x->turn();
    $x->stop();

?>