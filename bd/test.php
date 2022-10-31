<style>
    table {
        border-collapse: collapse;
    }
    th {
        border: 1px solid black;
    }
    td {
        border: 1px solid black;
    }
</style>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Имя</th>
            <th>Логин</th>
            <th>Возраст</th>
            <th>Группа</th>
        </tr>
    </thead>
    <tbody>
<?php
	$host = 'my_db'; // имя хоста
	$user = 'root';      // имя пользователя
	$pass = '1234';          // пароль
	$name = 'bd_test';      // имя базы данных
	
	$link = mysqli_connect($host, $user, $pass, $name);

    $query = 'SELECT `ID`, `NAME`, `LOGIN`, `AGE`, `ID_GROUP` FROM `studen`';
    $result = mysqli_query($link, $query) or die(mysqli_error($link));
    while ($row = mysqli_fetch_assoc($result)) {
       echo '<tr>';
       echo '<td>'. $row ['ID'].'</td>';
       echo '<td>'. $row ['NAME'].'</td>';
       echo '<td>'. $row ['LOGIN'].'</td>';
       echo '<td>'. $row ['AGE'].'</td>';
       echo '<td>'. $row ['ID_GROUP'].'</td>';
       echo '</tr>';
    }
?>
    </tbody>
</table>