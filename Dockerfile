FROM 	ubuntu:24.04

RUN 	apt-get update && \
	apt-get upgrade -y && \
    apt-get install python3 && \
    apt-get install python3-pip && \
    apt-get install python3.12-venv && \
    apt-get install git && \
    git clone https://github.com/SaralaSewwandi/project.git && \
    cd project && \
    # Set the working directory inside the container
    #WORKDIR /project
    python3.12 -m venv env && \
    source env/bin/activate && \
    pip install -r requirements.txt && \
    # Expose the port Flask runs on (default 5000)
    EXPOSE 5000 && \
    # Command to run the application when the container starts
    CMD ["python3.12", "Convolutional_Neural_Network/restClient.py"]