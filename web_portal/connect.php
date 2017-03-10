<?php

/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		connect.php
* Global Variables: host: host of databse, uname: username of database, pass: password of database
*/





$host = "localhost";
$uname = "root";
$pass = "YouCanWin@123";
//make connection with database
$dbhandle = mysql_connect($host,$uname,$pass)
  or die("Unable to connect to MySQL");

mysql_select_db("touch-n-pay",$dbhandle) 
  or die("Could not select examples");
?>