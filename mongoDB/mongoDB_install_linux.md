# Install MongoDB Community Edition on Ubuntu
*NOTE*  

**MongoDB Atlas** is a hosted MongoDB service option in the cloud which requires no installation overhead and offers a free tier to get started.

## Overview
Use this tutorial to install MongoDB 7.0 Community Edition on LTS (long-term support) releases of Ubuntu Linux using the apt package manager.

## MongoDB Version
This tutorial installs MongoDB 7.0 Community Edition. To install a different version of MongoDB Community, use the version drop-down menu in the upper-left corner of this page to select the documentation for that version.

## Considerations
Platform Support
MongoDB 7.0 Community Edition supports the following 64-bit Ubuntu LTS (long-term support) releases on x86_64 architecture:

- 22.04 LTS ("Jammy")

- 20.04 LTS ("Focal")

MongoDB only supports the 64-bit versions of these platforms. To determine which Ubuntu release your host is running, run the following command on the host's terminal:

```cat /etc/lsb-release```

MongoDB 7.0 Community Edition on Ubuntu also supports the ARM64 architecture on select platforms.

See Platform Support for more information.

*Production Notes*  
Before deploying MongoDB in a production environment, consider the Production Notes document which offers performance considerations and configuration recommendations for production MongoDB deployments.

### Official MongoDB Packages
To install MongoDB Community on your Ubuntu system, these instructions will use the official mongodb-org package, which is maintained and supported by MongoDB Inc. The official mongodb-org package always contains the latest version of MongoDB, and is available from its own dedicated repo.

*IMPORTANT*  
The mongodb package provided by Ubuntu is not maintained by MongoDB Inc. and conflicts with the official mongodb-org package. If you have already installed the mongodb package on your Ubuntu system, you must first uninstall the mongodb package before proceeding with these instructions.

*See MongoDB Community Edition Packages for the complete list of official packages.*

## Install MongoDB Community Edition
Follow these steps to install MongoDB Community Edition using the apt package manager.

1 Import the public key used by the package management system
From a terminal, install gnupg and curl if they are not already available:

```sudo apt-get install gnupg curl```

To import the MongoDB public GPG key from 
https://pgp.mongodb.com/server-7.0.asc
, run the following command:

```
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
```

2 Create a list file for MongoDB
Create the list file /etc/apt/sources.list.d/mongodb-org-7.0.list for your version of Ubuntu.

#### Ubuntu 22.04 (Jammy)
Create the /etc/apt/sources.list.d/mongodb-org-7.0.list file for Ubuntu 22.04 (Jammy):
```
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```

3  Reload local package database
Issue the following command to reload the local package database:
```
sudo apt-get update
```

4  Install the MongoDB packages
You can install either the latest stable version of MongoDB or a specific version of MongoDB.

#### Install the latest version of MongoDB

Install a specific release of MongoDB
To install the latest stable version, issue the following
```
sudo apt-get install -y mongodb-org
```

Optional. Although you can specify any available version of MongoDB, apt-get will upgrade the packages when a newer version becomes available. To prevent unintended upgrades, you can pin the package at the currently installed version:
```
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-database hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-mongosh hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
```

#### Install different verison 

To install a specific release, you must specify each component package individually along with the version number, as in the following example:

```
sudo apt-get install -y mongodb-org=7.0.3 mongodb-org-database=7.0.3 mongodb-org-server=7.0.3 mongodb-mongosh=7.0.3 mongodb-org-mongos=7.0.3 mongodb-org-tools=7.0.3

```

If you only install mongodb-org=7.0.3 and do not include the component packages, the latest version of each MongoDB package will be installed regardless of what version you specified.

Optional. Although you can specify any available version of MongoDB, apt-get will upgrade the packages when a newer version becomes available. To prevent unintended upgrades, you can pin the package at the currently installed version:

```
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-database hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-mongosh hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
```

# Start MongoDB.
You can start the mongod process by issuing the following command:

```sudo systemctl start mongod```

If you receive an error similar to the following when starting mongod:

Failed to start mongod.service: Unit mongod.service not found.

Run the following command first:

sudo systemctl daemon-reload

Then run the start command above again.

# Verify that MongoDB has started successfully.
```sudo systemctl status mongod```

You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:

sudo systemctl enable mongod

# Stop MongoDB.
As needed, you can stop the mongod process by issuing the following command:

```sudo systemctl stop mongod```

4
Restart MongoDB.
You can restart the mongod process by issuing the following command:

sudo systemctl restart mongod

You can follow the state of the process for errors or important messages by watching the output in the /var/log/mongodb/mongod.log file.

5  Begin using MongoDB.  
Start a mongosh session on the same host machine as the mongod. You can run 
mongosh
 without any command-line options to connect to a mongod that is running on your localhost with default port 27017.

mongosh

For more information on connecting using 
mongosh
, such as to connect to a mongod instance running on a different host and/or port, see the 
mongosh documentation.

To help you start using MongoDB, MongoDB provides Getting Started Guides in various driver editions. For the driver documentation, see 
Start Developing with MongoDB.
For help with troubleshooting errors encountered while installing MongoDB on Ubuntu, see our troubleshooting guide.

