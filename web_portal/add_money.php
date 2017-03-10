


<?php

/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		add_money.php
*
*/


	include("connect.php"); //create connection with database
	session_start(); //start session
	
	
	//check if your is logged in or not, if not redirect to login page
	if(!isset($_SESSION['users_id'])){ 
		header("location:index.php");
		die();
	}
	
	
	
	//get user details
	$q = "SELECT * FROM `users` WHERE `id` = '".$_SESSION['users_id']."'";;
	$f = mysql_query($q);
	$a = mysql_fetch_array($f); 
	
	
	
	//if name is not avilable then first ask for name
	if($a['name']==""){
		header("location:add_name.php");
		die();
	}
	
	
	//check whether request comes with proper perameters or not
	if(isset($_POST['money']) && $_POST['money'] != ""){
		
		
		//for security porous, it will remove all special characters
		$money = mysql_real_escape_string($_POST['money']);
		
		//create link for instamojo payment
		require("src/Instamojo.php");
		$_SESSION['money'] = $money;
		$api = new Instamojo\Instamojo('cd967a0dcfcc398a66b1e74072be912e', '7096a27b2df3e0bb3a55598c379ff96c','https://test.instamojo.com/api/1.1/');
		try {
			$response = $api->paymentRequestCreate(array(
				"buyer_name" => $a['name'],
				"purpose" => "Touch-n-Pay Credit",
				"amount" => $money,
				"send_email" => false,
				"phone" => $a['mobile_no'],
				"allow_repeated_payments" => false,
				"email" => "snk.bhimani@gmail.com",
				"redirect_url" => "http://malgadi.co.in/touch-n-pay/complete_payment.php"
			));
			$url = $response['longurl'];
			
			//redirect user to that created link
			header("location:".$url);
		}catch (Exception $e) {
			print('Error: ' . $e->getMessage());
			echo("<br>Contact us for any problem");
			die();
		}

	}
?>
<html>
	<head>
		<link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
		<link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
		<script type="text/javascript" src="js/jquery-2.1.1.min.js"></script>
		<script type="text/javascript" src="js/materialize.min.js"></script>
	</head>
	<body>
		<nav class="red lighten-1">
			<div class="nav-wrapper">
				<center style="position:absolute; margin:auto; margin-right:10%; left:0; right:0;">
					<span style="font-size: 2em;">Touch n Pay</span>
				</center>
				<ul id="nav" style="margin-right: 3%;" class="right">
					<li><a href="logout.php">Logout</a></li>
				</ul>
			</div>
		</nav>
		<div class="container">
			<h3 class="center" style="margin-top: 30px;">Welcome, <?php echo($a['name']); ?></h3>
			<h4 class="center" style="margin-top: 30px;">Add Money</h4>
			<div class="row" style="margin-top: 30px;">
				<div class="offset-s3 col s6">
					<form action="add_money.php" method="post">
						<div class="row">
							<div class="input-field col s12">
								<input id="money" type="text" name="money" class="validate">
								<label for="money">Amount: </label>
							</div>
						</div>
						<div class="row">
							<div class="input-field col s12">
								<button class="btn waves-effect waves-light" type="submit" name="action">
									add
									<i class="material-icons right">send</i>
								</button>
							</div>
						</div>
					</form>
				</div>
			</div>	
		</div>
	</body>
</html>