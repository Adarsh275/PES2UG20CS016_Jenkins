# PES2UG20CS016_Jenkins
(Creating a DevOps Pipeline, CI/CD tool)


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
