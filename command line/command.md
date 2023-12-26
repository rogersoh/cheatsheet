# compare 2 file
```
diff file1 file2
```

Compare 2 file and ignore whitespaces
```
diff -w file1 file2
```

# hexdump 

hexdump - display file contents in hexadecimal, decimal, octal, or ascii

### Description
The hexdump utility is a filter which displays the specified files, or standard input if no files are specified, in a user-specified format.

### Option
```
hexdump -C filename
```
"-C, --canonical
Canonical hex+ASCII display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, hexadecimal bytes, followed by the same sixteen bytes in %_p format enclosed in | characters. Invoking the program as hd implies this option.

## compress to zip file with password
Encrypt a zip file in the Mac Terminal

Open your Spotlight Search bar and search Terminal. ...
Type 
```
zip -er desiredfilename. ...
```
Drag and drop the folder, file or files you want to compress into a zip file into the Terminal window.
Press the Enter key.
Next you will be prompted to enter a password.