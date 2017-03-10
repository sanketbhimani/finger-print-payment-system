<?php

/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		logout.php
*
*/

//do logout
	session_start();
	unset($_SESSION);
   session_unset();
   session_destroy();
	
	header("location:index.php");
	
?>