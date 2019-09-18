<?php

ini_set("display_errors",0);
require_once "./utils.php";
header("Content-type: application/json;charset=UTF-8");

$mode = $_GET["mode"];

$deploy = false;
$str = file_get_contents("php://input");
$params = json_decode($str, true);
$file = __DIR__ . "/mode/" . $mode . ".php";

if (file_exists($file)) {
	require_once $file;
	if ($deploy) {
		try {
			$rets($params);
		} catch (Exception $e){
			print "Error";
		}
	}
} else {
	header("Location: ./index.html");
}
