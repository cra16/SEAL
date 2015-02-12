<?php
	$connection = mysql_connect("localhost", "root", "111111");
	$db = mysql_select_db("courseinfo", $connection)
	$data1 = $_POST['data1'];
	$data2 = $_POST['data2'];
	$data3 = $_POST['data3'];
	$data4 = $_POST['data4'];
	$data5 = $_POST['data5'];
	$data6 = $_POST['data6'];

	$query = "INSERT INTO coursedata (data1, data2, data3, data4, data5, data6) VALUES ('$data1', '$data2', '$data3', '$data4', '$data5', '$data6')";
	$result = mysql_query($query);
	if (!$result) {
	    $message  = 'Invalid query: ' . mysql_error() . "\n";
	    $message .= 'Whole query: ' . $query;
	    die($message);
	}

	if ($result != FALSE){
		echo "Successfully scored";
	} else {
		echo 0;
	}

	mysql_close($connection);

?>