output=$1
hyperfine --prepare 'sync; echo 3 | sudo tee /proc/sys/vm/drop_caches' \
	--parameter-scan num_threads 1 8 'UV_THREADPOOL_SIZE={num_threads} node write_files.js' \
	--export-json $output
