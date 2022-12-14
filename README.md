# django-twitter-term1
使用另一個repository code base origin2 到這來，使用https://medium.com/fuzzy-code/git-push-to-new-repo-from-existing-repos-branch-acb8bef3f7be
重新寫新的code push 到此處


Twitter codebase
啟動虛擬機
vagrant up

進入虛擬機中command
vagrant ssh

cd /vagrant

重新執行腳本
vagrant provision

關閉虛擬機
sudo shutdown -h now

開啟django
到網站localhost

虛擬機中到/vagrant後
啟動項目
python manage.py runserver 0.0.0.0:8000

新建一個app
python manage.py startapp accounts

打開db，操作db
mysql -uroot -pyourpassword
use twitter 
select * from auth_user


在虛擬機中手動創建tweets的
python manage.py startapp tweets

修改數據庫，告訴數據庫添加的
文件夾中有migrations
python manage.py makemigrations
若是文件夾中沒有migrations這個文件夾
python manage.py makemigrations ‘model_name'

產生對數據庫的真正修改
python manage.py makemigrations
python manage.py migrate

安裝包
pip freeze > requirements.txt

push code to remote
 git push origin -u branch

啟動unit test
python manage.py test
test更詳細的
python manage.py test -v2

啟動交互窗口
python manage.py shell
