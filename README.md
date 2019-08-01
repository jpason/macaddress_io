Simple script to decode Company Name associated with MAC address.
------------------------------------------------------------------


How to use it:

1. Register at https://macaddress.io to get your API key.
2. Save it in a file named `api_key`.
2. To make sure nobody steals your key, api_key file needs to be encrypted, so encrypt it with inluded `encrypt_api_key.py` script
4. (OPTIONAL) Build docker container using included Dockerfile, then run it with `docker run -it` to test the script.
5. Run `./macaddress_io.py` SOME_MAC_ADDRESS


macaddress_io.py should work in both python 2.7 and python 3.x
