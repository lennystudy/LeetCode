<?php
/**
* 测试类
*/
class A 
{
	
	function __construct()
	{
		# code...
	}

	function __set($name,$value){
		echo $name." ".$value;
		echo "hello";
	}
}

$a = new A();
$a->b = 1;
echo $a->b;