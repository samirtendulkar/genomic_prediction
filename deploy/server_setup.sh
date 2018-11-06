#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/samirtendulkar/genomic_prediction.git'

PROJECT_BASE_PATH='/home/samir/PycharmProjects/'
VIRTUALENV_BASE_PATH='/home/samir/PycharmProjects/'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git postgresql postgresql-contrib

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/profiles-rest-api

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/GenomeVenv

$VIRTUALENV_BASE_PATH/profiles_api/bin/pip install -r $PROJECT_BASE_PATH/genomic_prediction/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/genomic_prediction/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/genomic_prediction/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/gp.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/genomic_prediction/deploy/nginx_gp.conf /etc/nginx/sites-available/gp.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/gp.conf /etc/nginx/sites-enabled/gp.conf
systemctl restart nginx.service

echo "DONE! :)"