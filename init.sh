#!/bin/sh
# /etc/init.d/watcher-backend

WBLOC=/usr/local/scpnet/watcher-backend/frontend.py
USER=scpnet

case "$1" in
  start)
    if [ -z $(pgrep -f "python3 $WBLOC" | head -1) ]
      then
        echo "Starting watcher-backend"
        sudo -u $USER $WBLOC &
      else
        echo "watcher-backend is running on" $(pgrep -f "python3 $WBLOC" | awk '{print $1}')
    fi
    ;;
  stop)
    if [ -z $(pgrep -f "python3 $WBLOC" | head -1) ]
      then
        echo 'watcher-backend is not running'
      else
        echo "Stopping watcher-backend"
        echo $(pgrep -f "python3 $WBLOC")
        kill $(pgrep -f "python3 $WBLOC" | head -1)
    fi
    ;;
  status)
    if [ -z $(pgrep -f "python3 $WBLOC" | head -1) ]
      then
        echo "watcher-backend is not working"
      else
        echo "watcher-backend is running on" $(pgrep -f "python3 $WBLOC" | awk '{print $1}')
    fi
    ;;
  *)
    echo "Usage: /etc/init.d/watcher-backend{start|status|stop}"
    exit 1
    ;;
esac
 
exit 0
