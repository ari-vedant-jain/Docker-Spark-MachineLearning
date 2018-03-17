#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

os.system('python download_model.py')
import sys
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

    localModel = ModelFactory.loadModel("dbfs/mnt/ved-demo/housing/pipeline/")
    localModel.setOutputCols("prediction")
    data = request.data
    pred = localModel.transform(data)
    return pred


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
