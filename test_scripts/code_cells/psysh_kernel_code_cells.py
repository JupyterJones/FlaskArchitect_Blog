pip install psysh_kernel
python -m psysh_kernel install --user
python -m psysh_kernel install
[Errno 13] Permission denied: '/usr/local/share/jupyter'
Perhaps you want to install with `sudo` or `--user`?
(base) jack@jack-Desktop:~/Desktop/pas.bak$ python -m psysh_kernel install --user
[InstallKernelSpec] Installed kernelspec psysh in /home/jack/.local/share/jupyter/kernels/psysh


  help       Show a list of commands. Type `help [foo]` for information about [foo].      Aliases: ?                     
  ls         List local, instance or class variables, methods and constants.              Aliases: dir                   
  dump       Dump an object or primitive.                                                                                
  doc        Read the documentation for an object, class, constant, method or property.   Aliases: rtfm, man             
  show       Show the code for an object, class, constant, method or property.                                           
  wtf        Show the backtrace of the most recent exception.                             Aliases: last-exception, wtf?  
  whereami   Show where you are in the code.                                                                             
  throw-up   Throw an exception or error out of the Psy Shell.                                                           
  timeit     Profiles with a timer.                                                                                      
  trace      Show the current call stack.                                                                                
  buffer     Show (or clear) the contents of the code input buffer.                       Aliases: buf                   
  clear      Clear the Psy Shell screen.                                                                                 
  edit       Open an external editor. Afterwards, get produced code in input buffer.                                     
  sudo       Evaluate PHP code, bypassing visibility restrictions.                                                       
  history    Show the Psy Shell history.                                                  Aliases: hist                  
  exit       End the current session and return to caller.   

ls

help

buffer clear

$myArr = [];

//array_push($myArr, 5, 8);



$filename = "NOTE"
$handle = fopen($filename, "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        // process the line read.
        array_push($myArr,$line);
    }

    fclose($handle);
}


$myArr; 

if ($file = fopen("NOTE", "r")) {
    while(! feof($file)) 
    { $line = fgets($file);
     echo ("$line"); } 
    fclose($file); } 

$filename = "NOTE"
$handle = fopen($filename, "r+");

//In relation to error in fread, try

if (filesize($filename) > 0) {
$content = fread($handle, filesize($filename));
fclose($handle);

//echo $content; 
foreach ([$content] as $data) {
echo "$data \n";
}    
    
}


$AmazingCreature = ['Chumrucker', 'Succulator', 'Bazalett', 'Quizon'];

foreach ($AmazingCreature as $data) {
echo "$data \n";
}

$attributes = array("skinny", "fat", "smart", "dumb");

foreach ($attributes as $value) {
  echo "$value <br>";
}
echo "\n----------------------\n"
foreach ($attributes as $trait) {
  echo "$trait \n";
}
echo "\n----------------------\n"
echo $attributes[2];

%lsmagic

%magic

%%shell
ls 

%%shell
cd ..
ls -rant NOTEBOOKS

!pwd

$ds = new DOM



