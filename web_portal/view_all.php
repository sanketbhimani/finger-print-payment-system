<?php


/*
*
* Project Name: 	touch-n-pay
* Author List: 		sanket bhimani, arnest vekariya, keyur rakholiya
* Filename: 		view_all.php
*
*/


?>


<html>
<body>
<table border='1'>
<tr>
<td>id</td>
<td>name</td>
<td>balance</td>
<td>mobile no.</td>
<td>password</td>
<td>finger print id</td>
</tr>
<?php
include("connect.php"); //create connection with database
	//get details of all users
$q = "SELECT * FROM `users`";;
$f = mysql_query($q);
while($a = mysql_fetch_array($f)){
	?>
	<tr>
	<?php
		echo("<td>".$a['id']."</td>");
		echo("<td>".$a['name']."</td>");
		echo("<td>".$a['balance']."</td>");
		echo("<td>".$a['mobile_no']."</td>");
		echo("<td>".$a['password']."</td>");
		echo("<td>".$a['finger_print_id']."</td>");
	?>
	</tr>
	<?php
}


?>
</table>
<a href="delete_all_ids.php?sek=bhochu">delete all</a>
</body>
</html>