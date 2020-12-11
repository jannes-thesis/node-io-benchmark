node_script=$1
files_dir=$2
amount_files=$3
output_json=$4

cmd_str="UV_THREADPOOL_SIZE={num_threads} node ../node_scripts/${node_script} ${files_dir} ${amount_files}"
hyperfine --prepare 'sudo clear_page_cache' \
	--parameter-scan num_threads 1 8 "${cmd_str}"\
    --min-runs 3 \
	--export-json $output_json
