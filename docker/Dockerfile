# Pull base image.
FROM ubuntu:17.10

# Install Python.
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

ADD housing.py /
ADD dbml-local-0.3.0-spark2.3.jar /
ADD pipeline /pipeline

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

ENV JYTHON_VERSION 2.7.0
RUN apt-get update && apt-get install -y curl && apt-get clean

RUN curl -L "http://search.maven.org/remotecontent?filepath=org/python/jython-installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar" -o jython_installer-${JYTHON_VERSION}.jar

RUN java -jar jython_installer-${JYTHON_VERSION}.jar -s -d $HOME/jython-${JYTHON_VERSION} -i ensurepip

RUN ln -s $HOME/jython-${JYTHON_VERSION}/bin/jython /usr/bin

RUN rm jython_installer-${JYTHON_VERSION}.jar

CMD [ "jython", "./housing.py"]
