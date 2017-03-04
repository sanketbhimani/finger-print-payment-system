<?php
	include("connect.php");
	if(isset($_POST['user_id']) && isset($_POST['pass']) && $_POST['user_id'] != "" && $_POST['pass'] != ""){
		$user_id = mysql_real_escape_string($_POST['user_id']);
		$pass = mysql_real_escape_string($_POST['pass']);
		$q = "SELECT * FROM `users` WHERE `id` = '".$user_id."' AND `password` = '".$pass."'";
		$f = mysql_query($q);
		$number = mysql_num_rows($f);
		if($number > 0){
			$a = mysql_fetch_array($f);
			session_start();
			$_SESSION['users_id'] = $a['id'];
			header("location:home.php");
			die();
		}
		else{
			header("location:index.php?error=1");
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
	<?php
		if(isset($_GET['error'])){
			echo("<script>alert('Invalid username or password');</script>");
		}
	?>
		<nav class="red lighten-1">
			<div class="nav-wrapper">
				<center>
					<span style="font-size: 2em;">Touch n Pay</span>
				</center>
			</div>
		</nav>
		<div class="container">
			<h3 class="center" style="margin-top: 30px;">User Login</h3>
			<div class="row" style="margin-top: 30px;">
				<div class="offset-s3 col s6">
					<form action="index.php" method="post">
						<div class="row">
							<div class="input-field col s12">
								<input id="user_id" type="text" name="user_id" class="validate">
								<label for="user_id">Username: </label>
							</div>
						</div>
						<div class="row">
							<div class="input-field col s12">
								<input id="pass" type="password" name="pass" class="validate">
								<label for="pass">Password: </label>
							</div>
						</div>
						<div class="row">
							<div class="input-field col s12">
								<button class="btn waves-effect waves-light" type="submit" name="action">
									Submit
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