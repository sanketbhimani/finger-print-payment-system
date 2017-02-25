<?php

include("connect.php");

if(isset($_GET['fid']) && isset($_GET['cost']) && $_GET['fid'] != '' && $_GET['cost'] != ''){
	$finger_print_id = mysql_real_escape_string($_GET['fid']);
	$cost = mysql_real_escape_string($_GET['cost']);
	
	$q = "SELECT * FROM `users` WHERE `finger_print_id` = '".$finger_print_id."'";
	$f = mysql_query($q);
	$a = mysql_fetch_array($f);
	
	$mobile_no = $a['mobile_no'];
	$balance = $a['balance'];
	
	include('sms/way2sms-api.php');
	
	if($cost <= $balance){
		
		$updated_balance = $balance - $cost;
		
		$q = "UPDATE `users` SET `balance` = '".$updated_balance."' WHERE `finger_print_id` = '".$finger_print_id."'";
		mysql_query($q);
		date_default_timezone_set('Asia/Kolkata');
		$date = date('m/d/Y h:i:s a', time());
		
		$q = "INSERT INTO `payment_data` (`users_id`, `amount`, `debit_credit`, `date`) VALUES('".$a['id']."', '".$cost."', 'Debited', '".$date."')";
		mysql_query($q);
		
		sendWay2SMS ( "9409506643","123456",$mobile_no,$cost." rupees debited from your account. your current balance is ".$updated_balance);
		echo(1);
		die();
		
	}
	else{
		sendWay2SMS ( "9409506643","123456",$mobile_no,"insufficient balance in your account. your current balance is ".$balance);
		echo(2);
		die();
	}
}
echo(0);

?>