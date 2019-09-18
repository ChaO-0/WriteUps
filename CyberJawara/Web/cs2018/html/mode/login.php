<?php

$rets = function($params){
	$users = util_call("db", "users");

	foreach ($users as $user) {
		if ($user["loginid"] === $params["loginid"] && $user["password"] === sha1($params["pass"])) {
			$sess = util_call("session", "read");
			$sess["user"] = $user;
			util_call("session", "write", $sess);
			$files = util_call("db", "files");
			$u_files = array();
			foreach ($files as $file) {
				if ($file["priv"] <= $sess["user"]["priv"]) {
					array_push($u_files, $file);
				}
			}
			print json_encode(array("msg" => "ok", "user" => $sess["user"], "files" => $u_files));
			return true;
		}
	}

	print json_encode(array("msg" => "no"));
	return false;
};

$deploy = true;