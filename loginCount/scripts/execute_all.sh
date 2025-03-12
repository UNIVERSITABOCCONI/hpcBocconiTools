# clean
base_path=/root/utilities/hpcBocconiTools/loginCount/scripts/
mv ${base_path}logins_* ${base_path}data_logins/
rm -f ${base_path}data.txt

# define start end date of login count
start=$(date --date="${date} -8 day" +%Y-%m-%d)
end=$(date --date="${date} -1 day" +%Y-%m-%d)

/software/miniconda3/bin/python ${base_path}logins.py $start $end

/software/miniconda3/bin/python ${base_path}process_files.py > ${base_path}data.txt

/software/miniconda3/bin/python ${base_path}make_histo.py

# from your PC
# scp root@lnode01-da.hpc.unibocconi.it:/root/utilities/hpcBocconiTools/loginCount/scripts/logins_histo.png .

