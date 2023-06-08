# docent.buildout
cd /home/testsite/webapps/plone51

./bin/buildout -c buildout_master.cfg

./bin/instance restart

=============
THIS IS WHAT PRODUCT DOES - THIS NEEDS TO BE UPDATED FOR PLONE 6 AND THE PROPER PRODUCTS

* install all products, including my products on Github 
* install backup:  give location as:  "Backups/<site name>" at root of my site.  Will it create <folder> if not there?  make sure it Isn't backed up on the local of the plone instance.
* crontab?  How?  define cron job.  How?() - a) weekly for backup done, b) coming soon (daily - twice/day) 
* new Roles per the site definition document.  TBD
* timezone.  (done)
* restart if not running   TBD
