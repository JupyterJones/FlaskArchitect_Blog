https://psysh.org/#install

c.execute("CREATE VIRTUAL TABLE PROJECT using FTS4 (input,sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")

//$dir = 'sqlite:/[YOUR-PATH]/combadd.sqlite';
$dir = 'sqlite:/home/jack/Desktop/pas.bak/ALLnotes.db';
$dbh  = new PDO($dir) or die("cannot open the database");
$query =  "SELECT rowid, * FROM PROJECT";
foreach ($dbh->query($query) as $row)
{
    if (strpos($row[1],'command:') !== false) {
    echo $row[0],": ",$row[1],"\n";
    echo "-----------------------\n";
}
}
$dbh = null; //This is how you close a PDO connection

//$dir = 'sqlite:/[YOUR-PATH]/combadd.sqlite';
$dirn = 'sqlite:/home/jack/Desktop/pas.bak/ALLnotes.db';
$dbhn  = new PDO($dirn) or die("cannot open the database");
$query =  "SELECT rowid, * FROM PROJECT;
foreach ($dbhn->query($query) as $row)
{
    if (row[1] contains "www"){ 
    echo $row[0],": ",$row[1],"\n";
    echo "-----------------------\n";
}
}
$dbh = null; //This is how you close a PDO connection

//$dir = 'sqlite:/[YOUR-PATH]/combadd.sqlite';
$dir = 'sqlite:/home/jack/Desktop/pas.bak/ALLnotes.db';
$dbh  = new PDO($dir) or die("cannot open the database");
$query =  "SELECT rowid, * FROM PROJECT;
foreach ($dbh->query($query) as $row)
{
    $DATA =row[1];
    echo $DATA;
    if (strpos(row[1],'www') !== false) {
    echo 'Car exists.';
} else {
    echo 'No cars.';
}

}

$dbh = null; //This is how you close a PDO connection

var img1 = $$("input[name='img1']")[0].value;

$a = readline('Enter a string: ');
 
// For output
echo $a;   

echo "What do you want to input? ";
$input = rtrim(fgets(STDIN));
//echo "I got it:\n" . $input;

%lsmagic

echo "Are you sure you want to do this?  Type 'yes' to continue: ";
$handle = fopen ("php://stdin","r");
$line = fgets($handle);
if(trim($line) != 'yes'){
    echo "ABORTING!\n";
    exit;
}
echo "\n";
echo "Thank you, continuing...\n";

file_get_contents('php://input');

readline('input your name');

$a = readline();

$val = "
<script>
document.write(document.querySelector('#user').value);
</script>
";
echo $val;

//    if (row[1] contains "www"){ 
//    echo $row[0],": ",$row[1],"\n";
//    echo "-----------------------\n";

