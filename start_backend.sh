cd src/backend
if [ -f app.log ]; then
    rm app.log
fi

TIMEOUT=10
export FLASK_APP=dull_api
nohup flask run --host=0.0.0.0 --port 5000 2> error.log > /dev/null &
echo $!


COUNTER=0
while true ; do
    if [ $COUNTER -gt $TIMEOUT ]; then
        >&2 echo "Can't run flask. Please, check the app.log for details:"
        echo ""
        if [ -f error.log ]; then
            >&2 cat error.log
        fi
        exit 1
    fi
    if [ -f app.log ]; then
        if grep -q -i "running on" app.log; then
            grep -i "running on " app.log | awk '{print $4}'
            break
        fi
    fi
    sleep 1
    COUNTER=$((COUNTER+1))
done
