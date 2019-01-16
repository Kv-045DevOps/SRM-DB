export SELECT=$(psql -t -h srmsystemdb -p 5432 -c "select 1 from information_schema.tables where table_schema='public' and table_name='department'")
if [ $SELECT -eq 1 ]
then
    exit 0
else
    psql -h srmsystemdb -p 5432 -f ~/tmp/dbdump
    exit 0
fi