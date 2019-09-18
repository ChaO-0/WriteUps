<?php
session_start();

if ($args[0] === "read") {
	$rets = $_SESSION;
} elseif ($args[0] === "write") {
	$_SESSION = $args[1];
}
