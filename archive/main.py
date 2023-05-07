__author__ = "David Dawson"
__copyright__ = "Copyright 2020, David Dawson"
__credits__ = ["David Dawson"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dave Dawson"
__email__ = "davedawson.co@gmail.com"
__status__ = "Production"

from airflow import DAG
import dagfactory
from pathlib import Path

p = Path("airflow_dags/config/example_dag_factory.yml")
full = p.resolve()
example_dag_factory = dagfactory.DagFactory(full.as_posix())

# Creating task 
example_dag_factory.clean_dags(globals())
example_dag_factory.generate_dags(globals())