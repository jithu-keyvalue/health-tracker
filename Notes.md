📝 Notes
--------

- 🐳 Docker
    Run apps in isolated containers
    ```bash
    # Run a container
    docker run -d --name mydb postgres:15

    # View containers
    docker ps

    # Stop container
    docker stop mydb
    ```
    [Docs](https://docs.docker.com/get-started/)

- 🧩 Docker Compose
    Run multiple containers together
    ```yaml
    services:
      db:
        image: postgres:15
        env_file: .env
    ```

    Start services:
    ```bash
    docker compose up -d  # Run in background
    ```
    [Docs](https://docs.docker.com/compose/)

- 🌐 Port Mapping
    Connect host to container ports
    ```yaml
    ports:
      - "8080:80"    # host:container
      - "5432:5432"  # postgres default
    ```
    [Docs](https://docs.docker.com/config/containers/container-networking/)

- 📦 Docker Volumes
    Keep container data persistent
    ```yaml
    volumes:
      - mydata:/var/lib/postgresql/data
    ```
    [Docs](https://docs.docker.com/storage/volumes/)

- 🗃️ Postgres Setup
    Required environment variables
    ```bash
    POSTGRES_DB=mydb
    POSTGRES_USER=admin
    POSTGRES_PASSWORD=secret
    ```
    [Docs](https://hub.docker.com/_/postgres)

- 🔌 Postgres Connect
    Test database connection
    ```bash
    # Connect to container
    docker exec -it db-name psql -U user -d dbname

    # Test query
    SELECT version();
    ```
    [Docs](https://www.postgresql.org/docs/current/app-psql.html)