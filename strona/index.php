<html>
        <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8">
                <title>Raspberry Pi remote control</title>
                <style>
                        body {font-family: arial;}
                        td {text-align: center;}
                </style>
        </head>
        <body>
                <center>
                        <img src="logo.jpg">
                        <br>
                        <br>


<?php

function TglControl($val, $name)
{
        if ($val == 1)
                echo '<a href="?'.$name.'=0"><img src="on.jpg"></a>';
        else
                echo '<a href="?'.$name.'=1"><img src="off.jpg"></a>';
}

shell_exec('gpio -g mode 24 out');
shell_exec('gpio -g mode 25 out');

$out1val = shell_exec('gpio -g read 24');
$out2val = shell_exec('gpio -g read 25');

if (isset($_GET['out1']))
{
        if ($_GET['out1']) $out1val = 1; else $out1val = 0;
        shell_exec('gpio -g write 24 '.$out1val);
}

if (isset($_GET['out2']))
{
        if ($_GET['out2']) $out2val = 1; else $out2val = 0;
        shell_exec('gpio -g write 25 '.$out2val);
}
?>


                        <table width="350">
                                <tr><td width="50%"><b>Linia 1</b></td><td width="50%"><b>Linia 2</b></td></tr>
                                <tr><td><?php TglControl($out1val, "out1"); ?></td><td><?php TglControl($out2val, "out2"); ?></td></tr>
                        </table>
                </center>
        </body>
</html>

