# Containerized Model Serving using Databricks Model Export Library and Docker

## As a standalone app (outside of docker), use the following command:

<code>jython -J-cp dbml-local-0.3.0-spark2.3.jar housing.py</code>


## For running in docker


<code>$ docker run -it vedantja/realestate_price_predictor</code>

Enter information about the house below.
> number of bedrooms: 5
> number of bathrooms: 3
> sq footage of living area: 1000
> sq footage of the lot: 2000
> zipcode: 98039
> condition: 5


Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 PipelineModel model with 0 rows from pipeline/data.
Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 feature.StringIndexerModel model with 1 rows from pipeline/stages/0_StringIndexer_453bb914baee6462c1db/data.
Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 feature.VectorAssembler model with 0 rows from pipeline/stages/1_VectorAssembler_4b21b95f4a78010ae379/data.
Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 regression.DecisionTreeRegressionModel model with 63 rows from pipeline/stages/2_DecisionTreeRegressor_4dd187cc681dd86b9635/data.

{"prediction":571955.1501706485} 