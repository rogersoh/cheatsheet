# bio_io databases setup

## run mongodb service
```sudo systemctl start mongod```

## uncompress tar database
```tar -xvzf bioio_dump.tar.gz```

## restore database to mongodb
```mongorestore --gzip bioio_dump```