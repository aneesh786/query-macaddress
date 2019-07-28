# query-macaddress

This is a simple python script to query a mac address and output vendor information
This uses Python2.7
Example for running this script : 
```sh
python mac-query.py 44:38:39:ff:ef:57 at_Nz5rzTVK1Y4c4cXEYr4
```
##Here Mac address is the first Argument & second Argument for API Token. Anybody who executes this query will need an API Token from https://macaddress.io. Token given here is a sample one which won't work.###
# Dockerfile
Also dockerfile to dockerize this python script is provided.

Steps to create a docker image 
#############################
1. Keep Dockerfile & mac-query.py files on same folder
2. Execute below commands :
```sh
  sudo docker build -t macaddress .
  sudo docker run macaddress1 python mac-query.py 44:38:39:ff:ef:57 at_Nz5rzTVK1Y4c4cXEYr
```
