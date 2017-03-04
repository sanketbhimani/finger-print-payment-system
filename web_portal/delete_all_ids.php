<?php
	include("connect.php");
	if(isset($_GET['sek']) && $_GET['sek']!=""){
		$q = "TRUNCATE TABLE  `users`";
		mysql_query($q);
		$q = "TRUNCATE TABLE  `payment_data`";
		mysql_query($q);
		echo(1);
	}
	else{
		echo(0);
	}
	
?>