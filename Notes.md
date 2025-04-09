📝 Notes  
--------

- 🐳 Docker  
  A tool to run apps in lightweight containers that bundle code + dependencies.  
  Great for consistent environments across dev and prod.

- 🧩 Docker Compose  
  Lets you define and run multi-container setups (like app + db) using `docker-compose.yml`.

  ```bash
  docker compose up
  ```

- 🗃️ Postgres  
  A popular open-source SQL database used to store structured data (users, health records, etc.).

- 🔐 Environment Variables  
  Keep secrets and config (like DB passwords) out of the main file.
  Stored in a .env file (e.g. docker.env).

  ```bash
  POSTGRES_DB=healthdb
  POSTGRES_USER=healthuser
  POSTGRES_PASSWORD=supersecret
  ```

- 📦 Special Postgres vars  
  These variable names are required by the official Postgres Docker image:
  - POSTGRES_DB
  - POSTGRES_USER
  - POSTGRES_PASSWORD

- 🪣 Volumes  
  Used to persist DB data even if the container stops or is removed.

  ```bash
  volumes:
    - pgdata:/var/lib/postgresql/data
  ```

  - To delete volume & start clean:

  ```bash
  docker compose down -v
  docker compose up
  ```

- 🏷️ Container Name  
  Makes it easy to refer to the container by name: `container_name: health-db`

- 🌐 Port Mapping  
  Maps container's port to your machine.

  ```bash
  "5433:5432"  # access DB via localhost:5433
  ```

- 🧪 Test the DB
  ```bash
  docker exec -it health-db psql -U healthuser -d healthdb
  ```

  Inside Postgres shell: `SELECT NOW();`

  Returns the current DB time — confirms the DB is live and responding.