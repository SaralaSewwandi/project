FROM 	ubuntu:24.04

RUN apt update && apt install sudo -y 
RUN apt-get update && apt-get install -y git
#CMD ["git", "--version"]
RUN cd home/
RUN git clone https://github.com/SaralaSewwandi/project.git 
RUN cd project/ 
# Set the working directory
WORKDIR /project  
#RUN apt-get install -y python3 
#RUN apt-get install -y python3-pip 
RUN apt-get install -y python3.12-venv 
RUN python3.12 -m venv env 
#CMD source env/bin/activate 
# Install the application dependencies
RUN env/bin/pip3  install -r  requirements.txt
# Expose the port Flask runs on (default 5000)
EXPOSE 5000 
#CMD  source env/bin/activate 
# Command to run the application when the container starts
CMD ["env/bin/python3.12", "Convolutional_Neural_Network/restClient.py"]

