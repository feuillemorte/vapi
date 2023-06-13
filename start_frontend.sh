cd src/frontend
if [ -f app.log ]; then
    rm app.log
fi

TIMEOUT=10
npm install 2> error.log > app.log
npm run build 2>> error.log >> app.log
nohup npm start 2>> error.log >> app.log &
echo $!


COUNTER=0
while true ; do
    if [ $COUNTER -gt $TIMEOUT ]; then
        >&2 echo "Can't run frontend server. Please, check the error.log for details:"
        echo ""
        if [ -f error.log ]; then
            >&2 cat error.log
        fi
        exit 1
    fi
    if [ -f app.log ]; then
        if grep -q -i "started server on" app.log; then
            break
        fi
    fi
    sleep 1
    COUNTER=$((COUNTER+1))
done
