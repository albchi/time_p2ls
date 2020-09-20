FROM   ubuntu:18.04
ADD   ./hello.sh /usr/src/hello.sh
RUN   chmod +x /usr/src/hello.sh
CMD   ["/usr/src/hello.sh"]
