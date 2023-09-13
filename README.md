# PES2UG20CS016_Jenkins
(Creating a DevOps Pipeline, CI/CD tool)

## docker-compose stack for Kafka and its components

This docker-compose stack will create a Kafka cluster with a single Zookeeper node and a single Kafka broker. It will also create a Kafka topic called my-topic with 3 partitions and 1 replica.

To create the docker-compose stack, you can run the following command:

```docker-compose up -d```

This will start the Kafka cluster and create the my-topic topic.

You can verify that the Kafka cluster is up and running by running the following command:

```docker-compose ps```

This will show you the status of all the services in the docker-compose stack. The Kafka broker should be in the Up state.

You can also verify that the my-topic topic has been created by running the following command:

```kafka-topics --list --bootstrap-server kafka:9092```

This will list all the topics in the Kafka cluster. The my-topic topic should be listed.


## Install TimescaleDB or Postgres

### To install TimescaleDB 
```https://docs.timescale.com/latest/getting-started/installation/```

### To install Postgres
```https://www.postgresql.org/docs/14/tutorial-install.html```

The following commands will create a database called my_database and a table called my_table in TimescaleDB:
```
CREATE DATABASE my_database;

CREATE TABLE my_table (
  id serial PRIMARY KEY,
  name text NOT NULL,
  age integer
);
```


### Create a Kafka JDBC connector service in the docker-compose stack
```
kafka-jdbc-connector:
  image: confluentinc/cp-kafka-connect-jdbc:latest
  depends_on:
    - kafka
    - zookeeper
  environment:
    CONNECT_BOOTSTRAP_SERVERS: kafka:9092
    CONNECT_DATABASE_URL: jdbc:timescaledb://localhost:5432/my_database
    CONNECT_DATABASE_USER: timescaledb
    CONNECT_DATABASE_PASSWORD: password
    CONNECT_TABLE: my_table
```

## To create a JDBC sink connector in the Kafka Connect UI. To do this, 
***follow these steps:***
```
1.) Go to the Kafka Connect UI.
2.) Click on the "Connectors" tab.
3.) Click on the "Create Connector" button.
4.) Select the "JDBC Sink Connector" connector.
5.) Enter the following configuration values:
    * Name: The name of the connector.
    * Connection URL: The JDBC connection URL to the TimescaleDB database.
    * Username: The username for the TimescaleDB database.
    * Password: The password for the TimescaleDB database.
    * Table: The name of the table to write data to.
6.) Click on the "Create" button.
```
