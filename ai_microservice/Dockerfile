# Pull base image.
FROM ubuntu:17.10

# Install Python.
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv python-setuptools wget && \
  rm -rf /var/lib/apt/lists/*

RUN pip install boto3

# Download latest model from S3
ADD download_model.py /
# Flask App
ADD app.py /
# Model Serving Library
ADD dbml-local-0.3.0-spark2.3.jar /

# Install Java.
RUN \
apt-get update && apt-get install -y software-properties-common python-software-properties && \
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer


# Define working directory.
WORKDIR /

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

ENV JYTHON_VERSION 2.7.1
RUN apt-get update && apt-get install -y curl && apt-get clean

RUN curl -L "http://search.maven.org/remotecontent?filepath=org/python/jython-installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar" -o jython_installer-${JYTHON_VERSION}.jar
RUN java -jar jython_installer-${JYTHON_VERSION}.jar -s -d $HOME/jython-${JYTHON_VERSION} -i ensurepip
RUN ln -s $HOME/jython-${JYTHON_VERSION}/bin/jython /usr/bin
RUN rm jython_installer-${JYTHON_VERSION}.jar
RUN jython -m pip install flask boto3

CMD jython app.py $access_key $secret_access $bucket_name $zip_file_path
