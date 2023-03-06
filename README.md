# AirBnB Clone

![HBnB](hbnb.png)

## General Idea

```sh
	vagrant@ubuntu-focal:~/AirBnB_clone$ ./console.py # interactive mode
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF	help	quit	create	show 	update	all 	destroy

	(hbnb)
	(hbnb) quit
	vagrant@ubuntu-focal:~/AirBnB_clone$ echo "help" | ./console.py # non-interactive mode
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF	help	quit	create	show 	update	all 	destroy
	(hbnb)
	vagrant@ubuntu-focal:~/AirBnB_clone$ cat test_help
	help
	vagrant@ubuntu-focal:~/AirBnB_clone$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF	help	quit	create	show 	update	all 	destroy
	(hbnb)
	vagrant@ubuntu-focal:~/AirBnB_clone$
```

## A brief overview

This project is both the backend and frontend implementation of the [AirBnB](https://www.airbnb.com) site. It will show the basics of handling user data and will be like a precursor to the database management.

The following actions are possible with our clone:

| Action | Description |
| -- | -- |
| `create <class_name>` | Creates an object of a given class |
| `show <class_name> <id>` | Displays object(s) description |
| `update <class_name> <id> <attribute_name> <attribute_value>` | Modifies an attribute of an object |
| `all <class_name>` | Displays every instance of objects created in a session |
| `destroy <class_name> <id>` | Deletes an object |

## Sidebar

Looking forward to this project. Hope it goes well. :grinning:

## Authors

* Rayan Bhaa ([@Rayan-bhaa](https://github.com/Rayan-bhaa))
* Brian M'Ikiara ([@brian-ikiara](https://github.com/brian-ikiara))
