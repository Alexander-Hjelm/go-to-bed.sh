prodStartTime="040000"
prodEndTime="233000"

currentTime=`date +"%H%M%S"`
echo $prodStartTime
echo $prodEndTime
echo $currentTime
while true
do
  if [[ ! "$currentTime" < "$prodStartTime" && ! "$currentTime" > "$prodEndTime" ]]; then
    echo "do nothing"
  else
    echo "shutting down"
    shutdown
  fi

  sleep 100
done

