
for /r %%f in (*info.json) do (
"mongoimport.exe" --jsonArray --db GLOBIGDATA --collection TRAIN_PUBLICATION --file %%~nf.json
echo "blah blah blah '%%~nf'"
)
