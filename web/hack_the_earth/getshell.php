<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Big Hacker</title>

    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Before Hacking the Earth</h1>
    <h1>Please get the shell first</h1>
    <form action="getshell.php">
        <button class="bubbly-button" name="source">Get the source code</button>
    </form>
</body>
</html>

<?php
    error_reporting(0);
    if (isset($_GET['source'])) {
        highlight_file(__FILE__);
    }

    class Shell {
        public $cmd;
        function __construct($cmd) {
            $this->cmd = $cmd;
        }

        function __destruct() {
            system($this->cmd);
        }
    }

    $money = $_GET['money'];

    if ($money) {
        if ($money == 999 && $money !== '999') {
            new Shell($_GET['cmd']);
        } else {
            echo "<script>alert('不要用假钱买shell!!!')</script>";
        }
    }
?>


    