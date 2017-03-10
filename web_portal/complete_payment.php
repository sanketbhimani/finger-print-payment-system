<?php

/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		complete_payment.php
*
*/

	include("connect.php"); //create connection with database
	session_start(); //start session
	
	
	//check if your is logged in or not, if not redirect to login page
	if(!isset($_SESSION['users_id'])){ 
		header("location:index.php");
		die();
	}
	
	
	//verify payment from instamojo	
	require("src/Instamojo.php");
	$api = new Instamojo\Instamojo('cd967a0dcfcc398a66b1e74072be912e', '7096a27b2df3e0bb3a55598c379ff96c','https://test.instamojo.com/api/1.1/');
	try {
		$response = $api->paymentRequestPaymentStatus($_GET['payment_request_id'], $_GET['payment_id']);
		if(strtolower($response['payment']['status'])!="credit"){
			echo("Payment failed<br>Contact us for any problem");
			die();
		}
	}catch (Exception $e){
		print('Error: ' . $e->getMessage());
		echo("<br>Contact us for any problem");
		die();
	}
	
	
	$money = $_SESSION['money'];
	unset($_SESSION['money']);
	
	//add entry to database with date and time
	date_default_timezone_set('Asia/Kolkata');
	$date = date('m/d/Y h:i:s a', time());
	$q = "INSERT INTO `payment_data` (`users_id`, `amount`, `debit_credit`, `date`) VALUES ('".$_SESSION['users_id']."', '".$money."', 'Credited','".$date."')";
	mysql_query($q);
	
	//update balance in database
	$q = "SELECT * FROM `users` WHERE `id` = '".$_SESSION['users_id']."'";;
	$f = mysql_query($q);
	$a = mysql_fetch_array($f);
	$updated_balance = $a['balance'] + $money;
	$q = "UPDATE `users` SET `balance` = '".$updated_balance."' WHERE `id` = '".$_SESSION['users_id']."'";
	mysql_query($q);
	
	//send sms to user regarding money entry
	include('sms/way2sms-api.php');
	sendWay2SMS ( "9409506643","123456",$a['mobile_no'],$money." rupees credited in your account. your current balance is ".$updated_balance);
	
	//if done then redirect to home page
	header("location:home.php?done=1");
?>