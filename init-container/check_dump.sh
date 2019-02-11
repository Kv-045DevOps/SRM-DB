until pg_isready; do echo waiting for database; sleep 2; done;
export SELECT=$(psql -t -c "select 1 from information_schema.tables where table_schema='public' and table_name='department'")
if [ $SELECT = 1 ]
then
    exit 0
else
    psql -f dbdump
    exit 0
fi