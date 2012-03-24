<?php
/* This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details */
 
// Written by devast8a <devast8a[at]whitefirex.com>
/////////////////////////////////////////////////////////////////////
/** EDIT SETTINGS HERE **/
/////////////////////////////////////////////////////////////////////

// Path to log files
$path = "";

// Timezone to set to
$timezone = "Australia/Adelaide";

// if "true" then grab all files
$sAll = $_GET["all"];

// if "true" then include files generated today
$sToday = $_GET["today"];

/////////////////////////////////////////////////////////////////////
/** STOP EDITTING SETTING HERE **/
/////////////////////////////////////////////////////////////////////

include("grabbed.php");
include("Tar.php");

date_default_timezone_set($timezone);

$files = scandir($path);
$date = date("Ymd");
$session = Array();

if($sAll=="true"){
    $grabbed = Array();
}

foreach( $files as $file ){
    if($file == "." || $file == ".."){
        continue;
    }
    if( in_array($file, $grabbed) ){
        continue;
    }
    $fullpath = $path.$file;
    
    if( is_file( $fullpath ) ){
        $b = basename($fullpath,".log");
        if( $date == substr($b,strlen($b)-strlen($date)) ){
            if($sToday!="true"){
                continue;
            }
        }else{
            array_push($grabbed, $file);
        }
        
        array_push($session, $fullpath);
    }
}

if( count($session) ){
    echo "No files to grab";
    die();
}

// Write to grabbed.php
$output = "<?php\r\n\$files = Array(\r\n";
foreach( $grabbed as $file ){
    $output .= "\"$file\",\r\n";
}
$output .= "); ?>";
file_put_contents("grabbed.php", $output);

// Create archive
$ar = new Archive_Tar("log.tar.gz", "gz");
$ar->createModify($session,"",$path);

header("Content-Type: application/x-gzip");
header("Content-Disposition: attachment; filename=log.tar.gz");

echo file_get_contents("log.tar.gz");
unlink("log.tar.gz");

?>