### Run MongoDB Community Edition
ulimit Considerations
Most Unix-like operating systems limit the system resources that a process may use. These limits may negatively impact MongoDB operation, and should be adjusted. See UNIX ulimit Settings for the recommended settings for your platform.

NOTE
Starting in MongoDB 4.4, a startup error is generated if the ulimit value for number of open files is under 64000.

Directories
If you installed through the package manager, the data directory /var/lib/mongodb and the log directory /var/log/mongodb are created during the installation.

By default, MongoDB runs using the mongodb user account. If you change the user that runs the MongoDB process, you must also modify the permission to the data and log directories to give this user access to these directories.

Configuration File
The official MongoDB package includes a configuration file (/etc/mongod.conf). These settings (such as the data directory and log directory specifications) take effect upon startup. That is, if you change the configuration file while the MongoDB instance is running, you must restart the instance for the changes to take effect.

Procedure
Follow these steps to run MongoDB Community Edition on your system. These instructions assume that you are using the official mongodb-org package -- not the unofficial mongodb package provided by Ubuntu -- and are using the default settings.

Init System

To run and manage your mongod process, you will be using your operating system's built-in init system. Recent versions of Linux tend to use systemd (which uses the systemctl command), while older versions of Linux tend to use System V init (which uses the service command).

If you are unsure which init system your platform uses, run the following command:

ps --no-headers -o comm 1

Then select the appropriate tab below based on the result:

systemd - select the systemd (systemctl) tab below.

init - select the System V Init (service) tab below.



systemd (systemctl)

System V Init (service)
1
Start MongoDB.
You can start the mongod process by issuing the following command:

sudo systemctl start mongod

If you receive an error similar to the following when starting mongod:

Failed to start mongod.service: Unit mongod.service not found.

Run the following command first:

sudo systemctl daemon-reload

Then run the start command above again.

2
Verify that MongoDB has started successfully.
sudo systemctl status mongod

You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:

sudo systemctl enable mongod

3
Stop MongoDB.
As needed, you can stop the mongod process by issuing the following command:

sudo systemctl stop mongod

4
Restart MongoDB.
You can restart the mongod process by issuing the following command:

sudo systemctl restart mongod

You can follow the state of the process for errors or important messages by watching the output in the /var/log/mongodb/mongod.log file.

5
Begin using MongoDB.
Start a 
mongosh
 session on the same host machine as the mongod. You can run 
mongosh
 without any command-line options to connect to a mongod that is running on your localhost with default port 27017.

mongosh

For more information on connecting using 
mongosh
, such as to connect to a mongod instance running on a different host and/or port, see the 
mongosh documentation.

To help you start using MongoDB, MongoDB provides Getting Started Guides in various driver editions. For the driver documentation, see 
Start Developing with MongoDB.

Uninstall MongoDB Community Edition
To completely remove MongoDB from a system, you must remove the MongoDB applications themselves, the configuration files, and any directories containing data and logs. The following section guides you through the necessary steps.

WARNING
This process will completely remove MongoDB, its configuration, and all databases. This process is not reversible, so ensure that all of your configuration and data is backed up before proceeding.

1
Stop MongoDB.
Stop the mongod process by issuing the following command:

sudo service mongod stop

2
Remove Packages.
Remove any MongoDB packages that you had previously installed.

sudo apt-get purge "mongodb-org*"

3
Remove Data Directories.
Remove MongoDB databases and log files.

sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb

Additional Information
Localhost Binding by Default
By default, MongoDB launches with bindIp set to 127.0.0.1, which binds to the localhost network interface. This means that the mongod can only accept connections from clients that are running on the same machine. Remote clients will not be able to connect to the mongod, and the mongod will not be able to initialize a replica set unless this value is set to a valid network interface which is accessible from the remote clients.

This value can be configured either:

in the MongoDB configuration file with bindIp, or

via the command-line argument --bind_ip

WARNING
Before you bind your instance to a publicly-accessible IP address, you must secure your cluster from unauthorized access. For a complete list of security recommendations, see Security Checklist. At minimum, consider enabling authentication and hardening network infrastructure.

For more information on configuring bindIp, see IP Binding.

MongoDB Community Edition Packages
MongoDB Community Edition is available from its own dedicated repository, and contains the following officially-supported packages:

Package Name
Description
mongodb-org
A metapackage that automatically installs the component packages listed below.
mongodb-org-database
A metapackage that automatically installs the component packages listed below.

Package Name
Description
mongodb-org-server
Contains the mongod daemon, associated init script, and a configuration file (/etc/mongod.conf). You can use the initialization script to start mongod with the configuration file. For details, see the "Run MongoDB Community Edition" section, above.
mongodb-org-mongos
Contains the mongos daemon.
mongodb-mongosh
Contains the MongoDB Shell (
mongosh
).
mongodb-org-tools
A metapackage that automatically installs the component packages listed below:

Package Name
Description
mongodb-database-tools
Contains the following MongoDB  

# link example
[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com