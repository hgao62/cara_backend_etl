#!/usr/bin/env bash
airflow db init
airflow users create --username admin --password admin --firstname kobe --lastname Gao --role Admin --email hgao62@uwo.ca
airflow webserver -p 8080
echo "Airflow webserver is running"

# sleep 10
# echo "About to run Airflow scheduler"
# airflow scheduler
# echo "Airflow scheduler is running"