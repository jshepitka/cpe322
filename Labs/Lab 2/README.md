# Lab 2

[Kevin Lu - Internet of Things Repository](https://github.com/kevinwlu/iot)

```$ hostname ```

- provided the name I gave to identify my laptop "JOHNNY-LAPTOP"

```$ env```

- returned even more information about my system and the git bash terminal used to execute this command and the others for  this lab.

```$ ps```

- "Process Status" listed the running processes along with other information such as PID, PPID, WINID, UID, start time.

```$ git clone https://github.com/kevinwlu/iot.git```

- cloned the professor Lu's IoT repository into the Lab 2 folder.

```
$ cd iot
$ ls
$ cd
```

- navigated to the iot folder created after cloning the repository, listed the contents of the directory and then returned to the highest directory.

- ```df``` (disk filesystem) shows the disk space number of blocks (1kb size) and the amount of space used/available in the file system.


```
$ mkdir demo
$ cd demo
$ nano file
```

- ```$ mkdir demo``` creates a folder called demo in your current directory.
- ```$ cd demo``` goes into this newly created folder, and ```$ nano file``` opens up a simple text editor, nano and creates a file name file.

![image](https://user-images.githubusercontent.com/37707211/235468618-f75712a8-e332-48c2-b18a-b93443ac53f1.png)

-```$ cat file``` then reads the file "file" and would output the text but it was empty in my case. ```$ cp file file1``` then copies "file" to "file1". ```$ mv``` moves a file to another directory. ```$ rm file2``` removes the file2.

-```$ clear``` will clear the terminal.

-```$ man uname ``` man command could not be found.

-```uname -a``` returned the system information and information about the terminal (git bash) being used.

-```$ ifconfig``` is not a command in git bash but ```$ ipconfig``` is the equivalent command which returns network information about your system. things such as IPv4 Address and other ethernet information is shown.

- ```$ ping localhost``` pings you own system (localhost) and shows the time each reply takes. because it is local the time was less than 1ms. The command also shows the number of packets sent, received, and lost. other statics also shown.net

-```$ netstat``` lists active connections and the local address, foreign address and state of each connection.

[Link back to main README](https://github.com/jshepitka/cpe322/blob/main/README.md)
