<?php



/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		delete_all_ids.php
*
*/





	include("connect.php"); //create connection with database
	
	//check parameters for security reason
	if(isset($_GET['sek']) && $_GET['sek']!=""){
		//delete alll ids
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