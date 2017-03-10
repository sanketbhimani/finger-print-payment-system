<?php

/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		do_payment.php
*
*/



include("connect.php"); //create connection with database

//fid: finger print id, cost: money

if(isset($_GET['fid']) && isset($_GET['cost']) && $_GET['fid'] != '' && $_GET['cost'] != ''){
	//for security porous, it will remove all special characters
	$finger_print_id = mysql_real_escape_string($_GET['fid']);
	$cost = mysql_real_escape_string($_GET['cost']);
	
	
	//get details about user
	$q = "SELECT * FROM `users` WHERE `finger_print_id` = '".$finger_print_id."'";
	$f = mysql_query($q);
	$a = mysql_fetch_array($f);
	
	$mobile_no = $a['mobile_no'];
	$balance = $a['balance'];
	
	include('sms/way2sms-api.php');
	//if current balance is more then the cost then make payment
	if($cost <= $balance){
		//make entry in database about money deducted
		$updated_balance = $balance - $cost;
		
		$q = "UPDATE `users` SET `balance` = '".$updated_balance."' WHERE `finger_print_id` = '".$finger_print_id."'";
		mysql_query($q);
		date_default_timezone_set('Asia/Kolkata');
		$date = date('m/d/Y h:i:s a', time());
		
		$q = "INSERT INTO `payment_data` (`users_id`, `amount`, `debit_credit`, `date`) VALUES('".$a['id']."', '".$cost."', 'Debited', '".$date."')";
		mysql_query($q);
		//send sms regarding money deducted and return status 1
		sendWay2SMS ( "9409506643","123456",$mobile_no,$cost." rupees debited from your account. your current balance is ".$updated_balance);
		echo(1);
		die();
		
	}
	else{
		//else if enough cash is not available then payment fails and send releted sms and return status 2
		sendWay2SMS ( "9409506643","123456",$mobile_no,"insufficient balance in your account. your current balance is ".$balance);
		echo(2);
		die();
	}
}
//if proper request is not make then retuen statue 0
echo(0);

?>