bash start_backend.sh
bash start_frontend.sh
bash -c "trap : TERM INT; sleep infinity & wait"
