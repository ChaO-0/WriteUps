<?php

if ($args[0] === "users") {
	$rets = array(
        array(
            "loginid" => "admin",
            "password" => "3d7a977b30393c70cbddc6ac1ea95e35f4e048fc",
            "priv" => 1
        ),
        array(
            "loginid" => "tester",
            "password" => "ab4d8d2a5f480a137067da17100271cd176607a1",
            "priv" => 0
        )
    );
} elseif ($args[0] === "files") {
	$rets = array(
        array(
            "id" => 1,
            "name" => "flag",
            "path" => "secret_path_of_flag.txt",
            "priv" => 1
        ),
        array(
            "id" => 2,
            "name" => "lorem_ipsum",
            "path" => "lorem_ipsum.txt",
            "priv" => 0
        ),
        array(
            "id" => 3,
            "name" => "exploit",
            "path" => "exploit.txt",
            "priv" => 0
        )     
    );
}
