# 1. Begin with the very lightweight Alpine Linux image.
# Current version: docker://stephenmeyer/alpine-wos-explorer-file-sorter:0.4.0

FROM alpine

# 2. Install a basic Python and git environment.

RUN apk add --update bash python3 py3-pip python3-dev openjdk17

# 3.0 Clone and install the primary dependency, the Web of Science Explorer package.

RUN mkdir -p /tmp/setup/wos-explorer
COPY wos_explorer-0.11.0.tar.gz /tmp/setup/wos-explorer

# 3.1 From within the cloned repository, build and install the package.

WORKDIR /tmp/setup/wos-explorer
RUN pip install --break-system-packages wos_explorer-0.11.0.tar.gz

# 3.2 Install the punctuation data required by the wos-explorer's dependency, NLTK.

RUN python3 -c "import nltk; nltk.download('punkt_tab', download_dir='/usr/local/share/nltk_data')"

# 4.0 Create the data directories for the sample data and script.

RUN mkdir -p /sample-data/web-of-science
RUN mkdir -p /work
WORKDIR /work

# 4.1 Copy the sample data and script to the image that are used by the default command.

COPY unsorted-sample.txt /sample-data/web-of-science
COPY confirmation_script.sh /work

# 4.2 Copy the file sorter

COPY filesorter-0.6.0.jar /work
COPY unsorted-sample.txt /sample-data/web-of-science

# 5. Setup the default command that will confirm the image container is working correctly.

CMD ["bash", "/work/confirmation_script.sh"]
