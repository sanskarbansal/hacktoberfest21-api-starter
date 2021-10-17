#! /bin/sh
if [ -d '.env' ]; 
then 
    echo "Enabling virtual env"
else
    echo "No virtual env. Please run local_setup.sh first"
fi

source .env/bin/activate

export ENV=development
python main.py
deactivate