<?php

$rets = function($params=[]){
	$sess = util_call("session", "read");
	if (isset($sess["user"])) {
		$files = util_call("db", "files");
		foreach ($files as $file) {
			if ($file["id"] == $_GET["id"] && $file["priv"] <= $sess["user"]["priv"]) {
				header("Content-Disposition: attachment;filename=" . $file["name"] . ".txt");
				header("Content-type: application/octet-stream");			
				print file_get_contents(__DIR__ . "/../../files/" . $file["path"]);
				break;				
			}
		}
	}
};

$deploy = true;