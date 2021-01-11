## 2020-01-11 Aloodak Renewed
Aloodak is now refactored!

* Aloodak now uses the official IQAir API instead of Web Scraping
* Configuring Aloodak is now done using the `config.conf.json` file
* Aloodak now uses CRON to run instead of an infinite loop
* Aloodak now stores its generated content in memory instead of saving them as files.
* PM 2.5 was dropped out of Aloodak due to API limitations
* Dropped use of Pyrogram and BS4 in favor of requests
