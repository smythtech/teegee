# TeeGee: Token Generator
TeeGee is a tool for generating random tokens or strings. Rules can be defined for the generated token to allow TeeGee to generate passwords, MAC addresses, URLS, ID numbers, etc.

# Usage

| Option | Description |
|--------|:-----------:|
| -t | Length of token |     
| -l |      Include lowercase letters |
| -u |    Include uppercase letters |
| -n |    Include numbers |
| -s |    Include symbols(!"$*(){}[]<>~) |
| -c |    Include custom characters |
| -r |    Repeat x times |
| -p |    Preappend to token |
| -a |    Append to token |
| -g |    Seperate token into groups of x size |
|-d  |   Divider for groups (Default is a space) |

# Examples

## Generating passwords
```
$./teegee.py -t 8 -l -u -n
Ueg8m8kb
$
$./teegee.py -t 12 -l -u -n -s
QzSTQvs(DT]S 
$
```

## Generating MAC addresses

A MAC address is 6 bytes in length. If we look at a MAC address in terms of it being a string, it contains 12 hex characters (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E, and F) divided into 6 groups of two characters, with each group seperated by a colon.
To generate one we just need to define those rules for teegee. We can use the '-c' option to specify the hex characters, the '-g' option to device the string into groups of two characters, and use the '-d' option to seperate the groups with colons.
The command will then look like the following...
```
$./teegee.py -t 12 -c 0123456789abcdef -g 2 -d ":"
b8:d1:a3:49:d5:85 
$
```

## Generating .onion addresses

If we believe Wikipedia and look at how the .onion address should be formatted, we can see that it's said here: "These 16-character hashes can be made up of any letter of the alphabet, and decimal digits from 2 to 7". So it's 16 characters in length (-t 16), can contain any letter in the alphabet (-l), and has numbers ranging from 2-7 (-c 234567). Now, it's a URL we're generating so we need to preappend 'http://' to the start and '.onion' to the end. We can do this using the '-p' and '-a' options. Putting everything together we'll end up with a command like this...
```
$./teegee.py -t 16 -c 234567 -l -p "http://" -a ".onion"
http://ktlj2pt7akf5btng.onion
$
```
