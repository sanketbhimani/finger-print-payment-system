<?php


/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		register_new_user.php
* Functions:		generateRandomString
*/


//output '0' : error - delete id
//output '1' : successful
//output '2' : already exist - delete id




/*
*
* Function Name: 	generateRandomString
* Input: 		length (default 6)
* Output: 		rendom string oof given length
* Logic: 		create rendom string form array
* Example Call:	generateRandomString();
*
*/
function generateRandomString($length = 6) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyz';
    $charactersLength = strlen($characters);
    $randomString = '';
	//create rendom string of given length form array
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

include("connect.php"); //create connection with database
//fid: finger_print_id, mobileno: mobile no
//check parameters availability
if(isset($_GET['fid']) && isset($_GET['mobileno']) && $_GET['fid'] != "" && $_GET['mobileno'] != ""){
	//for security porous, it will remove all special characters
	$finger_print_id = mysql_real_escape_string($_GET['fid']);
	$mobile_no = mysql_real_escape_string($_GET['mobileno']);
	$password = generateRandomString();
	
	///if we remove comments form below code then this will use mobile no as user id and unique mobile no for one user 
	
//	$q = "SELECT * FROM `users` WHERE `mobile_no` = '".$mobile_no."'";
//	$f = mysql_query($q);
//	$number = mysql_num_rows($f);
//	if($number == 0){
		//insert in to database
		$q = "INSERT INTO `users` (`password`,`finger_print_id`,`mobile_no`) VALUES ('".$password."','".$finger_print_id."','".$mobile_no."')";
		mysql_query($q)
			or die(0);
		echo(1);
//	}
//	else{
//		$a = mysql_fetch_array($f);
//		$password = $a['password'];
//		echo(2);
//	}
	//send sms to user
	include('sms/way2sms-api.php');
	sendWay2SMS ( "9409506643","123456",$mobile_no,"Thank you for register on Touch-n-pay. login with, username=".mysql_insert_id().",   password=".$password."");
}
else{
	echo(0);
}

?>