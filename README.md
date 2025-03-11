# Python with SQL Alchemy

#### Project on using SQL alchemy with python and MySQL database on docker.

## Setup:
- Install requirements.txt
```commandline
pip install -r requirements.txt
```
- Create MySql database on docker
```commandline
docker pull mysql
```
- Run MySQL container
```commandline
docker run -p 3306:3306 --name mysql-d -e MYSQL_ROOT_PASSWORD=password -d mysql
```
- Create config.ini file in the project root directory like below:
```
[database]
port = 3306
host = localhost
username = root
name = mysql
password = password
```

#### Check is database available by running:
```commandline
mysql -h 127.0.0.1 -P 3306 -ppassword -uroot
```

## Methods created:
- add_item()
- add_items()
- retrieve_all_items()
- retrieve_all_items_as_dict()
- remove_item()
- show_all_tables()
- write_to_csv()
