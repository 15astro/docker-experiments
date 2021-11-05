# docker-experiments
Repo to document all experiments with Docker

# Docker Volumes
- Create mysql container without any volume, create db, stop container data check data
  
  ```docker run --platform linux/x86_64 -e MYSQL_ALLOW_EMPTY_PASSWORD=true -d mysql```
  
  ```docker exec -it 1d728 mysql``` 
  
  ```docekr ps```
  
  ```docker stop a5ff6e5baa98```
  
  
- Create mysql cotainer with bind mount, create db, stop container and check data

  ```docker run --platform linux/x86_64 -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v $(pwd)/mysql-data:/var/lib/mysql -d  mysql ```
  
  ```docker ps ```

  ```docker exec -it 81aa mysql ```


- Create mysql container with volume, create db, stop container and check data

  ```docker run --platform linux/x86_64 -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v mysql-data:/var/lib/mysql -d mysql ```

  ```docker ps ```

  ```docker exec -it 31 mysql ```

