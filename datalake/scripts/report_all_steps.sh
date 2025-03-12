

/root/utilities/hpcBocconiTools/datalake/scripts/report_all_users_account_data.sh
/root/utilities/hpcBocconiTools/datalake/scripts/report_gpu_cpu_ram_daily_data.sh

/software/miniconda3/bin/python /root/utilities/hpcBocconiTools/datalake/scripts/convert_csv_to_parquet.py 
/software/miniconda3/bin/python /root/utilities/hpcBocconiTools/datalake/scripts/transfer_file_to_datalake.py 

