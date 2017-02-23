<?php
//output '0' : error - delete id
//output '1' : successful
//output '2' : already exist - delete id

function generateRandomString($length = 6) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyz';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

include("connect.php");

if(isset($_GET['fid']) && isset($_GET['mobileno']) && $_GET['fid'] != "" && $_GET['mobileno'] != ""){
	$finger_print_id = mysql_real_escape_string($_GET['fid']);
	$mobile_no = mysql_real_escape_string($_GET['mobileno']);
	$password = generateRandomString();
	$q = "SELECT * FROM `users` WHERE `mobile_no` = '".$mobile_no."'";
	$f = mysql_query($q);
	$number = mysql_num_rows($f);
	if($number == 0){
		$q = "INSERT INTO `users` (`password`,`finger_print_id`,`mobile_no`) VALUES ('".$password."','".$finger_print_id."','".$mobile_no."')";
		mysql_query($q)
			or die(0);
		echo(1);
	}
	else{
		$a = mysql_fetch_array($f);
		$password = $a['password'];
		echo(2);
	}
	include('sms/way2sms-api.php');
	sendWay2SMS ( "9409506643","123456",$mobile_no,"Thank you for register on Touch-n-pay. login with, username=".$mobile_no.",passsword=".$password."");
}
else{
	echo(0);
}

?>