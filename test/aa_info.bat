
for %%f in (*.json) do "mongoimport.exe" --jsonArray --db GLOBIGDATA --collection TRAIN_PUBLICATION --file %%~nf.json 