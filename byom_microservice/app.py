#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

cmd = "python download_model.py %s %s %s %s" % (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
os.system(cmd)
sys.path.append('dbml-local-0.3.0-spark2.3.jar')

from com.databricks.ml.local import ModelFactory
from flask import Flask, abort, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_input():
    app.logger.info("{} request received from: {}".format(
        request.method, request.remote_addr))
    if not request.get_json():
       app.logger.error("Request has no data or request is not json, aborting")
       abort(400)
    pipeline = sys.argv[4]
    pipeline = pipeline.replace(".zip", "/")
    path = "dbfs/mnt/ved-demo/" + pipeline
    localModel = ModelFactory.loadModel(path)
    localModel.setOutputCols("prediction")
    data = request.data
    pred = localModel.transform(data)
    return pred


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
