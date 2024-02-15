from diagrams import Diagram
from diagrams.c4 import Person, System, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram(filename="./docs/diagrams/level 1", outformat="png", direction="TB", graph_attr=graph_attr):
    advertiser = Person(
        name="Advertiser",
        description="A business or individual placing ads"
    )

    user = Person(
        name="User",
        description="End-user who interacts with ads"
    )

    ctr_prediction_system = System(
        name="CTR Prediction System",
        description="System predicting the Click-Through Rate of ads"
    )

    platform = System(
        name="VK Platform",
        description="VK's social media and advertising platform."
    )

    advertiser >> Relationship("Uses") >> platform
    user >> Relationship("Interacts with ads, data collected by") >> platform
    ctr_prediction_system >> Relationship("Predicts of ads using") >> platform
    platform >> Relationship("Provides advertising platform and user data") >> ctr_prediction_system
