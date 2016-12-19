Shell Scripting Basics
======================

Variables
---------
#Declaration
	variable = something
#Use
	$variable

Capturing STDOUT
----------------
you can capture stdout using the > operator

if statment
-----------
**if** [commands]; **then**
	commands
[**elif** commands; **then**
	commands...]
[**else**
	commands...]
**fi**

case statement
--------------
**case** word **in**
	patterns | patterns**)** commands
	;;
**esac**

for loop
--------
**for** variable **in** words; **do**
	commands
**done**

while loop
----------
**while** [conditional]; **do**
	commands...
**done**

function
--------
#**NOTE** functions must be defined before they are used in the script
function_name(){
	commands...
}

trap
----
**trap** arg signals
#**signals** is a list of signals to intercept
#**arg** is a command to execute when one of the signals is received