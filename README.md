# AirBnB Clone

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230306%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230306T054218Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5a40d16061e6b14b03ac2c7f86355823fa0c8688982c62dea0953149dcffb464)

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

Rayan Bhaa ([@Rayan-bhaa](https://github.com/Rayan-bhaa))
Brian M'Ikiara ([@brian-ikiara](https://github.com/brian-ikiara))
