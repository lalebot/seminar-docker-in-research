FROM python:3.9.14-slim-bullseye
RUN apt-get update && apt-get install -y --no-install-recommends git sqlite3 wget tar && apt-get clean

#RUN wget https://meme-suite.org/meme/meme-software/5.4.1/meme-5.4.1.tar.gz
#RUN tar zxf meme-5.4.1.tar.gz
#RUN cd meme-5.4.1 \
#    && ./configure --prefix=$HOME/meme --enable-build-libxml2 --enable-build-libxslt\
#    && make && make test && make install

#RUN export PATH=$HOME/meme/bin:$HOME/meme/libexec/meme-5.4.1:$PATH

#RUN apt-get -y install ghostscript imagemagick openmpi-bin tcsh perl libexpat1-dev zlib1g-dev autoconf automake libtool libxml2  libxml-parser-perl

RUN pip install urllib3 

RUN cd ..
ADD https://raw.githubusercontent.com/lalebot/pip-prom-tom/master/conf.ini .
ADD https://raw.githubusercontent.com/lalebot/pip-prom-tom/master/exa_prom.txt .
ADD https://raw.githubusercontent.com/lalebot/pip-prom-tom/master/pip_prom_tom.py .

#CMD ["python","pip_prom_tom.py -i exa_prom.txt -o proyecto1 -u 1000 -g 250 -p 1"]