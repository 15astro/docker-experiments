# docker-experiments
Repo to document all experiments with Docker

### Docker Volumes
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

### Application Development with Docker:
1. Using monorepo vs polyrepo
2. Using env specific files to store environmental variables - ./dev.env, test.env
3. Accessing env variables using os.getenv in app
4. Debugging
5. CI: build, run, test, push docker images to docker hub/docker registry
6. Smoke test using application port checks 

### Docker Best Practices:
1. Use light images - base > slim > alpine
2. Copy only required files to image
3. Add .dockerignore 
4. Use exact versions of packages when installing packages using apt
5. Use COPY statements as late as possible in dockerfile - allows caching
6. Add less changing statements earlier of dockerfile - allows caching
7. Every RUN, COPY & ADD adds new layer. Add multiple RUN commands together
8. Multistage build
9. Add labels - git repo, maintainer build date, build #, git commit hash
10. Add --init to add avoid pid 1 problem
11. Use tagged images vs latest as latest may change
12. Run with non-root. Use USER directive in dockerfile
13. Use HEALTHCHECK directive within dockerfile for healthcheck
14. Use Linter


