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
	if($a['name']==""){
		header("location:add_name.php");
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
	<?php
		if(isset($_GET['done'])){
			echo("<script>alert('Your account is successfully credited');</script>");
		}
	?>
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
			<h3 class="center" style="margin-top: 30px;">Welcome, <?php echo($a['name']); ?></h3>
			<h4 class="center" style="margin-top: 30px;">Current balance: <?php echo($a['balance']); ?></h4>
			<a href="add_money.php" class="center waves-effect waves-light btn-large">add money</a>
			<br><br>
			<?php $cnt = 0; ?>
			<table class="striped centered responsive-table">
				<thead>
					<tr>
						<th>ID</th>
						<th>Amount</th>
						<th>Date</th>
						<th>Debited/Credited</th>
					</tr>
				</thead>
				<tbody>
				<?php
					$q = "SELECT * FROM `payment_data` WHERE `users_id` = '".$_SESSION['users_id']."' ORDER BY `id` DESC";
					$f = mysql_query($q);
					while($a = mysql_fetch_array($f)){
						$cnt++;
				?>
					<tr>
						<td><?php echo($cnt); ?></td>
						<td><?php echo($a['amount']); ?></td>
						<td><?php echo($a['date']); ?></td>
						<td><?php echo($a['debit_credit']); ?></td>
					</tr>
				<?php
					}
				?>
				</tbody>
			</table>
		</div>
	</body>
</html>