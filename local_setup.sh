if [ -d ".env" ]; 
then 
    echo ".env folder exists. Installing using pip"
else
    echo "creating .env and install using pip"
    python3 -m venv .env
fi

source .env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

deactivate