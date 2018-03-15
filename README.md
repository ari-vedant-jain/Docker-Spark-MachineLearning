# Containerized Model Serving using Databricks Model Export Library and Docker

## As a standalone app (outside of docker), use the following command:

<code>$ cd docker/ </code>

<code> $ jython -J-cp dbml-local-0.3.0-spark2.3.jar housing.py</code>


## For running in docker


<code>$ docker run -it vedantja/realestate_price_predictor</code>

## Output
### You should see the following output:
```
Enter information about the house below.
> number of bedrooms: 5 
> number of bathrooms: 3 
> sq footage of living area: 1000
> sq footage of the lot: 2000
> zipcode: 98039
> condition: 5
```
```
Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 PipelineModel model with 0 rows from pipeline/data.
Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 feature.StringIndexerModel model with 1 rows from pipeline/stages/0_StringIndexer_453bb914baee6462c1db/data.
Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 feature.VectorAssembler model with 0 rows from pipeline/stages/1_VectorAssembler_4b21b95f4a78010ae379/data.
Mar 13, 2018 8:10:38 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 regression.DecisionTreeRegressionModel model with 63 rows from pipeline/stages/2_DecisionTreeRegressor_4dd187cc681dd86b9635/data.
```

#### And the prediction will be output like this: 
``` 
{"prediction":571955.1501706485} 
```

## For running in docker
For running it as a microservice 

<code>docker run -p 15000:5000 vedantja/model_microservice_example</code>
### You should see the following output:
```
vjain:docker vedantjain$ docker run -p 15000:5000 vedantja/model_microservice_example
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 556-327-343
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
#### The application is running on port 5000. So open another terminal window and submit the following command:

<code>curl -H 'Content-Type:application/jsms": 4, "sqft_living": 1000, "sqft_lot": 2000, "zipcode": "98039", "condition": 5}' localhost:15000</code>

### You will see the following output in the new window:
```
{"prediction":571955.1501706485}
```
#### The output in the docker console should look something like this:
```
--------------------------------------------------------------------------------
INFO in app [./app.py:13]:
POST request received from: 172.17.0.1
--------------------------------------------------------------------------------
Mar 15, 2018 7:48:27 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 PipelineModel model with 0 rows from pipeline/data.
Mar 15, 2018 7:48:27 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 feature.StringIndexerModel model with 1 rows from pipeline/stages/0_StringIndexer_453bb914baee6462c1db/data.
Mar 15, 2018 7:48:27 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 feature.VectorAssembler model with 0 rows from pipeline/stages/1_VectorAssembler_4b21b95f4a78010ae379/data.
Mar 15, 2018 7:48:27 PM com.databricks.ml.local.util.Logging$class logInfo
INFO: Importing version 0.1.1 regression.DecisionTreeRegressionModel model with 63 rows from pipeline/stages/2_DecisionTreeRegressor_4dd187cc681dd86b9635/data.
172.17.0.1 - - [15/Mar/2018 19:48:27] "POST / HTTP/1.1" 200 -
```
