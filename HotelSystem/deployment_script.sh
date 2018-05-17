#!/bin/bash

##############################################################
#																		  #
#																		  #
#			      		HOSTEL ADMIN SYSTEM DEPLOYMENT SCRIPT				          #
#																		  #
#																		  #
##############################################################




echo "iInitialising the system...."

python3 manage.py makemigrations
sleep 2s
printf "\n"

python3 manage.py migrate
sleep 2s
printf "\n\n"

echo "You need to enter the details to create superuser...."
printf "\n"
python3 manage.py createsuperuser

printf "\n"
echo "wait for the server to start...."
sleep 1s
printf "\n"
echo "Initialising server...."
echo "Server Started. Visit http://127.0.0.1:8000/home"

python3 manage.py runserver &>> activity_logs.txt

