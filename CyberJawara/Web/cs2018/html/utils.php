<?php

function util_call() {
	$args = func_get_args();
	$path = array_shift($args);
	require __DIR__ . "/utils/" . $path . ".php";
	return $rets;
}
