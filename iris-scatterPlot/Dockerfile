FROM rocker/shiny:3.6.1
LABEL maintainer "Anket Sah <anket.sah@sjsu.edu>"

WORKDIR /srv/shiny-server

RUN apt-get update \
    && apt-get install -y libsasl2-dev libssl-dev
RUN echo \
  'options(repos=list(CRAN="https://cloud.r-project.org/"))' > \
  ".Rprofile"
RUN R -e "install.packages(c('ggplot2','gridExtra'))"

ADD https://raw.githubusercontent.com/rocker-org/shiny/master/shiny-server.sh /usr/bin/

COPY ./ ./

EXPOSE 3838

RUN chmod a+w .

RUN chmod +x /usr/bin/shiny-server.sh

CMD /usr/bin/shiny-server.sh
