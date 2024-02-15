from diagrams import Diagram
from diagrams.c4 import Container, Person, Relationship, System, SystemBoundary

graph_attr = {
    "splines": "spline",
}

with Diagram(filename="./docs/diagrams/level_3-ml-model-training-service", direction="TB", show=False, graph_attr=graph_attr):
    user = Person("User")

    platform = System(
        name="VK Platform",
        description="VK's social media and advertising platform."
    )

    hdfs = Container(
        "Data Warehouse",
        description="System for storing large volumes of data."
    )
    monitoring_service = Container(
        "Monitoring Service",
        description="Monitors the training process and system performance."
    )

    ml_prediction_service = Container(
        "Model Inference Service",
        description="Provides online predictions from models."
    )

    with SystemBoundary("ML Model Training Service"):
        data_ingestion_component = Container(
            "Data Ingestion Container",
            description="Ingests and organizes data for training."
        )

        preprocessing_component = Container(
            "Data Preprocessing Container",
            description="Preprocesses data to make it suitable for training."
        )

        training_component = Container(
            "Model Training Container",
            description="Trains machine learning models using preprocessed data."
        )

        model_storage_component = Container(
            "Model Storage Container",
            description="Stores trained models for future inference."
        )

        # Data flow
        hdfs >> Relationship("Provides raw data to") >> data_ingestion_component
        data_ingestion_component >> Relationship("Feeds data to") >> preprocessing_component
        preprocessing_component >> Relationship("Sends preprocessed data to") >> training_component
        training_component >> Relationship("Saves models in") >> model_storage_component
        training_component >> Relationship("Training process monitored by") >> monitoring_service
        data_ingestion_component >> Relationship("Sends logs, metrics, and data coverage to") >> monitoring_service
        preprocessing_component >> Relationship("Logs cardinality of data features to") >> monitoring_service
        model_storage_component >> Relationship("Sends models to") >> ml_prediction_service
        model_storage_component >> Relationship("Saves model dumps in") >> hdfs

    user >> Relationship("Interacts with") >> platform
    platform >> Relationship("Gets data from platform and preprocesses it", reverse=True) >> hdfs
