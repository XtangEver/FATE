FROM mcr.microsoft.com/java/jre:8u192-zulu-alpine
RUN apk add tzdata
WORKDIR /data/projects/fate/fateboard/

ARG fateboard_version

COPY fateboard ./
EXPOSE 8080

CMD java -Dspring.config.location=/data/projects/fate/fateboard/conf/application.properties  -Dssh_config_file=/data/projects/fate/fateboard/conf  -Xmx2048m -Xms2048m -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Xloggc:gc.log -XX:+HeapDumpOnOutOfMemoryError  -jar fateboard.jar