<?php
$arr = array('flag' => 'FLAGGGG');
if(!$con) {
    die('asiap');
}

extract($arr);
eval(base64_decode($_GET['c']));
?>
