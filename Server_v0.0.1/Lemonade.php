<?php
echo "<html><body>Your order has been placed! Thank you!</body></html>";
$file = 'queue.txt';
// Open the file to get existing content
$current = file_get_contents($file);
// Append a new person to the file
$current .= "Lemonade\n";
// Write the contents back to the file
file_put_contents($file, $current);
?>