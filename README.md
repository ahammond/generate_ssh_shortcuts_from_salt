generate_ssh_shortcuts_from_salt
================================

You have a cloud of servers managed by salt.
You'd like to be able to ssh to them without dealing with DNS issues or hacking your hosts file.
Generate a .ssh/config file full of aliases to make this easy.

Example Output
--------------

```
Host minecraft
    HostName 50.57.88.90

Host other
    HostName 1.2.3.4
```
