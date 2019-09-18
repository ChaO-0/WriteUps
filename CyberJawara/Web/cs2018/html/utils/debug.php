<?php

$p = $_GET["p"];
$eq = $_GET["eq"];

if (isset($eq) && isset($p)) {
	switch ($eq) {
		case "modetest":
			$dfpath = __DIR__ . "/../mode/" . $p . ".php";
			if (file_exists($dfpath)) {
				$deploy = true;
				require $dfpath;
				$rets();
			}
		case "escape":
			$rets = htmlspecialchars($p);
			print $rets;
	}
} else {
	http_response_code(404);
	exit();
}
