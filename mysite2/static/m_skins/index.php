<?php 
	$connection = mysql_connect("localhost", "root", "111111");
	$db = mysql_select_db("courseinfo", $connection);


	$query = "SELECT id, data1, data2, data3, data4, data5, data6 FROM coursedata";
	$result = mysql_query($query);
	if (!$result) {
	    $message  = 'Invalid query: ' . mysql_error() . "\n";
	    $message .= 'Whole query: ' . $query;
	    die($message);
	}

	$sum = array(0, 0, 0, 0, 0, 0);
	$avg = array(0, 0, 0, 0, 0, 0);
	$count = array(0, 0, 0, 0, 0, 0);


	while($row = mysql_fetch_assoc($result)){
		if($row['data1'] != 0){
			$sum[0] += $row['data1'];
			$count[0] += 1;
		}
		if($row['data2'] != 0){
			$sum[1] += $row['data2'];
			$count[1] += 1;
		}
		if($row['data3'] != 0){
			$sum[2] += $row['data3'];
			$count[2] += 1;
		}
		if($row['data4'] != 0){
			$sum[3] += $row['data4'];
			$count[3] += 1;
		}
		if($row['data5'] != 0){
			$sum[4] += $row['data5'];
			$count[4] += 1;
		}
		if($row['data6'] != 0){
			$sum[5] += $row['data6'];
			$count[5] += 1;
		}
	}

	for ($i = 0; $i < 6; $i++){
		$avg[$i] = round($sum[$i] / $count[$i]);
	}
	
	$avg = implode(",", $avg);

	echo $avg;