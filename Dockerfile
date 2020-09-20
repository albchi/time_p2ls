FROM   ubuntu:18.04
ADD   time_p2ls.sh /usr/src/time_p2ls.sh
RUN   chmod +x /usr/src/time_p2ls.sh 
CMD   ["/usr/src/time_p2ls.sh"]
