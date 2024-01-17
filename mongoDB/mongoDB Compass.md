# Compass
## Start Compass from the Command Line
You can start a Compass session from the command line.

In enterprise environments, a scripted start can make it easier to deploy Compass. For example, to limit access to sensitive systems, you can configure a command line start so that Compass can run on a jump host.

There are two ways to start Compass from the command line:

1. Specify a connection string on the command line

2. Specify connection details in a file

If your connection string contains sensitive information, consider using a configuration file to avoid exposing that information on the command line.

## Compass Executable Location
The name and location of the Compass executable varies by operating system.

| Operating System | Executable Name | Location |
|------|-----|------|
| Linux | mongodb-compass | The installer installs it in the /usr/bin directory.|
| Windows | MongoDBCompass.exe | The installer installs it in a folder you pick during the installation process. |
| MacOS | MongoDB Compass | The installer installs it under the Applications folder:  => /Applications/MongoDB\ Compass.app/Contents/MacOS/MongoDB\ Compass |


## Command Line Connection Specification
The command line invocation for Compass has two components, the path to the Compass executable and a connection string. You can optionally provide the username and password on the command line or the configuration file. The format is:
```
 <path/to/compass/executable>
 <connection string>
 --username <username> --password <password>
 ```
*NOTE*  
If the username and password arguments are not provided, Compass uses the credentials in the connection string.

Basic Connection String  
The following example uses a basic connection string for a 
MongoDB University training cluster. Modify the connection details to connect to your MongoDB installation:
```
mongodb-compass mongodb+srv://cluster0.xxxxxx.mongodb.net/library
```

Username and Password Parameters  
This example uses the username and password parameters to authenticate Compass to the MongoDB deployment provided in the connection string:

```
mongodb-compass mongodb+srv://cluster0.xxxxxx.mongodb.net/library
--username user1 --password password1
```

Configuration File Connection Specification  
The command line invocation for Compass can specify a configuration file.

The format is:
```
<path/to/compass/executable> \
   --file=<filename> \
   [--passphrase=<passphrase>] \
   [<connection id>]
```

The components of the command invocation are:

The path to the Compass executable

- A connection configuration file
- An optional passphrase for the connection configuration file
- An optional connection id
- To create the connection configuration file, follow the steps to export the 
connection details from your Compass instance. The export process creates a file 
that includes all of your favorite connections.  

*IMPORTANT*  
If you export your saved connections without using a passphrase, the configuration file 
contains the plaintext version of your username and password. Use a passphrase to 
encrypt the password.

To open Compass and connect to your MongoDB instance, use a command line like:
```
mongodb-compass --file=learningConnectionFile \
                --passphrase=superSecret
 ```               
If you have multiple favorites, include the connection id from the configuration file to specify which connection to use:
```
mongodb-compass --file=multipleConnectionFile \
                --passphrase=superSecret \
                27ba0eda-c27e-46f5-a74a-2c041b1b58c4
                ```