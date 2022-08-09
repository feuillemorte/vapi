cd src
if [ -f app.log ]; then
    rm app.log
fi

TIMEOUT=10
export FLASK_APP=dull_api
flask run --host=0.0.0.0 --port 5000 >app.log 2>&1 &

COUNTER=0
while true ; do
    if [ $COUNTER -gt $TIMEOUT ]; then
        >&2 echo "Can't run flask. Please, check the app.log for details:"
        if [ -f app.log ]; then
            >&2 cat app.log
        fi
        exit 1
    fi
    if [ -f app.log ]; then
        if grep -q -i "running on" app.log; then
            break
        fi
    fi
    sleep 1
    COUNTER=$((COUNTER+1))
done

echo $!
