<?php
	include("connect.php");
	session_start();
	if(!isset($_SESSION['users_id'])){
		header("location:index.php");
		die();
	}
	$q = "SELECT * FROM `users` WHERE `id` = '".$_SESSION['users_id']."'";;
	$f = mysql_query($q);
	$a = mysql_fetch_array($f);
	
	if(isset($_POST['name']) && $_POST['name'] != ""){
		
		$name = mysql_real_escape_string($_POST['name']);
		
		$q = "UPDATE `users` SET `name` = '".$name."' WHERE `id` = '".$_SESSION['users_id']."'";
		mysql_query($q);
		header("location:home.php");
		die();
		
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
				<center style="position:absolute; margin:auto; left:0; right:0;">
					<span style="font-size: 2em;">Touch n Pay</span>
				</center>
				<ul id="nav" style="margin-right: 3%;" class="right">
					<li><a href="logout.php">Logout</a></li>
				</ul>
			</div>
		</nav>
		<div class="container">
			<h4 class="center" style="margin-top: 30px;">Enter Your Name</h4>
			<div class="row" style="margin-top: 30px;">
				<div class="offset-s3 col s6">
					<form action="add_name.php" method="post">
						<div class="row">
							<div class="input-field col s12">
								<input id="name" type="text" name="name" class="validate">
								<label for="name">Your Name: </label>
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