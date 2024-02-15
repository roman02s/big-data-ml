from diagrams import Diagram
from diagrams.c4 import Container, Person, Relationship, System, SystemBoundary

graph_attr = {
    "splines": "spline",
}

with Diagram(filename="./docs/diagrams/level 2", direction="TB", graph_attr=graph_attr):
    user = Person("User")

    platform = System(
        name="VK Platform",
        description="VK's social media and advertising platform."
    )

    with SystemBoundary("CTR Prediction System"):
        data_collection_service_1 = Container(
            "Data Collection Service (Users)",
            description="Collects and aggregates data on users' behavior."
        )

        data_collection_service_2 = Container(
            "Data Collection Service (Platform)",
            description="Collects and aggregates data from advertising platforms and other sources."
        )

        data_collection_service_3 = Container(
            "Data Collection Service (Campaigns)",
            description="Collects and aggregates data from advertising campaigns."
        )

        data_processing_service = Container(
            "Data Processing Service",
            description="Cleans, processes, and prepares data for prediction models."
        )

        ml_training_service = Container(
            "ML Model Training Service",
            description="Trains machine learning models."
        )

        ml_prediction_service = Container(
            "Model Inference Service",
            description="Provides online predictions from models."
        )

        hdfs = Container(
            "Data Warehouse",
            description="System for storing large volumes of data."
        )

        kafka = Container(
            "Streaming Platform",
            description="System for processing and transferring streaming data."
        )
        kafka_2 = Container(
            "Streaming Platform",
            description="System for processing and transferring streaming data."
        )

        monitoring_service = Container(
            "Monitoring Service",
            description="Tracks the state, performance, and metrics of the model inference service."
        )

        api_gateway = Container(
            "API Gateway",
            description="Provides unified access to system services."
        )

    user >> Relationship("Interactively interacts with") >> platform
    platform >> Relationship("User data") >> data_collection_service_1
    platform >> Relationship("Platform data") >> data_collection_service_2
    platform >> Relationship("Campaign data") >> data_collection_service_3
    [data_collection_service_1, data_collection_service_2, data_collection_service_3] >> Relationship("Transmits data") >> kafka
    kafka >> Relationship("Transfers streaming data") >> data_processing_service
    data_processing_service >> Relationship("Stores processed data in") >> kafka_2
    kafka_2 >> Relationship("Transfers processed data") >> [hdfs, ml_prediction_service]
    ml_training_service >> Relationship("Provides data for") >> hdfs
    ml_prediction_service >> Relationship("Model loading") >> ml_training_service
    platform >> Relationship("Requests model results/metrics for auction", reverse=True) >> api_gateway
    api_gateway >> Relationship("Provides access to prediction service", reverse=True) >> ml_prediction_service
    api_gateway >> Relationship("Ensures monitoring of the model inference service") >> monitoring_service
    monitoring_service >> Relationship("") >> hdfs
    monitoring_service >> Relationship("Monitors the state") >> [ml_prediction_service, ml_training_service]
