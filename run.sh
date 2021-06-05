#!/bin/bash

current_md5=`md5sum mymkdoc/docs.zip`
current_yml_md5=`md5sum mymkdoc/mkdocs.yml | cut -d" " -f1`
old_yml_md5=`md5sum mkdoc/mkdocs.yml | cut -d" " -f1`

#echo "current_yml_md5:"${current_yml_md5}
#echo "old_yml_md5:"${old_yml_md5}

if [[ "${current_yml_md5}" != "${old_yml_md5}" ]];then
	echo "yml has been changed"
	rm -rf mkdoc/mkdocs.yml
	cp mymkdoc/mkdocs.yml mkdoc/
else
	echo "yml has not been changed"
fi

if [[ -f "mymkdoc/docs_zip.md5" ]];then
	old_md5=`head -n 1 mymkdoc/docs_zip.md5`
	if [[ "${current_md5}" != "${old_md5}" ]];then
		echo "file has been changed"
		rm -rf mymkdoc/docs
		rm -rf mkdoc/docs
		#unzip -o myNotebook/notebooks.zip -d dao/notebooks
		python3 unzip.py mymkdoc/docs.zip mkdoc/docs/
		echo "${current_md5}" > mymkdoc/docs_zip.md5
	else
		echo "file has not been changed"
	fi
else
	md5sum mymkdoc/docs.zip > mymkdoc/docs_zip.md5
fi

cd mkdoc
mkdocs gh-deploy
