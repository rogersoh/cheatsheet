# mongoDB cheatsheet

## Installation instruction
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/

## To run MongoDB (i.e. the mongod process) as a macOS service, run:
```
brew services start mongodb-community@7.0
```

## To stop MongoDB running as a macOS service, run
```
brew services stop mongodb-community@7.0
```

## To verify that MongoDB is running, perform one of the following:

If you started MongoDB as a macOS service:
```
brew services list
```