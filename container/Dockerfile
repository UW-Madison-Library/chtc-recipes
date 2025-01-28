# Used for stephenmeyer/alpine-wos-explorer:X.X.X-chtc versions pushed to Docker Hub

# 1. Begin with the very lightweight Alpine Linux image.

FROM alpine

# 2. Install a basic bash, Python and git environment.

RUN apk add --update bash python3 py3-pip python3-dev git

# 3.0 Clone and install the primary dependency, the Web of Science Explorer package.

RUN mkdir -p /tmp/setup
RUN git clone https://github.com/UW-Madison-Library/wos-explorer.git /tmp/setup/wos-explorer

# 3.1 From within the cloned repository, build and install the package.

WORKDIR /tmp/setup/wos-explorer
RUN python setup.py sdist
RUN pip install --break-system-packages dist/wos_explorer-0.10.0.tar.gz

# 3.2 Install the punctuation data required by the wos-explorer's dependency, NLTK.

RUN python3 -c "import nltk; nltk.download('punkt_tab', download_dir='/usr/local/share/nltk_data')"

# 4.0 Create the data directories for the sample data and script.

RUN mkdir -p /sample-data/web-of-science
RUN mkdir -p /work
WORKDIR /work

# 4.1 Copy the sample data and script to the image that are used by the default command.

COPY sample-records.json /sample-data/web-of-science
COPY confirmation_script.py /work

# 5. Setup the default command that will confirm the image container is working correctly.

CMD ["python", "/work/confirmation_script.py"]
