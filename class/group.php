<?php
    require_once 'Student.php';

    class Group {
        private $name;
        private $students = [];

        public function __construct($name) {
            $this->name = $name;
        }

        public function addStudent($student) {
            $this->students[] = $student;
        }

        public function display() {
            echo '<h2>Группа: '.$this->name.'</h2>';
            echo '<h3>Список студентов:</h3>';
            echo '<ol>';
            foreach ($this->students as $student) {
                echo '<li>';
                echo $student->getSurname().' ';
                echo $student->getName();
                echo '</li>';
            }
            echo '</ol>';
        }
    }
?>